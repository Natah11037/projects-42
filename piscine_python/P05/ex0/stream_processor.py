#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional  # noqa: F401


class DataProcessor(ABC):
    """Abstract base class for data processors."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data and return the result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor"""
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor for numeric data."""

    def process(self, data: Any) -> str:
        total = sum(data)
        avg = total / len(data)
        return (
            f"Processed {len(data)} numeric values, "
            f"sum={total}, avg={avg}"
        )

    def validate(self, data: Any) -> bool:
        """Validate if data is numeric."""
        if not isinstance(data, (list, tuple)):
            raise TypeError("type incorrect")
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("List must contain only numbers")
        return True


class TextProcessor(DataProcessor):
    """Processor for text data."""

    def process(self, data: Any) -> str:
        return (
            f"Processed text: {len(data)} characters, "
            f"{len(data.split())} words"
        )

    def validate(self, data: Any) -> bool:
        """Validate if data is text."""
        if not isinstance(data, str):
            raise TypeError("Text data must be a string")
        return True


class LogProcessor(DataProcessor):
    """Processor for log data."""

    def process(self, data: Any) -> str:
        level, message = data.split(":", 1)
        level = level.strip()
        message = message.strip()

        if level == "ERROR":
            return f"[ALERT] ERROR level detected: {message}"
        return f"[{level}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            raise TypeError("Log data must be a string")

        if not any(level in data for level in ["ERROR", "INFO", "WARNING"]):
            raise ValueError("Invalid log level")

        return True

    def format_output(self, result: str) -> str:
        return f"LOG >> {result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    numprocess = NumericProcessor()
    data1 = [1, 2, 3, 4, 5]
    print(f"Processing data: {data1}")
    try:
        numprocess.validate(data1)
    except (TypeError, ValueError) as e:
        print(e)
    else:
        print("Validation: Numeric data verified")
    print(f"Output: {numprocess.process(data1)}")

    print("\nInitializing Text Processor...")
    textprocess = TextProcessor()
    data2 = "Hello Nexus World"
    print(f"Processing data: {data2}")
    try:
        textprocess.validate(data2)
    except TypeError as e:
        print(e)
    else:
        print("Validation: Text data verified")
    print(f"Output: {textprocess.process(data2)}")

    print("\nInitializing Log Processor...")
    logprocess = LogProcessor()
    data3 = "ERROR: Connection timeout"
    print(f"Processing data: {data3}")
    try:
        logprocess.validate(data3)
    except (TypeError, ValueError) as e:
        print(e)
    else:
        print("Validation: Log entry verified")
    print(f"Output: {logprocess.process(data3)}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    listprocess = [numprocess, textprocess, logprocess]
    listdata = [[1, 2, 3], "Hello World", " INFO: System ready"]
    i = 1
    for processor, data in zip(listprocess, listdata):
        print(f"Result {i}: {processor.process(data)}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")
