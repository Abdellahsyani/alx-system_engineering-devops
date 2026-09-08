# 0x04. Loops, conditions and parsing

Bash scripting fundamentals: `for` / `while` / `until` loops, `if`/`elif`,
`case`, file test operators, and line-by-line parsing of `/etc/passwd`. All
scripts use `#!/usr/bin/env bash` and pass `shellcheck`.

## Key files

| File | What it does |
| --- | --- |
| `0-RSA_public_key.pub` | RSA public key used to connect to the task servers |
| `1-for_best_school` | Prints `Best School` 10 times with a `for` loop |
| `2-while_best_school` | Same output with a `while` loop |
| `3-until_best_school` | Same output with an `until` loop |
| `4-if_9_say_hi` | Prints `Hi` after the 9th iteration |
| `5-4_bad_luck_8_is_your_chance` | `if`/`elif`/`else` branching on the iteration index |
| `6-superstitious_numbers` | Counts 1→20, using `case` for special numbers |
| `7-clock` | Nested loops printing hours (0-12) and minutes |
| `8-for_ls` | Lists non-hidden entries, stripping everything before the first `-` |
| `9-to_file_or_not_to_file` | File tests (`-e`, `-s`, `-f`) on `school` |
| `10-fizzbuzz` | FizzBuzz from 1 to 100 |
| `100-read_and_cut` | Reads `/etc/passwd` and prints username, UID and home |
| `101-tell_the_story_of_passwd` | Parses `/etc/passwd` with `IFS=':'` into a sentence per user |

## Usage

```bash
chmod +x 10-fizzbuzz
./10-fizzbuzz
```

## Notes

`100-read_and_cut` and `101-tell_the_story_of_passwd` show the two parsing
idioms: piping each line to `cut`, versus splitting fields directly with
`while IFS=':' read -r ...`, which is the faster and quoting-safe form.
