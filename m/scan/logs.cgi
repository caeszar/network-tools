#!/bin/bash
echo "Content-type: text/html"

./head.cgi
echo "<div id="code_show" align="left">"
#echo "<pre class="prettyprint"</pre>"

cat log.html

echo "</div>" 

### FOOTER ###
./footer.cgi
