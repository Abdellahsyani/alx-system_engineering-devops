# review_shell

Scratch directory of shell exercises written during a review session. These are
practice snippets rather than graded project tasks — they revisit the material
from [0x00. Shell, basics](../0x00-shell_basics/README.md) and
[0x02. Shell, I/O redirections and filters](../0x02-shell_redirections/README.md).

## Key files

| File | What it does |
| --- | --- |
| `ex_1` | Moves to the parent directory and to `/boot`, listing the contents of each in long format |
| `ex_2` | Inspects `/tmp` and prints whether the entry `iamafile` is a file or a directory, using `awk` on the permission column |
| `ex_3` | Creates a symbolic link named `fil` in the parent directory pointing at `ex_3` |

## Usage

```bash
chmod +x ex_1
./ex_1
```

## Notes

`ex_3` is what created the dangling `fil` symlink at the repository root.
Nothing here is referenced by the numbered project directories, so these files
can be run — or removed — independently.
