# executing a command
exec { 'increase ULIMIT':
  command => "sed -i 's/15/1024/g' nginx && service nginx restart",
  cwd     => '/etc/default/',
  path    => ['/usr/bin', '/bin']
}
