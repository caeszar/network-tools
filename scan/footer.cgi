#!/bin/bash

#cat footer.html

echo "<div class="span3 padding10">  <p> </p>  </div></div></div>"	
echo "<div class="span3 padding10">  <p> </p>  </div></div></div>"	

echo "<div class="accordion" data-role="accordion"><div class="accordion-frame"><a href="#" class="heading" align="center" >Information generated on $(date)</a> "
echo "<div class="content"><p>$HTTP_USER_AGENT</p></div></div>"

echo "<div><p></p>  </div></div></div>"	
echo "<div class="accordion"><div align="right" class="accordion-frame"> A website designed by Cezar Matei using OpenSource Code and <a target="_blank" href="http://metroui.org.ua/"> Metro UI CSS 2.0 </a> theme &copy; Copyright <a target="_blank" href="http://tecmint.com"> Tecmint.com </a> `date +"%Y"` </div></div> "

echo "</body></html>"
