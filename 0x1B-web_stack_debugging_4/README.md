# 0x1B. Web stack debugging #4

Load-testing an Nginx server with ApacheBench reveals failed requests long
before the machine runs out of CPU. Both causes are file-descriptor limits, and
both fixes are Puppet manifests.

## Key files

| File | What it does |
| --- | --- |
| `0-the_sky_is_the_limit_not.pp` | Raises Nginx's own limit by rewriting `ULIMIT="-n 15"` to `ULIMIT="-n 4096"` in `/etc/default/nginx`, then restarts the service |
| `1-user_limit.pp` | Raises the `holberton` user's `nofile` soft/hard limits in `/etc/security/limits.conf` (5 → 50000, 4 → 40000) |

## Usage

```bash
ab -c 100 -n 2000 localhost/          # reproduce: many "Failed requests"
sudo puppet apply 0-the_sky_is_the_limit_not.pp
sudo puppet apply 1-user_limit.pp
ab -c 100 -n 2000 localhost/          # zero failures
```

## Notes

`0-...` orders its two `exec` resources with `before`, so the config edit
always precedes the restart. Both manifests use `provider => shell` because the
commands rely on shell quoting. The distinction matters: `/etc/default/nginx`
caps the service, while `/etc/security/limits.conf` caps every process of a
given user — a fix for one does not cover the other.
