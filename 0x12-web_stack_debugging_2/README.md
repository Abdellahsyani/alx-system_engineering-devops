# 0x12. Web stack debugging #2

Applying the principle of least privilege: run a command as another user, then
make Nginx run as the unprivileged `nginx` user on port 8080 instead of as root
on port 80.

## Key files

| File | What it does |
| --- | --- |
| `0-iamsomeoneelse` | Runs `whoami` as the user passed in `$1` (`su -s /bin/bash "$1" -c whoami`) |
| `1-run_nginx_as_nginx` | Switches the default site to port 8080, stops the conflicting Apache, relaxes `nginx.conf` permissions and starts Nginx as the `nginx` user |

## Usage

```bash
./0-iamsomeoneelse www-data
sudo ./1-run_nginx_as_nginx
curl -sI 0:8080 | head -1
ps aux | grep nginx        # master process owned by nginx, not root
```

## Notes

A non-root process cannot bind ports below 1024, which is why the site is moved
to 8080. `pkill apache2` is required because Apache already holds port 80 in
the exercise container, and `chmod 644 /etc/nginx/nginx.conf` lets the `nginx`
user read its own configuration.
