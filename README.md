# alx-system_engineering-devops

System engineering and DevOps projects from the ALX SE programme: shell
scripting, networking, web server and load balancer provisioning, configuration
management with Puppet, API consumption, monitoring, and web stack debugging.

Each directory is a self-contained project with its own README describing the
tasks, the key files and how to run them.

## Directory index

| Directory | Topic |
| --- | --- |
| [`0x00-shell_basics`](0x00-shell_basics) | Navigation, listing and file manipulation one-liners |
| [`0x01-shell_permissions`](0x01-shell_permissions) | Users, groups, `chmod` / `chown` / `chgrp` |
| [`0x02-shell_redirections`](0x02-shell_redirections) | I/O redirection and text filters |
| [`0x03-shell_variables_expansions`](0x03-shell_variables_expansions) | Init files, variables, expansions, base conversion |
| [`0x04-loops_conditions_and_parsing`](0x04-loops_conditions_and_parsing) | Loops, conditionals, `/etc/passwd` parsing |
| [`0x05-processes_and_signals`](0x05-processes_and_signals) | PIDs, signals and traps |
| [`0x06-regular_expressions`](0x06-regular_expressions) | Ruby regex one-liners |
| [`0x07-networking_basics`](0x07-networking_basics) | OSI model, TCP/UDP, listening ports, `ping` |
| [`0x08-networking_basics_2`](0x08-networking_basics_2) | `localhost`, `/etc/hosts`, local IPs, `nc` |
| [`0x09-web_infrastructure_design`](0x09-web_infrastructure_design) | Web stack designs from single server to secured/monitored |
| [`0x0A-configuration_management`](0x0A-configuration_management) | Puppet `file`, `package` and `exec` resources |
| [`0x0B-ssh`](0x0B-ssh) | Key-based authentication and SSH client configuration |
| [`0x0C-web_server`](0x0C-web_server) | Nginx installation, redirects and custom 404 |
| [`0x0D-web_stack_debugging_0`](0x0D-web_stack_debugging_0) | Apache not running |
| [`0x0E-web_stack_debugging_1`](0x0E-web_stack_debugging_1) | Nginx not listening on port 80 |
| [`0x0F-load_balancer`](0x0F-load_balancer) | HAProxy round-robin and `X-Served-By` header |
| [`0x10-https_ssl`](0x10-https_ssl) | DNS records and TLS termination at the load balancer |
| [`0x12-web_stack_debugging_2`](0x12-web_stack_debugging_2) | Running Nginx as an unprivileged user |
| [`0x13-firewall`](0x13-firewall) | `ufw` policies and port forwarding |
| [`0x14-mysql`](0x14-mysql) | MySQL setup, replication user and sample database |
| [`0x15-api`](0x15-api) | JSONPlaceholder to-do reports exported to CSV/JSON |
| [`0x16-api_advanced`](0x16-api_advanced) | Reddit API queries with pagination |
| [`0x17-web_stack_debugging_3`](0x17-web_stack_debugging_3) | `strace` to find a WordPress 500 |
| [`0x18-webstack_monitoring`](0x18-webstack_monitoring) | Datadog agent and dashboards |
| [`0x19-postmortem`](0x19-postmortem) | Incident postmortem write-up |
| [`0x1A-application_server`](0x1A-application_server) | Gunicorn behind Nginx, zero-downtime reloads |
| [`0x1B-web_stack_debugging_4`](0x1B-web_stack_debugging_4) | File-descriptor limits under load |
| [`review_shell`](review_shell) | Scratch shell exercises from a review session |

## Environment

Scripts target Ubuntu (16.04/20.04 in the task sandboxes) and are written for
Bash (`#!/usr/bin/env bash`), Python 3, Ruby or Puppet depending on the
project. Bash scripts are checked with `shellcheck`, Python with `pycodestyle`
and Puppet manifests with `puppet-lint`.
