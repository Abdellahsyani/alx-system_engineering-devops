# configure ssh with puppet
include stdlib

file_line {'ssh_config_school_identity':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school'
}
file_line {'ssh_config_no_password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no'
}
