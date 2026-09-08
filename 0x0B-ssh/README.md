# 0x0B. SSH

Connecting to remote servers with key-based authentication, generating key
pairs, and configuring the SSH client — manually and through Puppet.

## Key files

| File | What it does |
| --- | --- |
| `0-use_a_private_key` | Connects to the task server as `ubuntu` using the private key `~/.ssh/school` |
| `1-create_ssh_key_pair` | Generates an RSA key pair named `school`, 4096 bits, passphrase `betty` |
| `2-ssh_config` | Client config (`ssh_config`) that disables password authentication and points at the `school` identity file |
| `100-puppet_ssh_config.pp` | Same client configuration expressed as Puppet `file_line` resources |

## Usage

```bash
./1-create_ssh_key_pair            # produces ./school and ./school.pub
./0-use_a_private_key              # ssh -i ~/.ssh/school ubuntu@<server>
puppet apply 100-puppet_ssh_config.pp
```

## Notes

`100-puppet_ssh_config.pp` requires the `stdlib` module (`puppet module install
puppetlabs-stdlib`) for `file_line`, which edits `/etc/ssh/ssh_config`
in place rather than templating the whole file. Private keys are never
committed — only the client-side configuration is.
