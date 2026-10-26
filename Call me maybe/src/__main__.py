from src.parser import load_vocab
from llm_sdk.llm_sdk import Small_LLM_Model


def main() -> None:
    """Load and inspect the model vocabulary."""
    model = Small_LLM_Model()
    vocab_path = model.get_path_to_vocab_file()

    vocab = load_vocab(vocab_path)

    print("Type :", type(vocab))
    print("Nombre d'entrées :", len(vocab))

    for key, value in list(vocab.items())[:10]:
        print(repr(key), "->", repr(value))


if __name__ == "__main__":
    main()