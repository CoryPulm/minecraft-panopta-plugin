This is a plugin for Panopta's on server monitoring agent that reports back to their services to keep track of what your Minecraft server is doing.

You can sign up for Panopta [here](http://www.panopta.com/) and download the monitoring agent [here](http://answers.panopta.com/how-do-i-install-and-configure-a-panopta-monitoring-agent-v-2/)

Requirements:
mcstatus
Python 2.7


Just throw the following into your panopta.cfg located at /etc/panopta-agent/panopta_agent.cfg and place the server name and port in the fields:
[minecraft]
minecraft_server: 
minecraft_port:
