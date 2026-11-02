*This project has been created as part of the 42 curriculum by nweber--.*

# Call Me Maybe

## Description

Call Me Maybe is a Python function-calling tool. It takes natural-language
prompts and a JSON list of available function definitions, then produces one
structured function call per prompt. It selects a function and extracts its
arguments; it does not execute the selected function.

The project uses the `Qwen/Qwen3-0.6B` model through the provided `llm_sdk`
wrapper. Pydantic models validate prompt and function-definition data. The
current argument decoder supports `string`, `number`, `integer`, and `boolean`
parameter types.

## Instructions

### Requirements

- Python 3.10 or later
- [uv](https://docs.astral.sh/uv/)
- Network access on the first run to download the model and tokenizer, unless
  they are already cached

The SDK included in this repository uses PyTorch, Transformers, and
Hugging Face Hub to load the model. **This conflicts with the subject's
additional requirement forbidding PyTorch and Hugging Face packages.** The
current implementation therefore does not meet that requirement.

### Installation

From the repository root, synchronize the project environment:

```bash
make install
```

### Execution

Run with the default input, function definitions, and output paths:

```bash
make run
```

Specify custom files with the command-line options:

```bash
uv run python -m src \
  --functions_definition path/to/functions_definition.json \
  --input path/to/prompts.json \
  --output path/to/function_calls.json
```

The Makefile also provides:

```bash
make debug        # Run the program under pdb
make clean        # Remove Python and test/type-check cache directories
make lint         # Run flake8 and the required mypy checks
make lint-strict  # Run flake8 and mypy --strict
```

The lint targets obtain `flake8` and `mypy` through `uv run --with`, so these
tools do not need to be added to the project's runtime dependencies.

The defaults are:

- Function definitions: `data/input/functions_definition.json`
- Prompts: `data/input/function_calling_tests.json`
- Output: `data/output/function_calls.json`

Input files must contain JSON arrays. The prompt file contains objects with a
non-empty `prompt` string. The definitions file contains objects with a
function `name`, `description`, `parameters`, and `returns`. Supported
parameter type names are `string`, `number`, `integer`, and `boolean`.

An empty prompt array (`[]`) is valid and produces an empty output array
without loading the model. If prompts are supplied but the function-definition
array is empty, the program prints an error and exits with a non-zero status.
Missing files, malformed JSON, and invalid input structures are reported on
standard error.

## Example

Given a prompt:

```json
[
  {
    "prompt": "What is the sum of 2 and 3?"
  }
]
```

And a matching function definition for `fn_add_numbers`, the expected output
shape is:

```json
[
  {
    "prompt": "What is the sum of 2 and 3?",
    "name": "fn_add_numbers",
    "parameters": {
      "a": 2.0,
      "b": 3.0
    }
  }
]
```

The generated values depend on model inference; this example illustrates the
required output format and is not a benchmark result.

## Algorithm

1. The input loader parses both JSON files and validates each prompt and
   function definition with Pydantic.
2. The context builder formats the function descriptions and parameter schemas
   into the model prompt.
3. Function selection tokenizes each available function name. The selector is
   intended to narrow the candidates to names matching the generated prefix
   and use the model's next-token logits to choose among their next tokens.
   In the current implementation, the candidate-token list is not cleared
   between iterations, so this constraint is not reliably enforced yet.
4. For each parameter, the argument selector generates a value token by token.
   It reads token IDs from the model vocabulary and uses type-specific status
   checks to reject candidates that do not match the expected primitive value
   format. String candidates are parsed as JSON strings; numeric candidates
   are checked for numeric characters and separators; boolean candidates are
   checked against `true` and `false`.
5. The selected function and generated parameters are serialized to the output
   JSON file.

This is the project's constrained-decoding approach: restrict candidate
tokens according to the expected function name or argument type rather than
relying only on the model to produce a complete, well-formed function call.
The argument decoders apply type checks, but the current function-selector
limitation means the implementation has not been demonstrated to guarantee
full schema-valid output for every possible input.

## Design Decisions

- **Pydantic data models:** Validate prompt and function-definition objects
  before inference.
- **Separate pipeline stages:** `parser.py`, `context_builder.py`, and
  `selector.py` separate input validation, prompt construction, function
  selection, and argument generation.
- **Use the provided SDK:** The wrapper supplies model tokenization, decoding,
  logits, and vocabulary access. It loads Qwen3-0.6B by default.
- **JSON output:** Each result contains exactly the original prompt, selected
  function name, and a parameters object.
- **Empty-input behavior:** An empty prompt list is handled without
  initializing the model, avoiding unnecessary model loading.

## Performance and Reliability

The subject sets targets of at least 90% function/argument accuracy, 100%
valid JSON, and under five minutes for the supplied prompts on standard
hardware. These are targets, **not measured results**: no accuracy benchmark
or end-to-end timing with Qwen3-0.6B is currently documented.

Input JSON and Pydantic validation errors are reported clearly. Empty prompt
arrays are supported. Model inference still depends on the SDK, model files,
available resources, and the behavior of the constrained decoders.

Known limitations:

- The current function-selector implementation needs further validation for
  prefix filtering and overlapping function names.
- Numeric and boolean decoders have not been comprehensively tested against
  boundary cases such as negative values, decimals, and tokenization
  variations.
- The project has no committed automated test suite.
- The current PyTorch and Hugging Face dependencies conflict with the
  subject's prohibition on those packages.

## Challenges

- **Structured output from a small model:** The decoder checks candidate
  tokens against the expected primitive type instead of accepting arbitrary
  generated prose.
- **Variable tokenization:** Function names and JSON values are represented by
  model-specific token IDs, so decoding must account for the model tokenizer
  rather than assuming one token per character.
- **Malformed and empty input:** The loader validates JSON shape and reports
  missing or invalid input files. Empty prompt lists are treated as a valid
  no-work case.
- **Reliability evidence:** Passing parser and empty-input checks does not
  establish inference accuracy; real-model evaluation remains necessary.

## Testing Strategy

The project should be tested at both the input-validation and inference
boundaries:

- Valid prompts and function definitions
- Empty arrays (`[]`), missing files, malformed JSON, and wrong top-level
  JSON types
- Missing or extra fields and unsupported parameter types
- Empty strings, special characters, large and negative numbers, and boolean
  values
- Ambiguous prompts and functions with overlapping names
- Output JSON syntax, exact keys, parameter names, and value types
- Accuracy and runtime measured with the required model

Targeted checks have been run during development for syntax, input errors, and
empty-array handling. These checks are not a substitute for a maintained
automated test suite or end-to-end evaluation with Qwen3-0.6B.

## Resources

- [42 subject: Call Me Maybe](./subject.md)
- [Qwen3-0.6B model card](https://huggingface.co/Qwen/Qwen3-0.6B)
- [Hugging Face Transformers documentation](https://huggingface.co/docs/transformers/)
- [Python `json` documentation](https://docs.python.org/3/library/json.html)
- [Pydantic documentation](https://docs.pydantic.dev/)
- [uv documentation](https://docs.astral.sh/uv/)

### Use of AI

AI assistance was used during development to review code behavior, identify
edge cases, suggest and validate changes to input/error handling and
constrained decoding, and prepare this README.
