#!/bin/bash
echo ""

##  HEADER MENU html

#cat head.html
 ./body.cgi
 
## Declare IP Variables ##
remote_host=`./remote_host.pl | cut -d" " -f6`	  
city=`geoiplookup -f /usr/share/GeoIP/GeoLiteCity.dat $REMOTE_ADDR | grep City | cut -d: -f2`
country=`geoiplookup $REMOTE_ADDR | grep Country | cut -d: -f 2`
asn=`geoiplookup $REMOTE_ADDR | grep ASN | cut -d: -f 2`

## SHOW IP VAR ##
echo "<div id="ip" align="right" style="color:#067D98"><normal> HOST: <a style="color:#AE0C32">$remote_host</a>  LOCATION:  <a style="color:#AE0C32">$country</a> City: <a style="color:#AE0C32">$city</a> ASN: <a style="color:#AE0C32">$asn</a> </normal></div>" 


### GOOGLE ADS TOP ###
echo "<div align="center">"
cat << EOF

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Tools_Top_720x90_Ad -->
<ins class="adsbygoogle"
     style="display:inline-block;width:720px;height:90px"
     data-ad-client="ca-pub-2601749019656699"
     data-ad-slot="3790603779"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

EOF
echo "</div>"
## END GOOGLE ADS ###

## LEFT IP Address with GO TO##
echo "<div id="ip1"><h1><a href="/"><i class="icon-arrow-left fg-darker smaller"></i></a>  Go to  <small class="on-left"> your IP:<a href="http://$REMOTE_ADDR" target="_blank" > $REMOTE_ADDR</small></h1>"

## MENU LEFT FLOAT ##
echo "<div class="grid"><div class="row"><div class="span3">"

	echo "<nav>"
		echo " <ul class="side-menu">"

			echo "<li><a href="/">DNS Tools</a></li>"                              
			echo "<li><a href="dns.cgi">DNS Records</a></li>"
			echo "<li><a href="net.cgi">Net Tools</a></li>"
			echo "<li><a href="mail.cgi">Mail Tools</a></li>"
			echo "<li><a href="scan.cgi">Scan Tools</a></li>"
			echo "<li><a href="headers.cgi">HTTP Headers</a></li>" 
			echo "<li><a href="geoip.cgi">IP Location</a></li>"	
			echo "<li><a href="ipcalc.cgi">IP Calc</a></li>"			
			echo "<li><a href="url.cgi">Tiny URL</a></li>"
			echo "<li><a href="pass.cgi">Password Gen</a></li>" 

		echo " </ul>"
	echo "</nav>"
echo " </div>"
## END MENU LEFT ##
