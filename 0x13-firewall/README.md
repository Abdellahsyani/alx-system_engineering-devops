# 0x13. Firewall

Hardening a server with `ufw`: denying all inbound traffic except the ports the
web stack needs, and forwarding an alternate port to the web server.

## Key files

| File | What it does |
| --- | --- |
| `0-block_all_incoming_traffic_but` | Installs `ufw`, allows inbound `22` (SSH), `80` (HTTP) and `443` (HTTPS), sets the default policy to deny incoming / allow outgoing, then enables the firewall |
| `100-port_forwarding` | A `/etc/ufw/before.rules` copy adding a `nat` `PREROUTING` rule that redirects TCP port `8080` to port `80` |

## Usage

```bash
sudo ./0-block_all_incoming_traffic_but
sudo ufw status verbose

sudo cp 100-port_forwarding /etc/ufw/before.rules
sudo ufw reload
curl -sI 0:8080 | head -1
```

## Notes

Allow SSH **before** enabling the firewall, or the session is cut off. The
port-forwarding rule lives in `before.rules` because `ufw`'s generated rules
run after it and only cover the `filter` table — NAT rules must be declared in
the `*nat` block manually.
