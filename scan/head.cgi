#!/bin/bash
echo ""

##  HEADER MENU html

cat head.html
 ./body.cgi
 ## LEFT MENU on page ##
 	      remote_host=`./remote_host.pl | cut -d" " -f6`	  
              city=`geoiplookup -f /usr/share/GeoIP/GeoLiteCity.dat $REMOTE_ADDR | grep City | cut -d: -f2`
              country=`geoiplookup $REMOTE_ADDR | grep Country | cut -d: -f 2`
              asn=`geoiplookup $REMOTE_ADDR | grep ASN | cut -d: -f 2`
echo "<div align="right" style="color:#067D98"><normal> HOST: <a style="color:#AE0C32">$remote_host</a>  LOCATION:  <a style="color:#AE0C32">$country</a> City: <a style="color:#AE0C32">$city</a> ASN: <a style="color:#AE0C32">$asn</a> </normal></div>" 

echo "<div class="container"><h1><a href="/"><i class="icon-arrow-left fg-darker smaller"></i></a>  Go to  <small class="on-left"> your IP:<a href="http://$REMOTE_ADDR" target="_blank" > $REMOTE_ADDR</small></h1>"

echo "<div class="grid"><div class="row"><div class="span3">"

	echo "<nav>"
		echo " <ul class="side-menu">"
			echo "<li><a href="../">HOME</a></li>"

			echo "<li><a href="../dns.cgi">DNS Records</a></li>"
			echo "<li><a href="../net.cgi">Net Tools</a></li>"
			echo "<li><a href="../scan.cgi">Scan Tools</a></li>"
			echo "<li><a href="../url.cgi">Tiny URL</a></li>"
			echo "<li><a href="../geoip.cgi">IP Location</a></li>"
			echo "<li><a href="../ipcalc.cgi">IP Calc</a></li>"
			echo "<li><a href="../pass.cgi">Password Gen</a></li>" 
			echo "<li><a href="../headers.cgi">HTTP Headers</a></li>"                                    
		echo " </ul>"
	echo "</nav>"
echo " </div>"
