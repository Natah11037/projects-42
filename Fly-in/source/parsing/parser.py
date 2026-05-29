class Parser():
    def __init__(self, map: str):
        self.map = map

    def parse(self) -> dict:
        data = {
            "start hub": None,
            "hub": [],
            "end hub": None,
            "connections": [],
            "nb_drones": None
        }
        valid_lines = self._read_file()
        if valid_lines is None:
            return None
        for i, (index, line) in enumerate(valid_lines):
            try:
                self._parse_ligne(line, i, index)
            except ValueError as e:
                print(e)
                return None

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
                    print(f"Error: Invalid number of drones on line {index}.")
            else:
                raise ValueError("Error: First line must specify "
                                 f"number of drones on line {index}.")
