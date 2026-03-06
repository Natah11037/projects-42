#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol  # noqa: F401


class ProcessingStage(Protocol):
    def process(data) -> Any:
        ...


class InputStage():
    def process(data) -> Dict:
        if isinstance(data, dict):
            return (f"Input: {data}")
        elif isinstance(data, str):
            return (f'Input: "{data}"')
        else:
            return ("Input: Real-time sensor stream")


class TransformStage():
    def process(data) -> Dict:
        if isinstance(data, dict):
            save_value = data["value"]
            float(save_value)
            if data["sensor"] == "temp":
                data["sensor"] = "temperature"
            else:
                return ("Please put a good sensor like 'temp'")
            if data["unit"] != "C":
                return ("Please put a good unit like 'C'")
            else:
                data["value"] = f"{data["value"]}°C"
            if save_value > 50 or save_value < -20:
                data["unit"] = "Out of range"
            else:
                data["unit"] = "Normal range"
            return ("Transform: Enriched with metadata and validation")
        elif isinstance(data, str):
            nb_actions = 0
            parts = ",".split(data)
            for instructions in parts:
                if instructions == "action":
                    nb_actions += 1
            data = f"{nb_actions}"
            return ("Transform: Parsed and structured data")


class OutputStage():
    def process(data) -> str:
        if isinstance(data, dict):
            return (f"Output: Processed {data["sensor"]} reading: "
                    f"{data["value"]} ({data["unit"]})")
        elif isinstance(data, str):
            return (f"Output: User activity logged: {data} actions processed")


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages: list[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    @abstractmethod
    def process(data) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def process(data) -> Any:
        pass


class CSVAdapter(ProcessingPipeline):
    def process(data) -> Any:
        pass


class StreamAdapter(ProcessingPipeline):
    def process(data) -> Any:
        pass


class NexusManager():
    def __init__(self):
        self.pipelines: list[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline):
        self.pipelines.append(pipeline)

    def process_data():
        pass


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")

    print("=== Multi-Format Data Processing ===\n")

    json001 = JSONAdapter("JSON_001")
    csv001 = CSVAdapter("CSV_001")
    stream001 = StreamAdapter("Stream_001")

    json001.add_stage(InputStage)
    json001.add_stage(TransformStage)
    json001.add_stage(OutputStage)

    csv001.add_stage(InputStage)
    csv001.add_stage(TransformStage)
    csv001.add_stage(OutputStage)

    stream001.add_stage(InputStage)
    stream001.add_stage(TransformStage)
    stream001.add_stage(OutputStage)

    manager = NexusManager()

    manager.add_pipeline(json001)
    manager.add_pipeline(csv001)
    manager.add_pipeline(stream001)

    print("Processing JSON data through pipeline...")

    data_json = {
        "sensor": "temp",
        "value": 23.5,
        "unit": "C"
    }
    for stage in json001.stages:
        print(stage.process(data_json))

    print("\nProcessing CSV data through same pipeline...")

    data_csv = "user,action,timestamp"
    for stage in csv001.stages:
        data_csv = stage.process(data_csv)
        print(data_csv)
