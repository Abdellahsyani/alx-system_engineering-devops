# 0x09. Web infrastructure design

Design-only project: each task is a whiteboard diagram of a web stack, plus the
reasoning behind it (single points of failure, security, monitoring). Each task
file holds the link to the published diagram; the rendered PNGs are stored in
`images/`.

## Key files

| File | Design |
| --- | --- |
| `0-simple_web_stack` | One server hosting DNS `www` record, Nginx, an application server, the application code and a MySQL database |
| `1-distributed_web_infrastructure` | Three servers: an HAProxy load balancer in round-robin, two application servers, and a MySQL primary/replica pair |
| `2-secured_and_monitored_web_infrastructure` | The distributed stack plus three firewalls, an SSL certificate terminating HTTPS, and three monitoring clients |
| `images/` | PNG exports of the three diagrams |

## Architectural notes

- **Simple stack**: every component shares one machine, so it is a single point
  of failure, cannot be maintained without downtime, and cannot scale
  horizontally.
- **Distributed stack**: the load balancer removes the app-server SPOF, and the
  primary/replica database splits writes (primary) from reads (replicas); the
  load balancer itself is still a SPOF and traffic is plain HTTP.
- **Secured/monitored stack**: firewalls restrict traffic to the ports each
  role needs, SSL terminating at the load balancer leaves internal traffic
  unencrypted, and a single writable database node still limits write capacity.
