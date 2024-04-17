# Evaluating the robustness of our web server configuration with Nginx under stress testing

# Adjusting the request handling capacity by modifying Nginx settings
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

# Reloading Nginx to apply the configuration changes
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
