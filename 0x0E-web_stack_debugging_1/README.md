# 0x0E. Web stack debugging #1

An Nginx server that does not answer on port 80. The task is to repair it, then
to do the same in as few lines of Bash as possible.

## Key files

| File | What it does |
| --- | --- |
| `0-nginx_likes_port_80` | Recreates the `sites-enabled/default` symlink to `sites-available/default` and restarts Nginx so it listens on port 80 |
| `1-debugging_made_short` | The short version: `ln -sf` plus a start, killing the stale master process |

## Usage

```bash
sudo ./0-nginx_likes_port_80
curl -sI localhost | head -1     # HTTP/1.1 200 OK
```

## Notes

The root cause is the enabled-site symlink: Nginx only reads virtual hosts from
`/etc/nginx/sites-enabled/`, so a missing or dangling link leaves it with no
server block bound to port 80. Useful checks: `nginx -t`, `ss -lntp | grep :80`
and `ls -l /etc/nginx/sites-enabled/`.
