# images

Rendered diagrams for the [0x09. Web infrastructure design](../README.md)
tasks. Each task file in the parent directory links to the same diagram hosted
online; these PNGs are the local copies so the designs stay readable if the
external links rot.

## Key files

| File | Diagram |
| --- | --- |
| `0-simple_web_stack.png` | Single-server LAMP-style stack: DNS → server running Nginx, the application server, the code base and MySQL |
| `1-distributed_web_infrastructure.png` | HAProxy load balancer in front of two application servers with a MySQL primary/replica pair |
| `2-secured_and_monitored_web_infrastructure.png` | The distributed design hardened with firewalls, HTTPS termination and monitoring agents |

## Notes

Images only — no code. Reference them from Markdown with a relative path, e.g.
`![Simple web stack](images/0-simple_web_stack.png)`.
