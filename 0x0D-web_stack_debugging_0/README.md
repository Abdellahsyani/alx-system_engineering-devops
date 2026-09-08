# 0x0D. Web stack debugging #0

First debugging exercise: a container runs Apache but no page is served. The
fix is to find *why* nothing answers on port 80 and to write the shortest
script that makes `curl` succeed.

## Key files

| File | What it does |
| --- | --- |
| `0-give_me_a_page` | Starts the Apache service and prints its status, so `curl localhost` returns the holberton page |

## Usage

```bash
sudo ./0-give_me_a_page
curl -s localhost
```

## Notes

Debugging method used here: confirm the symptom (`curl localhost` refused),
check whether anything listens on port 80 (`ss -lntp`), then check the service
state (`service apache2 status`) before changing anything. The service was
simply not running.
