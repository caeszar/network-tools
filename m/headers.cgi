#!/bin/bash 

POST=$(</dev/stdin)

./head.cgi


	# read in our parameters
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER1=`echo "$POST" | sed -n 's/^.*folder1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`	
	
	# test if any parameters were passed
	if [ $CMD ]
	then
	  case "$CMD" in

            head)
	 echo "<div id="text" align="center"><p>Headers for  $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
              curl -I "$FOLDER" 2> /dev/null
	echo "</div>"		  
				;;
				
            ssl)	
		 echo "<div id="text" align="center"><p>SSL Headers for $FOLDER1 :</p></div>"
	echo "<div id="block" align="left"><pre>"
			curl -Iv https://"$FOLDER1" 2> /dev/null
  echo "</div>"			  
              ;;
	     *)
	      echo "Unknown command $CMD<br>"
	      ;;
	  esac
	fi
	
	echo " </div> "	
	echo " </div> "	


### SEARCH BLOCK ###	
echo "<div class="search_block">"	

####  SEARCH FORMS ###
echo "<div class="left">"

echo "<div align=left> Please enter domain name !</div>"

	echo "<form method=POST>"
       
	echo "<p><input type=radio name=cmd value=head checked ><input id="searchbox" type=text placeholder='domain.tld' name=folder>"
	echo "<input id="submit" value='headers' type=submit></p>"

    echo "<p><input type=radio name=cmd value=ssl><input id="searchbox" type=text name=folder1 value= >"
	echo "<input id="submit" value='SSL head' type=submit></p>"

	echo "</form>"
echo " </div> "	

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "
./footer.cgi
