cernvm-appliance-agent
======================

Appliance agent for interactive and scripted configuration and monitoring, replaces rAA.

The main application is in usr/libexec/cernvm-appliance-agent.
It contains cgi-scripts, css and other files and modules that are handled by the apache server. 
The directory usr/libexec/cernvm-appliance-agent/etc/ contains the configuration files 
that are used internally in the application and they are basically part of the code. 
The configuration files related to the server are kept separetly in etc/cernvm-appliance-agent/
while the service which is in etc/init.d/cernvm-httpd.s, 
starts an instance of the httpd with the application's configuration file is in etc/init.d
var/log/cernvm-appliance-agent is the place where error logs are kept.
