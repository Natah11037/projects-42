from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional, Self


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def verify_ID(self) -> Self:
        if self.contact_id.startswith("AC"):
            return self
        else:
            raise ValueError("Error: Contact ID must start with 'AC'")

    @model_validator(mode="after")
    def verifiy_physical(self) -> Self:
        if self.contact_type == ContactType.physical:
            if self.is_verified is True:
                return self
            else:
                raise ValueError("Error: Physical contact"
                                 " reports must be verified")
        return self

    @model_validator(mode="after")
    def verifiy_telepathic(self) -> Self:
        if self.contact_type == ContactType.telepathic:
            if self.witness_count > 2:
                return self
            else:
                raise ValueError("Error: Telepathic contact requires"
                                 " at least 3 witnesses")
        return self

    @model_validator(mode="after")
    def verifiy_message_for_signal(self) -> Self:
        if self.signal_strength > 7.0:
            if self.message_received:
                return self
            else:
                raise ValueError("Error: Strong signals (> 7.0) should include"
                                 " received messages")
        return self


def main() -> None:
    try:
        contacts = [
            {
                "contact_id": "AC_2024_001",
                "timestamp": "20070608",
                "location": "Area 51, Nevada",
                "contact_type": "radio",
                "signal_strength": 8.5,
                "duration_minutes": 45,
                "witness_count": 5,
                "message_received": "Greetings from Zeta Reticuli",
                "is_verified": True
            },
            {
                "contact_id": "AC_2024_002",
                "timestamp": "20070608",
                "location": "Area 51, Nevada",
                "contact_type": "telepathic",
                "signal_strength": 8.5,
                "duration_minutes": 45,
                "witness_count": 2,
                "message_received": "Zeta Reticuli want to dominate all "
                "the humans",
                "is_verified": True
            }
        ]

        print("\nAlien Contact Log Validation")
        for contact in contacts:
            alien = AlienContact.model_validate(contact)
            print("======================================")
            print("Valid contact report:")
            print(f"ID: {alien.contact_id}")
            print(f"Type: {alien.contact_type.name}")
            print(f"Location: {alien.location}")
            print(f"Signal: {alien.signal_strength}")
            print(f"Duration: {alien.duration_minutes}")
            print(f"Witnesses: {alien.witness_count}")
            print(f"Message: {alien.message_received}\n")
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
