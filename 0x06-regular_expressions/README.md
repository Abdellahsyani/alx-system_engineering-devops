# 0x06. Regular expressions

Ruby one-liners (Oniguruma regex engine) that each take a string as `ARGV[0]`,
scan it with a regular expression and print the concatenated matches.

## Key files

| File | Pattern | Matches |
| --- | --- | --- |
| `0-simply_match_school.rb` | `/School/` | The literal word `School` |
| `1-repetition_token_0.rb` | `/hbt{2,5}n/` | `hb` + 2 to 5 `t` + `n` |
| `2-repetition_token_1.rb` | `/hb?tn/` | Optional `b` |
| `3-repetition_token_2.rb` | `/hbt+n/` | One or more `t` |
| `4-repetition_token_3.rb` | `/hbt*n/` | Zero or more `t` |
| `5-beginning_and_end.rb` | `/^h.n$/` | Whole string: `h`, any char, `n` |
| `6-phone_number.rb` | `/^\d{10}$/` | Exactly 10 digits |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | `/[A-Z]/` | Every uppercase letter |

## Usage

```bash
chmod +x 0-simply_match_school.rb
./0-simply_match_school.rb "Best School"   # => School
```

## Notes

`String#scan` returns every match, and `join` glues them together, so scripts
print an empty line when nothing matches rather than failing. Requires `ruby`
on the `PATH`.
