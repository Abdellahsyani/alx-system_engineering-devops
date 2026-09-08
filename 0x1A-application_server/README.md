# 0x1A. Application server

Putting a real application server behind Nginx: Gunicorn serves the Flask
application over local ports, and Nginx acts as reverse proxy for the dynamic
routes while still serving static content itself.

## Key files

| File | What it does |
| --- | --- |
| `2-app_server-nginx_config` | Nginx site proxying `/airbnb-onepage` to Gunicorn on `:5000`, aliasing `/hbnb_static` to `/data/web_static/current/` |
| `3-app_server-nginx_config` | Adds a regex location proxying `/airbnb-dynamic/number_odd_or_even/<n>` to `:5001` |
| `4-app_server-nginx_config` | Adds `/api/` proxied to `:5002` |
| `5-app_server-nginx_config` | Adds `/static/` served from the `web_dynamic` static directory |
| `4-reload_gunicorn_no_downtime` | `pkill -HUP gunicorn` — graceful reload with zero downtime |
| `gunicorn.service` | Upstart job running Gunicorn with 3 workers on `0.0.0.0:5003`, as `ubuntu:www-data`, logging to `/tmp/airbnb-{access,error}.log` |

## Usage

```bash
sudo cp 5-app_server-nginx_config /etc/nginx/sites-available/default
sudo nginx -t && sudo service nginx restart

gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
sudo ./4-reload_gunicorn_no_downtime
```

## Architectural notes

Nginx terminates client connections and forwards only dynamic paths to
Gunicorn, which runs the WSGI application in several worker processes. Static
files bypass Python entirely through `alias`/`try_files`. `SIGHUP` makes
Gunicorn spawn new workers with the updated code and retire the old ones once
their in-flight requests finish, which is why reloads cause no downtime.
