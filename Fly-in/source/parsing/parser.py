class Parser():
    def __init__(self, map: str):
        self.map = map

    def parse(self) -> dict:
        try:
            self.data = {
                "start_hub": None,
                "hub": [],
                "end_hub": None,
                "connections": [],
                "nb_drones": None,
            }
            valid_lines = self._read_file()
            if valid_lines is None:
                return None
            exist_start = False
            exist_end = False
            for i, (index, line) in enumerate(valid_lines):
                try:
                    exist_start, exist_end = self._parse_ligne(line, i, index,
                                                               exist_start,
                                                               exist_end)
                except ValueError as e:
                    print(e)
                    exit(1)
            self.parse_hub()
            self.parse_name()
            self.parse_same_connection()
            self.parse_connection()
            if self.data["nb_drones"] is None:
                raise ValueError("Error: No Number of Drones detected.")
            if self.data["start_hub"] is None:
                raise ValueError("Error: No Start Hub detected.")
            if self.data["end_hub"] is None:
                raise ValueError("Error: No End Hub detected.")
        except ValueError as e:
            print(e)
            exit(1)
        return self.data

    def _read_file(self):
        try:
            with open(self.map, 'r') as file:
                lines = file.readlines()
        except (FileNotFoundError, IOError):
            print(f"Error: File '{self.map}' not found or could not be read.")
            return None
        valid_lignes = []
        for index, line in enumerate(lines, start=1):
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            else:
                valid_lignes.append((index, line))
        return valid_lignes

    def _parse_ligne(self, line: str, i: int, index: int, exist_start: bool,
                     exist_end: bool):
        if i == 0:
            if line.startswith("nb_drones:"):
                try:
                    nb_drones = int(line.split(":")[1].strip())
                    if nb_drones <= 0:
                        raise ValueError("Error: Number of drones cannot "
                                         "be negative or zero, "
                                         f"line {index}.")
                    else:
                        self.data["nb_drones"] = nb_drones
                except ValueError:
                    raise ValueError("Error: Invalid number of drones "
                                     f", line {index}.")
            else:
                raise ValueError("Error: First line must specify "
                                 f"number of drones, line {index}.")
        else:
            if line.startswith("start_hub:"):
                if exist_start:
                    raise ValueError("Error: Multiple start_hub definitions "
                                     f", line {index}.")
                self.data["start_hub"] = (index, line.split(":")[1].strip())
                exist_start = True
            elif line.startswith("end_hub:"):
                if exist_end:
                    raise ValueError("Error: Multiple end_hub definitions "
                                     f", line {index}.")
                self.data["end_hub"] = (index, line.split(":")[1].strip())
                exist_end = True
            elif line.startswith("hub:"):
                self.data["hub"].append((index, line.split(":")[1].strip()))
            elif line.startswith("connection:"):
                self.data["connections"].append((index,
                                                 line.split(":")[1].strip()))
            else:
                raise ValueError(f"Error: Invalid line format, line {index}")
        return exist_start, exist_end

    def parse_connection(self):
        for (index, connection) in self.data["connections"]:
            parts = connection.split("-")
            list_hub_name = []
            for hub in self.data["hub"]:
                list_hub_name.append(hub.get('name', False))
            list_hub_name.append(self.data['start_hub']['name'])
            list_hub_name.append(self.data['end_hub']['name'])

            if parts[0] not in list_hub_name:
                raise ValueError(f"Error: Invalid connection '{connection}' "
                                 f",line {index}. "
                                 "Both hubs must be defined in the map.")
            if parts[1] not in list_hub_name:
                raise ValueError(f"Error: Invalid connection '{connection}' "
                                 f", line {index}. "
                                 "Both hubs must be defined in the map.")
            if parts[1] not in list_hub_name:
                raise ValueError(f"Error: Invalid connection '{connection}' "
                                 f", line {index}. "
                                 "Both hubs must be defined in the map.")
        self.data["connections"] = [connection for (_, connection) in
                                    self.data["connections"]]

    def parse_same_connection(self):
        for i, (index, connection) in enumerate(self.data["connections"]):
            connections = set(connection)
            for j, (index2, connection2) in enumerate(self.data["co"
                                                                "nnections"]):
                if i != j and connections == set(connection2):
                    raise ValueError("Error: Duplicate connection "
                                     f"'{connection}' "
                                     f"and '{connection2}', line {index}"
                                     f" and {index2}.")

    def parse_name(self):
        for hub in self.data["hub"]:
            if "-" in hub["name"]:
                raise ValueError("Error: Invalid hub name "
                                 f"'{hub['name']}'."
                                 " Hub names cannot contain '-',"
                                 f" line {hub['index']}.")
        if "-" in self.data["start_hub"]["name"]:
            raise ValueError("Error: Invalid start hub name "
                             f"'{self.data['start_hub']['name']}'."
                             " Hub names cannot contain '-',"
                             f" line {self.data['start_hub']['index']}.")
        if "-" in self.data["end_hub"]["name"]:
            raise ValueError("Error: Invalid end hub name "
                             f"'{self.data['end_hub']['name']}'."
                             " Hub names cannot contain '-',"
                             f" line {self.data['end_hub']['index']}.")

    def _parse_hub_raw(self, raw: str, index: int) -> dict:
        parts = raw.split()
        name = parts[0]
        try:
            x = int(parts[1])
            y = int(parts[2])
        except (ValueError, IndexError):
            raise ValueError("Error: Invalid coordinates for hub "
                             f"'{name}', line {index}.")
        color = None
        zone = "normal"
        max_drones = 1
        for part in parts[3:]:
            part = part.strip("[]")
            if not part:
                continue
            if "=" in part:
                key, val = part.split("=")
                if key == "color":
                    if val.isalpha():
                        color = val
                    else:
                        raise ValueError("Error: Invalid color value for "
                                         f"hub '{name}', line {index}.")
                elif key == "zone":
                    if val in ["normal", "blocked", "restricted",
                               "priority"]:
                        zone = val
                    else:
                        raise ValueError("Error: Invalid zone value for "
                                         f"hub '{name}', line {index}.")
                elif key == "max_drones":
                    try:
                        max_drones = int(val)
                        if max_drones <= 0:
                            raise ValueError("Error: Max drones value cannot"
                                             " be negative or "
                                             f"zero, line {index}.")
                    except ValueError:
                        raise ValueError("Error: Invalid max_drones value for "
                                         f"hub '{name}', line {index}.")
            else:
                raise ValueError(f"Error: Invalid metadata '{part}' for "
                                 f"hub '{name}', line {index}.")
        return {"name": name, "x": x, "y": y, "color": color, "zone": zone,
                "max_drones": max_drones, "index": index}

    def parse_hub(self):
        if self.data["start_hub"]:
            index, raw = self.data["start_hub"]
            self.data["start_hub"] = self._parse_hub_raw(raw, index)
        if self.data["end_hub"]:
            index, raw = self.data["end_hub"]
            self.data["end_hub"] = self._parse_hub_raw(raw, index)
        if self.data["hub"]:
            self.data["hub"] = [
                self._parse_hub_raw(raw, index)
                for (index, raw) in self.data["hub"]
            ]
        names = set()
        for hub in self.data["hub"]:
            if hub["name"] in names:
                raise ValueError(f"Error: Duplicate hub name '{hub['name']}'"
                                 f", line {hub['index']}.")
            names.add(hub["name"])


if __name__ == "__main__":
    parser = Parser("01_linear_path.txt")
    data = parser.parse()
    print(f"Start hub: {data['start_hub']}\n"
          f"Hubs: {data['hub']}\n"
          f"End hub: {data['end_hub']}\n"
          f"Connections: {data['connections']}\n"
          f"Number of drones: {data['nb_drones']}")
