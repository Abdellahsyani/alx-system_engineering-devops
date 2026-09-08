# 0x03. Shell, init files, variables and expansions

Scripts about shell initialisation files, aliases, local vs. global variables,
arithmetic expansion, brace expansion and base conversion.

## Key files

| File | What it does |
| --- | --- |
| `0-alias` | Creates an alias `ls` that runs `rm *` (a lesson in alias hazards) |
| `1-hello_you` | Greets the current user via `$USER` |
| `2-path` | Appends `/action` to `PATH` |
| `3-paths` | Counts the number of entries in `PATH` |
| `4-global_variables` | Lists all environment variables (`printenv`) |
| `5-local_variables` | Lists all shell variables, locals included (`set`) |
| `6-create_local_variable` | Creates the local variable `BEST=School` |
| `7-create_global_variable` | Exports the global variable `BEST=School` |
| `8-true_knowledge` | Prints `TRUEKNOWLEDGE + 128` |
| `9-divide_and_rule` | Prints `POWER / DIVIDE` |
| `10-love_exponent_breath` | Prints `BREATH` to the power of `LOVE` |
| `11-binary_to_decimal` | Converts `$BINARY` (base 2) to decimal |
| `12-combinations` | All two-letter combinations except `oo` |
| `13-print_float` | Prints `$NUM` with two decimal places |
| `100-decimal_to_hexadecimal` | Converts `$DECIMAL` to hexadecimal |
| `101-rot13` | ROT13-encodes stdin |
| `102-odd` | Prints every other line of stdin |
| `103-water_and_stir` | Adds two base-5-encoded words and prints the result in a custom alphabet |

## Usage

Scripts that read variables expect them to be exported first, and those using
aliases or `PATH` changes must be **sourced** to affect the current shell:

```bash
export TRUEKNOWLEDGE=1207 && ./8-true_knowledge
source ./2-path && echo "$PATH"
```

## Notes

`0-alias` is deliberately destructive if the alias is later invoked; source it
only in a throwaway shell.
