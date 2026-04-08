from enum import Enum
from datetime import datetime
from typing import Self
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_id(self) -> Self:
        if self.mission_id.startswith("M"):
            return self
        else:
            raise ValueError("Mission ID must start with 'M'")

    @model_validator(mode="after")
    def verif_for_chief(self) -> Self:
        chief = False
        for member in self.crew:
            if member.rank == Rank.captain or member.rank == Rank.commander:
                chief = True
        if chief is True:
            return self
        else:
            raise ValueError("Must have at least one Commander or Captain")

    @model_validator(mode="after")
    def verif_for_exp(self) -> Self:
        if self.duration_days > 365:
            total_members = 0
            experienced = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1
                total_members += 1
            if total_members / 2 > experienced:
                raise ValueError("Long missions (> 365 days) "
                                 "need 50% experienced crew (5+ years)")
        return self

    @model_validator(mode="after")
    def active_members(self) -> Self:
        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    try:
        data = [
            {
                "mission_id": "M_zeta_001",
                "mission_name": "ZETA-01",
                "destination": "Zarbookiak",
                "launch_date": "20770608",
                "duration_days": 364,
                "crew": [
                    {
                        "member_id": "O_Kaa_001",
                        "name": "Kaatarina",
                        "rank": "officer",
                        "age": 37,
                        "specialization": "Laughter yoga trainer",
                        "years_experience": 14,
                        "is_active": True
                    },
                    {
                        "member_id": "C_Ter_001",
                        "name": "Teros",
                        "rank": "captain",
                        "age": 27,
                        "specialization": "torture and investigations",
                        "years_experience": 11,
                        "is_active": True
                    },
                    {
                        "member_id": "c_Cih_001",
                        "name": "Cihan",
                        "rank": "cadet",
                        "age": 19,
                        "specialization": "coding",
                        "years_experience": 1,
                        "is_active": True
                    },
                    {
                        "member_id": "Co_Rho_001",
                        "name": "Rhoshandiatelly-neshiaunnveshenk"
                        " Koyaanfsquatsiuty",
                        "rank": "commander",
                        "age": 30,
                        "specialization": "supervizing and guiding",
                        "years_experience": 13,
                        "is_active": True
                    },
                    {
                        "member_id": "c_Har_001",
                        "name": "Harry Potter",
                        "rank": "cadet",
                        "age": 20,
                        "specialization": "magician",
                        "years_experience": 9,
                        "is_active": True
                    }
                ],
                "mission_status": "planned",
                "budget_millions": 457.0
            },
            {
                "mission_id": "M_zeta_002",
                "mission_name": "ZETA-02",
                "destination": "Zarbookiak",
                "launch_date": "20780607",
                "duration_days": 364,
                "crew": [
                    {
                        "member_id": "O_Kaa_001",
                        "name": "Kaatarina",
                        "rank": "officer",
                        "age": 37,
                        "specialization": "Laughter yoga trainer",
                        "years_experience": 14,
                        "is_active": True
                    },
                    {
                        "member_id": "O_Ter_001",
                        "name": "Teros",
                        "rank": "officer",
                        "age": 27,
                        "specialization": "torture and investigations",
                        "years_experience": 11,
                        "is_active": True
                    },
                    {
                        "member_id": "c_Cih_001",
                        "name": "Cihan",
                        "rank": "cadet",
                        "age": 19,
                        "specialization": "coding",
                        "years_experience": 1,
                        "is_active": True
                    },
                    {
                        "member_id": "O_Rho_001",
                        "name": "Rhoshandiatelly-neshiaunnveshenk"
                        " Koyaanfsquatsiuty",
                        "rank": "officer",
                        "age": 30,
                        "specialization": "supervizing and guiding",
                        "years_experience": 13,
                        "is_active": True
                    },
                    {
                        "member_id": "c_Har_001",
                        "name": "Harry Potter",
                        "rank": "cadet",
                        "age": 20,
                        "specialization": "magician",
                        "years_experience": 9,
                        "is_active": True
                    }
                ],
                "mission_status": "planned",
                "budget_millions": 753.0
            }
        ]

        print("Space Mission Crew Validation")
        for mission in data:
            spacemission = SpaceMission.model_validate(mission)
            print("=========================================")
            print("Valid mission created:")
            print(f"Mission: {spacemission.mission_name}")
            print(f"ID: {spacemission.mission_id}")
            print(f"Destination: {spacemission.destination}")
            print(f"Budget: ${spacemission.budget_millions}M")
            print(f"Crew size: {len(spacemission.crew)}")
            print("Crew members:")
            for member in spacemission.crew:
                print(f"- {member.name} ({member.rank.name}) - "
                      f"{member.specialization}")
            print()
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
