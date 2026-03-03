#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional  # noqa: F401


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {}


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temperatures = []
            for data in data_batch:
                if data.startswith("temp"):
                    parts = data.split(":")
                    save_temp = float(parts[1])
                    temperatures.append(save_temp)

            avg_temp = sum(temperatures) / len(temperatures)
        except (ValueError, ZeroDivisionError):
            return ("Please consider to put an integer behind the ':' "
                    "characters to assign a value. Verify also that the"
                    " variable 'temp' exists")
        return (f"Stream ID: {self.stream_id}, Type: Environmental Data\n"
                f"Processing sensor batch: [{', '.join(data_batch)}]\n"
                f"Sensor analysis: {len(data_batch)} readings processed, avg "
                f"temp: {avg_temp}°C")


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            total = 0
            for data in data_batch:
                if data.startswith("buy"):
                    bought = data.split(":")
                    save_money_lost = int(bought[1])
                    total += save_money_lost
                elif data.startswith("sell"):
                    selled = data.split(":")
                    save_money_gain = int(selled[1])
                    total -= save_money_gain
        except ValueError:
            return ("Please consider to put an integer behind the ':' "
                    "characters to assign a value")
        return (f"Stream ID: {self.stream_id}, Type: Financial Data\n"
                f"Processing transaction batch: [{', '.join(data_batch)}]\n"
                f"Transaction analysis: {len(data_batch)} operations, net flow"
                f": {total} units")


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        total_errors = 0
        for data in data_batch:
            if data.startswith("error"):
                total_errors += 1
        return (f"Stream ID: {self.stream_id}, Type: System Events\n"
                f"Processing event batch: [{', '.join(data_batch)}]\n"
                f"Event analysis: {len(data_batch)} events, "
                f"{total_errors} {'errors' if total_errors > 1 else 'error'}"
                f" detected")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor_001 = SensorStream("SENSOR_001")
    list_for_sensor = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(sensor_001.process_batch(list_for_sensor))

    print("\nInitializing Transaction Stream...")
    trans_001 = TransactionStream("TRANS_001")
    list_for_transaction = ["buy:100", "sell:150", "buy:75"]
    print(trans_001.process_batch(list_for_transaction))

    print("\nInitializing Event Stream...")
    event_001 = EventStream("EVENT_001")
    list_for_event = ["login", "error", "logout"]
    print(event_001.process_batch(list_for_event))
