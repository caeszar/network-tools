#!/bin/bash
echo "Content-type: text/html"

./head.cgi
echo "<div id="code_show" align="left">"
#echo "<pre class="prettyprint"</pre>"

cat yesterday-log.html
echo "<div align=center><h1> ALL LOGS RAPORT </h1></div>"
cat all-logs-report.html

echo "</div>" 

### FOOTER ###
./footer.cgi
