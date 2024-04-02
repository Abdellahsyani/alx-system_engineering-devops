# setup loadbalancer with HAProxy
include stdlib

package { 'nginx':
  ensure   => installed,
  name     => 'nginx',
  provider => 'apt'
}
exec { 'firewall':
  path    => ['/usr/sbin', '/usr/bin', '/bin'],
  command => "ufw allow 'Nginx HTTP'"
}
service { 'nginx':
  ensure  => running,
  name    => 'nginx',
  restart => ''
}
file_line {'custom_header':
  ensure => 'present',
  path   => 'etc/nginx/sites-available/default',
  line   => '	add_header X-Served-By ${HOSTNAME};'
}
exec { 'reload nginx':
  path    => ['/usr/sbin', '/usr/bin', '/bin'],
  command => 'nginx -s reload'
}
