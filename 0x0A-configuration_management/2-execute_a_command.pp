# executing a command
exec { 'killer':
  path    => ['/usr/bin', '/bin'],
  command => 'pkill killmenow',
}
