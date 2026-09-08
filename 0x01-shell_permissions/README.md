# 0x01. Shell, permissions

Scripts about Unix identity (users and groups) and file permission management
with `chmod`, `chown` and `chgrp`. Each file is a one-command Bash script.

## Key files

| File | What it does |
| --- | --- |
| `0-iam_betty` | Switches the current user to `betty` (`su betty`) |
| `1-who_am_i` | Prints the effective username (`id -un`) |
| `2-groups` | Prints all groups the current user belongs to |
| `3-new_owner` | Makes `betty` the owner of `hello` |
| `4-empty` | Creates the empty file `hello` |
| `5-execute` | Adds execute permission for the owner of `hello` |
| `6-multiple_permissions` | Adds execute+read for owner and group |
| `7-everybody` | Adds execute permission for owner, group and others |
| `8-James_Bond` | Sets permissions to `007` (no owner/group rights) |
| `9-John_Doe` | Sets permissions to `753` |
| `10-mirror_permissions` | Copies `olleh`'s mode onto `hello` (`--reference`) |
| `11-directories_permissions` | Recursively adds `+X` (execute on directories only) |
| `12-directory_permissions` | Creates `my_dir` with mode `751` |
| `13-change_group` | Changes the group of `hello` to `school` |
| `100-change_owner_and_group` | Sets owner `vincent` and group `staff` on everything in the cwd |
| `101-symbolic_link_permissions` | Changes owner/group of the symlink itself (`chown -h`) |
| `102-if_only` | Changes owner to `betty` only if currently owned by `guillaume` |
| `103-Star_Wars` | Streams the ASCII-art Star Wars over telnet |

## Usage

```bash
chmod +x 5-execute
./5-execute
```

## Notes

Ownership changes (`chown`, `chgrp`) require root or the appropriate
capability; run them under `sudo` in a sandbox. `11-directories_permissions`
uses the capital `+X` flag so regular files are left untouched.
