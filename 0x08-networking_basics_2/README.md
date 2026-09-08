# 0x08. Networking basics #1

Scripts about `localhost`, the `/etc/hosts` resolution file, listing the
machine's IPv4 addresses, and listening on a local port.

## Key files

| File | What it does |
| --- | --- |
| `0-change_your_home_IP` | Rewrites `/etc/hosts` so `localhost` resolves to `127.0.0.2` and `facebook.com` to `8.8.8.8`, preserving all other entries |
| `1-show_attached_IPs` | Prints every active IPv4 address on the machine (`ip -4 addr show`) |
| `100-port_listening_on_localhost` | Listens on port 98 with `nc`, then connects to it with `telnet` |
| `.echo.swp` | Leftover Vim swap file (not part of the tasks) |

## Usage

```bash
sudo ./0-change_your_home_IP   # modifies /etc/hosts
./1-show_attached_IPs
sudo ./100-port_listening_on_localhost
```

## Notes

`0-change_your_home_IP` overwrites `/etc/hosts` — back it up first. It builds
the new file in the working directory, filters out the old `localhost` and
`facebook.com` lines, then copies it into place, so the change is idempotent.
