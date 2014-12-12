#!/bin/bash
echo "Content-type: text/html"

   
./head.cgi


echo "<div id="search" align="left">"
echo "<div align=left> Guardster FREE webproxy</div>"


echo "<p>"
echo "<form method='post' action='http://tproxy.guardster.com/proxy.php' target="new">"
echo "<input type='text' name='URL' value='http://' id="searchbox">"
echo "<input type='submit' id="submit1" value='surf anonymously' style=''><br>"

	echo "<p>Options:<br>"
	echo "<input type='checkbox' name='cookies' >No Cookies - "
	echo "<input type='checkbox' name='javascript'  CHECKED>No Scripts - "
	echo "<input type='checkbox' name='images' >No Images - "
	echo "<input type='checkbox' name='referrer' CHECKED>Hide Referrer<br>"
	echo "<input type='checkbox' name='agent' >Hide User Agent -"
	echo "<input type='checkbox' name='title' >Hide Title -"
	echo "<input type='checkbox' name='header' >Hide Header"
echo "</form>"
echo "</p>"	

echo " </div> "	

 ./footer.cgi
