#!/bin/bash
echo "Content-type: text/html"
echo ""

echo "<script src="https://google-code-prettify.googlecode.com/svn/loader/run_prettify.js"></script>"
echo "<link rel="stylesheet" type="text/css" href="/m/css/style.css" />"
echo "<link rel="stylesheet" type="text/css" href="/m/css/menu.css" />"
echo "<link rel="stylesheet" type="text/css" href="/m/css/head.css" />"
echo "<link rel="stylesheet" type="text/css" href="/m/css/icons.css" />"
echo "<script src="/m/css/fb.js"></script>"
echo "<script src="/m/css/tweet.js"></script>"
echo "<script src="/m/css/googlep.js"></script>"


### SOCIAL BUTTONS FLOAT RIGHT SCRIPT ###
cat << EOF

<script type="text/javascript">
//<![CDATA[
  (function() {
    var shr = document.createElement('script');
    shr.setAttribute('data-cfasync', 'false');
    shr.src = '//dsms0mj1bbhn4.cloudfront.net/assets/pub/shareaholic.js';
    shr.type = 'text/javascript'; shr.async = 'true';
    shr.onload = shr.onreadystatechange = function() {
      var rs = this.readyState;
      if (rs && rs != 'complete' && rs != 'loaded') return;
      var site_id = 'f96f0b868409f5d2e688f579f67161c7';
      try { Shareaholic.init(site_id); } catch (e) {}
    };
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(shr, s);
  })();
//]]>
</script>

<html><head><title>Online Network Tools - Mobile version: DNS, IP, Whois, Traceroute, Email</title></head> 
<meta name="description" content="Free all-in-one online network troubleshooting, diagnostic and scanning tools at one awesome interface.">
<meta name="keywords" content="dns tools, ping, traceroute, check http headers, whois lookup, password generator, network scanner, spf tool, ip calculation">
    
EOF


echo "<body>"

echo "<div id="fb-root"></div>"      

## HEADER ###
echo "<div id="logo">"

remote_host=`./remote_host.pl | cut -d" " -f6`	  
city=`geoiplookup -f /usr/share/GeoIP/GeoLiteCity.dat $REMOTE_ADDR | grep City | cut -d: -f2`
country=`geoiplookup $REMOTE_ADDR | grep Country | cut -d: -f 2`
asn=`geoiplookup $REMOTE_ADDR | grep ASN | cut -d: -f 2`

##LOGO##
echo "<div class="header1">"

echo "<a href="/m/" title='Go Home!'><img src=/m/images/logo_tools.png width="150" height="31"></a>"
echo "<a href="http://$REMOTE_ADDR" title='Go to your IP Address!' target="_blank"> IP: $REMOTE_ADDR</a>"

## Social icons ###
echo "<span class="right">"

echo "<a target="_blank" class="metro" href="/m/track.cgi" title='Track your location on Google Map!'><span class="icon-location"></span></a>"
echo "<a target="_blank" class="metro" href="https://www.facebook.com/TecMint" title='Tecmint on Facebook'><span class="icon-facebook"></span></a>"
echo "<a target="_blank" class="metro" href="https://twitter.com/tecmint" title='Tecmint on Twitter'><span class="icon-twitter"></span></a>"
echo "<a target="_blank" class="metro" href="https://plus.google.com/+Tecmint/posts" title='Tecmint on Google Plus'><span class="icon-google-plus"></span></a>"
echo "<a target="_blank" class="metro" href="http://tecmint.com" title='Go to Tecmint.com'><span class="icon-home"></span></a>"
echo "<a target="_blank" class="metro" href="/" title='Desktop Version'><span class="icon-firefox"></span></a>"
echo "<a target="_blank" class="metro" href="/m/scan/" title='Scan ++'><span class="icon-search"></span></a>"

echo "</span>"

echo "<div></div>"
echo "</div>"
echo "</div>"


## MENU ##
#echo "<div id="menu" align="center" >"
echo "<div class="header">"

    echo "<a id="button" href="/m/index.cgi" ><strong>dns tools</strong></a>"
	echo "<a id="button" href="/m/dns.cgi" ><strong>records</strong></a>"
	echo "<a id="button" href="/m/net.cgi"><strong>network</strong></a>"
	echo "<a id="button" href="/m/mail.cgi"><strong>mail</strong></a>"
	echo "<a id="button" href="/m/scan.cgi"><strong>scanners</strong></a>"
	echo "<a id="button" href="/m/geoip.cgi"><strong>location</strong></a>"
	echo "<a id="button" href="/m/ipcalc.cgi"><strong>ipcalc</strong></a>"
	echo "<a id="button" href="/m/headers.cgi"><strong>headers</strong></a>"
	echo "<a id="button" href="/m/url.cgi"><strong>tinyURL</strong></a>"
	echo "<a id="button" href="/m/pass.cgi"><strong>genpass</strong></a>"	
	##echo "<a id="button" href="/m/scan"><strong>scan+</strong></a>"	
echo "<div class="clr"> </div>"
echo "</div>"
echo "</div>"


## LOCATION MENU ###
echo "<div id="menu1" align="left" >"
echo "<div align="left" style="color:#3778C7"><normal> Host: <a style="color:#AE0C32">$remote_host</a>Location:<a style="color:#AE0C32">$country </a>City:<a style="color:#AE0C32">$city </a> ASN:<a style="color:#AE0C32">$asn</a> </normal></div>" 

### FACEBOOK LIKE ###
#echo "<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://tools.tecmint.com" data-via="tecmint" data-related="tecmint" data-hashtags="tecmint">Tweet</a>"
#echo " <div class="g-plusone" data-size="medium"></div>"
#echo " <div class="fb-like" data-href="http://tools.tecmint.com" data-width="auto" data-layout="button_count" data-action="like" data-show-faces="false" data-share="true"></div>"
echo "</div>"

## TOP GOOGLE ADD ##
echo "<div class="advertise_top">"
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


## START PAGE ###
#echo "  <div id="code_show" align="left">  "
#echo "<pre class="prettyprint"</pre>"
echo "<div id="nocode" align="left">"
