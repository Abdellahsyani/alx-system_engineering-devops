# 0x0F. Load balancer

Scaling the web stack horizontally: duplicating the web server, adding a
custom `X-Served-By` header so the responding host can be identified, and
putting an HAProxy load balancer in front of both servers.

## Key files

| File | What it does |
| --- | --- |
| `0-custom_http_response_header` | Idempotently installs Nginx and adds the `X-Served-By: $hostname` response header; used to provision `web-01` and `web-02` identically |
| `1-install_load_balancer` | Installs HAProxy, backs up the stock `haproxy.cfg`, and writes a frontend on `*:80` forwarding to a round-robin backend of the two web servers |
| `2-puppet_custom_http_response_header.pp` | The custom-header setup as a Puppet manifest |

## Usage

```bash
sudo ./0-custom_http_response_header          # run on each web server
sudo ./1-install_load_balancer                # run on the load balancer
curl -sI lb-01.myabdo.tech | grep X-Served-By # alternates between web-01/web-02
```

## Architectural notes

HAProxy runs in HTTP mode with `balance roundrobin`, so requests alternate
between the two backends; `check` enables active health checks, and an
unhealthy backend is removed from rotation automatically. Both scripts define
an `install()` helper that skips packages already present, making them safe to
re-run.
