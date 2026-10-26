

from typing import Any

from pydantic import json


def load_vocab(vocab_path: str) -> dict[str, Any]:
    with open(vocab_path, "r", encoding="utf-8") as file:
        try:
            vocab = json.load(file)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in vocabulary file.")

    if not isinstance(vocab, dict):
        raise ValueError("The vocabulary must be a JSON object.")

    return vocab


def build_inverse_vocab(vocab: dict[str, int]) -> dict[int, str]:
    inverse_vocab = {}

    for voc_key, voc_value in vocab.items():
        inverse_vocab[voc_value] = voc_key

    return inverse_vocab
