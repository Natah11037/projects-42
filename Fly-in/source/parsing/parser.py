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
            for i, (index, line) in enumerate(valid_lines):
                try:
                    self._parse_ligne(line, i, index)
                except ValueError as e:
                    print(e)
            self.parse_hub()
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

    def _parse_ligne(self, line: str, i: int, index: int):
        if i == 0:
            if line.startswith("nb_drones:"):
                try:
                    nb_drones = int(line.split(":")[1].strip())
                    if nb_drones <= 0:
                        raise ValueError("Error: Number of drones cannot "
                                         "be negative or zero on "
                                         f"line {index}.")
                    else:
                        self.data["nb_drones"] = nb_drones
                except ValueError:
                    raise ValueError("Error: Invalid number of drones "
                                     f"on line {index}.")
            else:
                raise ValueError("Error: First line must specify "
                                 f"number of drones on line {index}.")
        else:
            if line.startswith("start_hub:"):
                self.data["start_hub"] = line.split(":")[1].strip()
            elif line.startswith("end_hub:"):
                self.data["end_hub"] = line.split(":")[1].strip()
            elif line.startswith("hub:"):
                self.data["hub"].append(line.split(":")[1].strip())
            elif line.startswith("connection:"):
                self.data["connections"].append(line.split(":")[1].strip())

    def _parse_hub_raw(self, raw: str) -> dict:
        parts = raw.split()
        name = parts[0]
        try:
            x = int(parts[1])
            y = int(parts[2])
        except (ValueError, IndexError):
            raise ValueError(f"Error: Invalid coordinates for hub '{name}'.")
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
                                         f"hub '{name}'.")
                elif key == "zone":
                    if val in ["normal", "blocked", "restricted",
                               "priority"]:
                        zone = val
                    else:
                        raise ValueError("Error: Invalid zone value for "
                                         f"hub '{name}'.")
                elif key == "max_drones":
                    try:
                        max_drones = int(val)
                    except ValueError:
                        raise ValueError("Error: Invalid max_drones value for "
                                         f"hub '{name}'.")
            else:
                raise ValueError(f"Error: Invalid metadata '{part}' for "
                                 f"hub '{name}'.")
        return {"name": name, "x": x, "y": y, "color": color, "zone": zone,
                "max_drones": max_drones}

    def parse_hub(self):
        if self.data["start_hub"]:
            self.data["start_hub"] = self._parse_hub_raw(
                self.data["start_hub"])
        if self.data["end_hub"]:
            self.data["end_hub"] = self._parse_hub_raw(self.data["end_hub"])
        if self.data["hub"]:
            self.data["hub"] = [
                self._parse_hub_raw(hub) for hub in self.data["hub"]
            ]
        names = set()
        for hub in self.data["hub"]:
            if hub["name"] in names:
                raise ValueError(f"Error: Duplicate hub name '{hub['name']}'.")
            names.add(hub["name"])


if __name__ == "__main__":
    parser = Parser("01_linear_path.txt")
    data = parser.parse()
    print(f"Start hub: {data['start_hub']}\n"
          f"Hubs: {data['hub']}\n"
          f"End hub: {data['end_hub']}\n"
          f"Connections: {data['connections']}\n"
          f"Number of drones: {data['nb_drones']}")
