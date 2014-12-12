#!/bin/bash
echo "Content-type: text/html"
echo ""

POST=$(</dev/stdin)

cat head_headers.html   
./head.cgi

### SEARCH BLOCK ###	
echo "<div class="search_block">"	
####  SEARCH FORMS ###
echo "<div class="left">"
echo " <div class="span9"> <p class="description">"
                                
echo "<div align=left> Please enter domain name !</div>"
	
echo "<div class="container" style="padding: -0px 0px">"

### GOOGLE ADS RIGHT ###
cat advertise_left.html
### ENG GOOGLE ADS RIGHT


echo " <div class="grid fluid">"
echo "<div class="row"> "

	echo "<form method=post>"
	echo "<p><input id="searchbox" type=text placeholder="domain.tld" name=folder4 >"
	echo "<input id="submit" value="Headers" type=submit></p>"		
	echo "</form>"
	
echo " </div> "
echo " </div></div>"
      
## Fereastra ###     
echo " </pre><div class="window"><div class="caption"><span class="icon icon-windows"></span><div class="title">Window Result</div><button class="btn-min"></button><button class="btn-max"></button><button class="btn-close"></button></div>"
   
echo " <div class="content">"
echo "<pre class="prettyprint linenums no-phone" style="margin-top: 15px""    
echo "  <div id="code2" align="left">  "


	FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
	# test if any parameters were passed
	
echo "Output of HTTP headers for $FOLDER4:<pre><div align="left">"
echo "-----------------------------------------------------------------------------"
	if [[ -z "$FOLDER4" ]]
    then
echo "Enter domain name to get HTTP headers:"
    else
		curl -I "$FOLDER4" 2> /dev/null
	fi	  	                
echo "-----------------------------------------------------------------------------"
echo "</pre>"	

echo "</pre>"
echo "</div>"
echo "</div>"
echo "</div>"
echo "</div>"

./footer.cgi
