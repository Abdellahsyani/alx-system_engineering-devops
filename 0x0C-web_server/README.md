# 0x0C. Web server

Provisioning an Nginx web server on a fresh Ubuntu machine: installing it,
serving a page on port 80, adding a redirect and a custom 404 page — first with
Bash, then declaratively with Puppet.

## Key files

| File | What it does |
| --- | --- |
| `0-transfer_file` | `scp`s a file to a remote server; usage: `PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` |
| `1-install_nginx_web_server` | Installs Nginx, opens the firewall, and serves `Hello World!` on port 80 |
| `2-setup_a_domain_name` | Holds the domain name configured for the project (`myabdo.tech`) |
| `3-redirection` | Adds a `301` redirect from `/redirect_me` to a YouTube URL |
| `4-not_found_page_404` | Adds a custom 404 page returning `Ceci n'est pas une page` |
| `7-puppet_install_nginx_web_server.pp` | The whole setup as a Puppet manifest (`package`, `file`, `exec`, `service`) |
| `some_page.html`, `lkhra`, `ubuntu@18.207.112.142` | Scratch artefacts left over from manual testing |

## Usage

```bash
./0-transfer_file ./1-install_nginx_web_server 1.2.3.4 ubuntu ~/.ssh/school
sudo ./1-install_nginx_web_server
curl -sI localhost | head -1
sudo puppet apply 7-puppet_install_nginx_web_server.pp
```

## Notes

The Bash scripts back up `index.nginx-debian.html` before overwriting it and
insert the redirect with `sed -i '24i ...'` into
`/etc/nginx/sites-available/default` — a line-number-based edit that assumes
the stock Ubuntu config, so re-running them on an already-modified file can
place the directive in the wrong block. The Puppet manifest orders resources
explicitly with `require` (update → package → service).
