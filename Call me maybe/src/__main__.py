import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Test the local language model.")
    parser.add_argument("prompt", nargs="?", help="Prompt sent to the model.")
    parser.add_argument("--model", default="Qwen/Qwen3-0.6B")
    parser.add_argument("--device", help="Inference device, for example cpu, cuda, or mps.")
    parser.add_argument("--max-new-tokens", type=int, default=128)
    args = parser.parse_args()

    prompt = args.prompt if args.prompt is not None else input("Prompt: ")
    if not prompt.strip():
        parser.error("the prompt must not be empty")
    if args.max_new_tokens < 1:
        parser.error("--max-new-tokens must be greater than zero")

    from llm_sdk.llm_sdk import Small_LLM_Model

    model = Small_LLM_Model(args.model, device=args.device)
    input_ids = model.encode(prompt).tolist()[0]
    generated_ids: list[int] = []

    for _ in range(args.max_new_tokens):
        logits = model.get_logits_from_input_ids(input_ids)
        next_token_id = max(range(len(logits)), key=logits.__getitem__)
        input_ids.append(next_token_id)
        generated_ids.append(next_token_id)
        if not model.decode([next_token_id]):
            break

    print(model.decode(generated_ids))


if __name__ == "__main__":
    main()