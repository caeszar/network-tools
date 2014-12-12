#!/bin/bash

## TOP LONG ADVERTISE ##
echo "<div class="advertise_top">"
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


## FACEBOOK COMMENTS ##
#echo "<div id="fbcomments" align="center">"

#echo "<div> Facebook Comments</div>"
echo "</div>"



echo "<div id="footer"><center><h6> $HTTP_USER_AGENT <p>Information generated on $(date) </p><p> A website created by Cezar Matei  &copy; Copyright `date +"%Y"` <a id="a" target="_blank" href="http://tecmint.com"> Tecmint.com </a></p></h6></center> </div>"
echo "</body></html>"
