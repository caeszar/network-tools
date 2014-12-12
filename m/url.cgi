#!/bin/bash

POST=$(</dev/stdin)

./head.cgi


	FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`

	# test if any parameters were passed

		if [[ -z "$FOLDER4" ]]
    then
			echo > /dev/null
    else
	        short_url=`curl -s http://tinyurl.com/api-create.php?url=$"$FOLDER4"`

			echo "<div id="text" align="center"><p>Short URL for $FOLDER4:</p></div>"
	echo "<div id="block" align="left"><pre>"
               echo "Short URL is : <strong><a href="$short_url" target="_blank" style="color:#F7FE2E">$short_url</a></strong>"
        echo "</div>"
	fi	  
echo "</div>"

### SEARCH BLOCK ###	
echo "<div class="search_block">"	

####  SEARCH FORMS ###
echo "<div class="left">"

	echo "<div align=left> Please enter a url!</div>"
	echo "<form method=POST>"

	echo "<p><input id="searchbox" type=text placeholder="domain.tld" name=folder4 >"
	echo "<input id="submit" value='short url' type=submit></p>"

	echo "</form>"
echo " </div> "	

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "
./footer.cgi
