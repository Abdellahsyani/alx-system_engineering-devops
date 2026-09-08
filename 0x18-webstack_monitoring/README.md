# 0x18. Webstack monitoring

Instrumenting the web stack with Datadog so both application-level metrics
(requests per second, HTTP status codes) and host-level metrics (CPU, memory,
disk) are collected and alertable.

## Key files

| File | What it does |
| --- | --- |
| `2-setup_datadog` | Holds the ID of the Datadog dashboard created for the task, which graphs the `system.cpu.user` and `system.disk.in_use` metrics of the monitored host |

## Usage

The agent is installed on the host with the one-line installer from the Datadog
account, then the Nginx integration is enabled:

```bash
DD_API_KEY=<key> DD_SITE="datadoghq.com" bash -c \
  "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"
sudo datadog-agent status
```

## Notes

Monitoring splits into **application monitoring** (is the service behaving
correctly?) and **server monitoring** (is the machine healthy?). This directory
stores only the dashboard reference — the agent configuration lives on the
monitored servers, not in the repository, because it embeds an API key.
