#!/bin/bash
echo "Content-type: text/html"
echo ""

POST=$(</dev/stdin)

cat head_url.html   
./head.cgi

### SEARCH BLOCK ###	
echo "<div class="search_block">"	
####  SEARCH FORMS ###
echo "<div class="left">"

echo " <div class="span9"> <p class="description">"

echo "Choose a tool !"           
echo "<div class="container" style="padding: -0px 0px">"

### GOOGLE ADS RIGHT ###
cat advertise_left.html
### ENG GOOGLE ADS RIGHT


echo "<div class="grid fluid">"
echo "<div class="row"> "


	echo "<form method=POST>"
	echo "<p><input id="searchbox" type=text placeholder="domain.tld" name=folder4 >"
	echo "<input id="submit" value="url" type=submit></p>"		
	echo "</form>"
echo "</div> "
echo "</div></div>"
      
      ## Fereastra ###     
echo "</pre><div class="window"><div class="caption"><span class="icon icon-windows"></span><div class="title">Window Result</div><button class="btn-min"></button><button class="btn-max"></button><button class="btn-close"></button></div>"
   
echo "<div class="content">"

echo "<div id="code1" align="right">"
	 
# read in our parameters in form method get
  FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
	# test if any parameters were passed
              echo "Output of shorturl $FOLDER4 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
		if [[ -z "$FOLDER4" ]]
    then
        echo "Enter a long URL:"
    else
        short_url=`curl -s http://tinyurl.com/api-create.php?url=$FOLDER4`
              echo "Short URL is : <font size="4px"><a href="$short_url" target="_blank" style="color:#AE0C32">$short_url</a></font>"
	fi	  
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"	
echo "</div>"
echo "</div>"
echo "</div>"
echo "</div>"
echo "</div>"

./footer.cgi
