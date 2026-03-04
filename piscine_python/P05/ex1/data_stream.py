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

    def filter_data(self, data_batch: list[Any], criteria:
                    Optional[str] = None) -> list[Any]:
        if criteria == "Activate":
            temperatures = []
            for data in data_batch:
                if data.startswith("temp"):
                    parts = data.split(":")
                    save_temp = float(parts[1])
                    if save_temp >= 50 or save_temp <= -20:
                        temperatures.append(save_temp)
            return (temperatures)

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

    def filter_data(self, data_batch: list[Any], criteria:
                    Optional[str] = None) -> list[Any]:
        if criteria == "Activate":
            large_trans = []
            for data in data_batch:
                parts = data.split(":")
                save_trans = float(parts[1])
                if save_trans >= 100:
                    large_trans.append(save_trans)
            return (large_trans)

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


class StreamProcessor():
    def __init__(self, streams: list[DataStream] = None):
        if not streams:
            streams = []
        self.streams = streams

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: Dict[DataStream, list[Any]]) -> None:
        print("Batch 1 Results:")
        for stream, data in batches.items():
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {len(data)} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {len(data)} operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {len(data)} events processed")


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

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    processor = StreamProcessor([sensor_001, trans_001, event_001])
    batches = {
        sensor_001: list_for_sensor,
        trans_001: list_for_transaction,
        event_001: list_for_event
    }
    processor.process_all(batches)

    filtered_sensor = sensor_001.filter_data(list_for_sensor, "Activate")
    filtered_transaction = trans_001.filter_data(list_for_transaction,
                                                 "Activate")
    try:
        l_sensor = len(filtered_sensor)
        l_trans = len(filtered_transaction)
    except TypeError:
        print("\nFilter is not activate. if you want to turn in on"
              " put on the criteria argument 'Activate'")
    else:
        print("\nStream filtering active: High-priority data only")
        print(f"Filtered results: {l_sensor} "
              f"critical sensor alerts, {l_trans}"
              f" large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
