# 0x02. Shell, I/O redirections and filters

Scripts practising stdin/stdout redirection and the classic text-filter
toolchain: `cat`, `head`, `tail`, `cut`, `sort`, `uniq`, `grep`, `tr`, `find`,
`rev` and `paste`. Several scripts read from **stdin**, so they are meant to be
piped into.

## Key files

| File | What it does |
| --- | --- |
| `0-hello_world` | Prints `Hello, World` |
| `1-confused_smiley` | Prints an escaped smiley, exercising quoting rules |
| `2-hellofile` | Displays `/etc/passwd` |
| `3-twofiles` | Displays `/etc/passwd` then `/etc/hosts` |
| `4-lastlines` / `5-firstlines` | Last / first 10 lines of `/etc/passwd` |
| `6-third_line` | Third line of the file `iacta` |
| `7-file` | Writes `Best School` into a file with a pathological name |
| `8-cwd_state` | Saves `ls -la` output into `ls_cwd_content` |
| `9-duplicate_last_line` | Appends the last line of `iacta` to itself |
| `10-no_more_js` | Recursively deletes all `*.js` files |
| `11-directories` | Counts directories (excluding `.`) in the current tree |
| `12-newest_files` | Ten most recently modified files |
| `13-unique` | Prints only lines that appear exactly once (stdin) |
| `14-findthatword` | Lines of `/etc/passwd` containing `root` |
| `15-countthatword` | Number of lines containing `bin` |
| `16-whatsnext` | Lines containing `root` plus the 3 following lines |
| `17-hidethisword` | Lines *not* containing `bin` |
| `18-letteronly` | Lines of `sshd_config` starting with a letter |
| `19-AZ` | Replaces `A`→`Z` and `c`→`e` (stdin) |
| `20-hiago` | Removes all `c` and `C` characters (stdin) |
| `21-reverse` | Reverses each input line |
| `22-users_and_homes` | Username and home directory pairs, sorted |
| `100-empty_casks` | Names of empty files/directories in the tree |
| `101-gifs` | Sorted, extension-less names of every `.gif` in the tree |
| `102-acrostic` | Builds a word from the first letter of each input line |
| `103-the_biggest_fan` | Top 11 senders from a piped TSV log |

## Usage

Scripts that filter stdin need input piped in:

```bash
cat data.txt | ./13-unique
echo "hello" | ./21-reverse
```

## Notes

`10-no_more_js` deletes files recursively — run it only inside a disposable
directory.
