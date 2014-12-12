#!/bin/bash

POST=$(</dev/stdin)
 
./head.cgi

	# read in our parameters
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER1=`echo "$POST" | sed -n 's/^.*folder1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
    	FOLDER2=`echo "$POST" | sed -n 's/^.*folder2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER3=`echo "$POST" | sed -n 's/^.*folder3=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
	
	
	# test if any parameters were passed

	if [[ -z "$FOLDER4" ]]
    then
echo > /dev/null
    else

echo "<div id="text" align="center"><p>IP class information for $FOLDER4:</p></div>"
	echo "<div id="block" align="left"><pre>"
       		ipcalc "$FOLDER4"
		sipcalc "$FOLDER4"
	echo "</div>"				  
		
	fi	  	                
	echo "</div>"
			  
			  
### SEARCH BLOCK ###	
echo "<div class="search_block">"	

####  SEARCH FORMS ###
echo "<div class="left">"

	echo "<div align=left> Please enter a IP and a subnet mask!</div>"
	
	echo "<form method=POST>"
	echo "<p><input id="searchbox" type=text placeholder="192.168.10.20/24" name=folder4 >"
	echo "<input id="submit" value="Calculate" type=submit></p>"		
	echo "</form>"
echo " </div> "	

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "

./footer.cgi
