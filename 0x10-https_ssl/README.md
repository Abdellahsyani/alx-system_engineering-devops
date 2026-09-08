# 0x10. HTTPS SSL

Serving the stack over HTTPS: inspecting DNS records for the domain and its
subdomains, terminating TLS at the HAProxy load balancer, and forcing every
HTTP request to be redirected to HTTPS.

## Key files

| File | What it does |
| --- | --- |
| `0-world_wide_web` | Uses `dig` to report the record type and target of `www`, `lb-01`, `web-01` and `web-02`; with a second argument it queries just that subdomain |
| `1-haproxy_ssl_termination` | HAProxy config binding `*:443` with the concatenated certificate + key, terminating TLS and forwarding plain HTTP to the backends |
| `100-redirect_http_to_https` | Same config plus a `redirect scheme https code 301` rule on the HTTP frontend |

## Usage

```bash
./0-world_wide_web myabdo.tech
./0-world_wide_web myabdo.tech web-02
sudo cp 1-haproxy_ssl_termination /etc/haproxy/haproxy.cfg
sudo service haproxy restart
curl -sI https://www.myabdo.tech
```

## Architectural notes

TLS terminates at the load balancer: certificates live only there (obtained via
certbot in the task), and traffic between the balancer and the web servers is
unencrypted inside the private network. The `ssl-default-bind-*` settings pin a
Mozilla "intermediate" cipher suite and a TLS 1.2 minimum.
