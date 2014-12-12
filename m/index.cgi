#!/bin/bash 

POST=$(</dev/stdin)
 
./head.cgi

 
	#### read in our parameters ###
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER1=`echo "$POST" | sed -n 's/^.*folder1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
    FOLDER2=`echo "$POST" | sed -n 's/^.*folder2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER3=`echo "$POST" | sed -n 's/^.*folder3=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
	#### test if any parameters were passed ###
	if [ $CMD ]
	then
	  case "$CMD" in

            dig)
echo "<div id="text" align="center">Dig result for $FOLDER:</div>"
echo "<div id="block" align="left"><pre>"
	/usr/bin/dig "$FOLDER" 2> /dev/null
	echo "</div>"
		  ;;
				
            host)
echo "<div id="text" align="center">Host result for $FOLDER1:</div>"
echo "<div id="block" align="left"><pre>"
    /usr/bin/host "$FOLDER1" 2> /dev/null
	echo "</div>"			  
              ;;
 
			nslookup)
echo "<div id="text" align="center">Nslooup result for $FOLDER2:</div>"
echo "<div id="block" align="left"><pre>"
      /usr/bin/nslookup "$FOLDER2" 2> /dev/null
	echo "</div>"			  
              ;;

			whois)
echo "<div id="text" align="center">Whois $FOLDER3:</div>"
echo "<div id="block" align="left"><pre>"
       /usr/bin/whois "$FOLDER3" 2> /dev/null
	echo "</div>"			  
              ;;			  
		
 			ip)
echo "<div id="text" align="left">Domain $FOLDER4 has IP Address:</div>"
	result=`/usr/bin/dig +short "$FOLDER4" 2> /dev/null`
         while read -r line; do
        echo "<div id="block" align="center">$line</div>"
        done <<< "$result" 			  
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

	echo "<div align=left> please select a tool</div>"
	echo "<form method=POST>"
	echo "<p><input type=radio name=cmd value=ip checked ><input id="searchbox" type=text placeholder="domain.tld" name=folder4 >"
	echo "<input id="submit" value="address" type=submit></p>"       
	echo "<p><input type=radio name=cmd value=dig><input id="searchbox" type=text placeholder=' ' name=folder >"
	echo "<input id="submit" value="dig" type=submit></p>"
    echo "<p><input type=radio name=cmd value=host><input id="searchbox" type=text name=folder1 value= >"
	echo "<input id="submit" value="host" type=submit></p>"
    echo "<p><input type=radio name=cmd value=nslookup><input id="searchbox" type=text name=folder2 value= >"
	echo "<input id="submit" value="nslookup" type=submit></p>"	
    echo "<p><input type=radio name=cmd value=whois><input id="searchbox" type=text name=folder3 value= >"
	echo "<input id="submit" value="whois" type=submit></p>"		
	echo "</form>"
echo " </div> "	

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "	

### FOOTER ###
./footer.cgi
