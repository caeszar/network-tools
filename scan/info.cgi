#!/bin/bash
echo "Content-type: text/html"
echo ""
   
./head.cgi

echo " <div class="span9"> <p class="description">"

 ## Fereastra ###     
   echo " </pre><div class="window"><div class="caption"><span class="icon icon-windows"></span><div class="title">Server Basic Info</div><button class="btn-min"></button><button class="btn-max"></button><button class="btn-close"></button></div>"
   
   echo " <div class="content">"
   echo "<pre class="prettyprint linenums no-phone" style="margin-top: 15px;">  "    

echo "  <div id="code2" align="left">  "

echo "<h1>General system information for host $(hostname -f)</h1>"
echo "<h1>Info</h1>"
echo "$(uname -a)"
echo "$(cat /proc/version)"

echo "<h1>Uptime</h1>"
echo "$(uptime)"
echo "Memory Info"
echo "$(free -m)"
echo "<h1>Disk Info:</h1>"
echo "$(df -h)"
echo "<h1>Logged in user</h1>"
echo "$(w)"

echo "<h1>Mounts</h1>"
echo "$(mount)"

#echo "<h1>Apache Log</h1>"
#echo "$(tail /var/log/apache2/tools.tecmint.com-access.log)"

echo "<h1>Open Connections</h1>"
echo "$(netstat -ad)"
echo "$(lsof -i)"

echo "<h1>Listen Connections</h1>"
echo "$(netstat -tulpn)"

echo "<h1>Top Process</h1>"
echo "$(ps -auxf | sort -nr -k 4 | head -10)"
echo "$(ps -auxf | sort -nr -k 3 | head -10)"

echo "<h1>Network settings</h1>"
echo "$(/sbin/ifconfig -a)"

echo "</div>"
echo "</div>"

./footer.cgi
