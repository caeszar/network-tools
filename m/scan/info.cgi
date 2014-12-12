#!/bin/bash
echo "Content-type: text/html"

   
./head.cgi

echo "<div id="code_show" align="left">"
echo "<pre class="prettyprint"</pre>"


echo "<h1>General system information for host $(hostname)</h1>"

echo "<h2>Generated on `date`</h2>"

echo "<h1>Info</h1>"

echo "Distribution: `cat /etc/issue.net`"
echo "$(uname -a)"
echo "$(cat /proc/version)"
echo " "

echo "<h2>CPU info:</h2>"
echo "`lscpu`"
echo " "

echo "<h2>Last Reboot:</h2>"
echo "`who -b` "

echo "<h1>Uptime</h1>"
echo "$(uptime)"

echo "<h2>RAM info:</h2>"
echo "$(free -h)"
echo "<h1>Disk Info:</h1>"
echo "$(df -h)"

echo "<h1>Logged in user</h1>"
echo "$(w)"

echo "<h1>Mounts</h1>"
echo "$(mount)"

echo "<h1>Traffic Info</h1>"
echo "'"
echo "`vnstat -i eth0`"
echo -e " \n"
echo "'"
echo "'"
echo "`vnstat -i tun0`"
echo "'"

echo "<h1>Last Users Logged In</h1>"

logged=`last -wF`
         while read -r line; do
echo "___________________________________________________________________________________________________________________________________"
        echo "$line"
        done <<< "$logged"
echo " "

echo "<h1>Open Connections</h1>"
echo "$(netstat -ad)"
echo "   "
echo -e "\n$(lsof -i)"

echo "<h1>Listen Connections</h1>"
echo "$(netstat -tulpn)"

echo "<h1>Top Process</h1>"

echo "$(ps -auxf | sort -nr -k 4 | head -10)"
echo "<p>$(ps -auxf | sort -nr -k 3 | head -10)</p>"

echo "<h1>Network settings</h1>"
echo "$(/sbin/ifconfig -a)"

echo "<h1>Server Services Status</h1>"

 result=`/usr/sbin/sysv-rc-conf --list`
         while read -r line; do
		 echo "______________________________________________________________________________"
        echo "$line"
        done <<< "$result"

echo "<h1>I/O </h1>"
echo "<pre>$(iostat ALL)</pre>"
echo "<pre>$(/usr/bin/vmstat)</pre>"


echo "  "
echo "<h1>All Processes:</h1>"
echo "<pre> `ps aux`</pre>"

echo " </div> "	

 

### FOOTER ###
./footer.cgi
