# 0x17. Web stack debugging #3

A WordPress site returns HTTP 500. `strace` on the Apache worker shows a failed
`open()` on a misspelled PHP file, and the fix is delivered as a Puppet
manifest rather than a manual edit.

## Key files

| File | What it does |
| --- | --- |
| `0-strace_is_your_friend.pp` | Puppet `exec` that runs `sed -i 's/phpp/php/g' wp-settings.php` in `/var/www/html`, correcting the typo that broke the include |

## Usage

```bash
strace -p "$(pgrep -f apache2 | head -1)"   # observe the failing syscall
sudo puppet apply 0-strace_is_your_friend.pp
curl -sI localhost | head -1                # HTTP/1.1 200 OK
```

## Notes

`strace` surfaces the failing syscall (`open("...phpp") = -1 ENOENT`) when the
application logs are unhelpful — the general technique this task teaches. The
`exec` sets `cwd` and an explicit `path` because Puppet runs commands with a
minimal environment.
