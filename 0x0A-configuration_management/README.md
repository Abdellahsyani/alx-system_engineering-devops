# 0x0A. Configuration management

First contact with Puppet: declarative manifests (`.pp`) that describe the
desired state of a machine instead of the steps to reach it. Each manifest
demonstrates one core resource type.

## Key files

| File | Resource | Desired state |
| --- | --- | --- |
| `0-create_a_file.pp` | `file` | `/tmp/school` exists, mode `0744`, owner/group `www-data`, content `I love Puppet` |
| `1-install_a_package.pp` | `package` | `flask` 2.1.0 and `werkzeug` 2.1.1 installed through the `pip3` provider |
| `2-execute_a_command.pp` | `exec` | Runs `pkill killmenow` to stop the `killmenow` process |

## Usage

```bash
puppet apply 0-create_a_file.pp
puppet-lint --no-140chars-check 0-create_a_file.pp
```

## Notes

Manifests are idempotent: applying them repeatedly converges to the same state.
`exec` is the escape hatch and is *not* idempotent by itself — production
manifests normally guard it with `onlyif`, `unless` or `creates`.
