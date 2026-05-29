class Parser():
    def __init__(self, map: str):
        self.map = map

    def parse(self):
        valid_lignes = self._read_file()
        if valid_lignes is None:
            return None
        for index, ligne in valid_lignes:
            self._parse_ligne(ligne)

    def _read_file(self):
        try:
            with open(self.map, 'r') as file:
                lines = file.readlines()
        except (FileNotFoundError, IOError):
            print(f"Error: File '{self.map}' not found or could not be read.")
            return None
        valid_lignes = []
        for index, line in enumerate(lines):
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            else:
                valid_lignes.append((index, line))
        return valid_lignes
    
    def _parse_ligne(self, ligne: str):
