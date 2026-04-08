try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("please consider installing pydantic before launching the program\n"
          "pip install pydantic\n")
    exit(1)

from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(le=20, ge=1)
    power_level: float = Field(le=100.0, ge=0.0)
    oxygen_level: float = Field(le=100.0, ge=0.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    try:
        stations = [{"station_id": "Fr_001", "name": "Freyja",
                     "crew_size": "13",
                     "power_level": 90, "oxygen_level": 23,
                     "last_maintenance": "20070608",
                     "is_operational": True},
                    {"station_id": "Fr_001", "name": "Freyja",
                     "crew_size": "13",
                     "power_level": 11037, "oxygen_level": 23,
                     "last_maintenance": "20070608",
                     "is_operational": True}]

        print("\nSpace Station Data Validation")
        for stat in stations:
            station = SpaceStation.model_validate(stat)
            print("========================================")
            print("Valid station created:")
            print(f"ID: {station.station_id}")
            print(f"Name: {station.name}")
            print(f"Crew: {station.crew_size}")
            print(f"Power: {station.power_level}%")
            print(f"Oxygen: {station.oxygen_level}%")
            if station.is_operational is True:
                print("Status: Operational")
            else:
                print("Status: Maintenance")
            print("\n========================================")
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
