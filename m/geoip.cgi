#!/bin/bash

POST=$(</dev/stdin)

./head.cgi




	FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`

	# test if any parameters were passed

         if [[ -z "$FOLDER4" ]]
    then
echo > /dev/null
    else
              city=`geoiplookup -f /usr/share/GeoIP/GeoLiteCity.dat "$FOLDER4" | grep City | cut -d: -f2`
              country=`geoiplookup "$FOLDER4" | grep Country | cut -d: -f 2`
              asn=`geoiplookup "$FOLDER4" | grep ASN | cut -d: -f 2`
 echo "<div id="text" align="center"><p>Geolocation for $FOLDER4:</p></div>"
	echo "<div id="block" align="left"><pre>"
echo -e "Country: <strong><a style="color:#fff">$country</a></strong> \nCity: <strong><a style="color:#fff">$city</a></strong> \nASN: <strong><a style="color:#fff">$asn</a></strong>"
	echo "</div>"	             
              
fi	  
echo " </div> "	

### SEARCH BLOCK ###	
echo "<div class="search_block">"	

####  SEARCH FORMS ###
echo "<div class="left">"

	echo "<div align=left> Please enter IP or Hostname!</div>"
	echo "<form method=POST>"

	echo "<p><input id="searchbox" type=text placeholder="domain.tld" name=folder4 >"
	echo "<input id="submit" value="geoip" type=submit></p>"

echo "</form>"
echo " </div> "	

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "

./footer.cgi
