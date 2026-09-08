# 0x00. Shell, basics

Introductory Bash one-liners covering navigation, listing, and basic file
manipulation. Every task is a standalone executable script whose first line is
`#!/bin/bash` and whose body is a single command.

## Key files

| File | What it does |
| --- | --- |
| `0-current_working_directory` | Prints the absolute path of the working directory (`pwd`) |
| `1-listit` | Lists the content of the current directory |
| `2-bring_me_home` | Changes the working directory to the user's home |
| `3-listfiles` | Long-format listing (`ls -l`) |
| `4-listmorefiles` | Long-format listing including hidden files |
| `5-listfilesdigitonly` | Long listing showing numeric user/group IDs |
| `6-firstdirectory` | Creates `/tmp/my_first_directory` |
| `7-movethatfile` | Moves `/tmp/betty` into `/tmp/my_first_directory` |
| `8-firstdelete` | Deletes `/tmp/my_first_directory/betty` |
| `9-firstdirdeletion` | Removes the (empty) `/tmp/my_first_directory` |
| `10-back` | Returns to the previous working directory (`cd -`) |
| `11-lists` | Lists `.`, `..` and `/boot` in long format |
| `12-file_type` | Prints the type of `/tmp/iamafile` |
| `13-symbolic_link` | Creates the symlink `__ls__` pointing to `/bin/ls` |
| `14-copy_html` | Copies newer/missing `*.html` files to the parent directory |
| `100-lets_move` | Moves files starting with an uppercase letter to `/tmp/u` |
| `101-clean_emacs` | Deletes Emacs backup files (`*~`) |
| `102-tree` | Creates the nested directories `welcome/to/school` |
| `103-commas` | Lists entries comma separated, directories suffixed with `/` |
| `school.mgc` | `file` magic definition matching data files containing `SCHOOL` |
| `ex_3` | Scratch practice script kept from the review session |

## Usage

```bash
chmod +x 0-current_working_directory
./0-current_working_directory
```

`school.mgc` is used with the `file` command:

```bash
file -C -m school.mgc      # compile the magic file
file --mime-type -m school.mgc.mgc *
```

## Notes

Scripts are intentionally minimal (one command each) — the point of the
directory is command discovery, not scripting style. Several tasks mutate the
filesystem (`100-lets_move`, `101-clean_emacs`, `8-firstdelete`); run them in a
throwaway directory.
