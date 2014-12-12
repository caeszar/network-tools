#!/bin/bash
echo "Content-type: text/html"
echo ""

POST=$(</dev/stdin)

cat head_geoip.html   
./head.cgi

### SEARCH BLOCK ###	
echo "<div class="search_block">"	

####  SEARCH FORMS ###
echo "<div class="left">"
echo " <div class="span9"> <p class="description">"
                                
echo "Enter IP or hostname !"           
echo "<div class="container" style="padding: -0px 0px">"

### GOOGLE ADS RIGHT ###
cat advertise_left.html
### ENG GOOGLE ADS RIGHT


    echo "<div class="grid fluid">"
    echo "<div class="row"> "

	echo "<form method=post>"
	echo "<p><input id="searchbox" type=text placeholder="domain.tld" name=folder4 >"
	echo "<input id="submit" value="geoip" type=submit></p>"		
	echo "</form>"
	echo " </div></div></div>"

## Fereastra ###     
   echo " </pre><div class="window"><div class="caption"><span class="icon icon-windows"></span><div class="title">Window Result</div><button class="btn-min"></button><button class="btn-max"></button><button class="btn-close"></button></div>"
   
echo " <div class="content">"
echo "<pre class="prettyprint linenums no-phone" style="margin-top: 15px""    

	echo "<div id="code2" align="right">"
	 
	# read in our parameters in form method get
  FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
	# test if any parameters were passed
echo "IP information for $FOLDER4 :<pre><div align="left">"
echo "--------------------------------------------------------------------------------"
			  
         if [[ -z "$FOLDER4" ]]
    then
        echo "Enter IP or hostname:"
    else
	city=`geoiplookup -f /usr/share/GeoIP/GeoLiteCity.dat "$FOLDER4" | grep City | cut -d: -f2`
	country=`geoiplookup "$FOLDER4" | grep Country | cut -d: -f 2`
	asn=`geoiplookup "$FOLDER4" | grep ASN | cut -d: -f 2`
              
	echo -e "Country: <a style="color:#AE0C32">$country</a> \nCity: <a style="color:#AE0C32">$city</a> \nASN: <a style="color:#AE0C32">$asn</a>"
		fi	  
echo "--------------------------------------------------------------------------------"
echo "</pre>"	
echo "</div>"

echo "</div>"
echo "</div>"
echo "</div>"

./footer.cgi
