# executing a command
exec { 'correct this typo':
  command => "sed -i 's/phpp/php/g' wp-settings.php",
  cwd     => '/var/www/html',
  path    => ['/usr/bin', '/bin']
}
