#!/bin/bash

echo "<div class="span3 padding10">  <p> </p>  </div></div></div>"	
echo "<div class="span3 padding10">  <p> </p>  </div></div></div>"	

### BOTTOM GOOGLE ADS ###
echo "<div align="center">"
cat << EOF

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Tools_Footer_720x90_Ad -->
<ins class="adsbygoogle"
     style="display:inline-block;width:720px;height:90px"
     data-ad-client="ca-pub-2601749019656699"
     data-ad-slot="6744070172"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

EOF
echo "</div>"
## END GOOGLE ADS ##
echo "<div class="accordion" data-role="accordion"><div align="right" class="accordion-frame"><a href="#" class="heading" align="right" >Information generated on $(date)</a> "
echo "<div class="content"><p>$HTTP_USER_AGENT</p></div></div>"



## FACEBOOK COMMENTS ###
#echo "<div align="center">"

##echo " Facebook Comments "

#echo "</div>"
## END FACEBOOK COMMENTS ##

echo "<div><p></p></div></div></div>"	

## LAST FOOTER ##
echo "<div class="accordion"><div align="right" class="accordion-frame"> A website designed by Cezar Matei using OpenSource Code and <a target="_blank" href="http://metroui.org.ua/"> Metro UI CSS 2.0 </a> theme. <a target="_blank" href="http://tecmint.com"> Tecmint.com </a> &copy; Copyright `date +"%Y"` </div></div> "

echo "</body></html>"
