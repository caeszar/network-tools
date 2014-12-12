#!/bin/bash  
./head.cgi
#### Check port function 
             
      check_port() {
         if test "$#" != "2" ; then
                echo -e " Use script like this:\n"$O" host port "
                exit 1
                        else
           nc -z -w 5 $1 $2
                result=`echo $?`
				
        case "$result" in 
        
        1)        
echo "<p><strong><a style="color:#AE0C32">FAILURE!</a></strong></p>Port <a style="color:#AE0C32">"$2"</a> not open on host <a style="color:#AE0C32">"$1"</a>!"
        ;;
        
        0)
echo -e "<p><strong><a style="color:#00BE49">SUCCESS!</a></strong></p>Port <a style="color:#00BE49">"$2"</a> is open on host <a style="color:#00BE49">"$1"</a>!"
        ;;
         
       *)
         echo -e "Error...!\nPort "$2" not open on host "$1"!"
        ;;
                esac
        fi
               }
## end of check port ###
	 
	# read in our parameters
	CMD=`echo "$QUERY_STRING" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$QUERY_STRING" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER7=`echo "$QUERY_STRING" | sed -n 's/^.*folder7=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER4=`echo "$QUERY_STRING" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER5=`echo "$QUERY_STRING" | sed -n 's/^.*folder5=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER6=`echo "$QUERY_STRING" | sed -n 's/^.*folder6=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	# test if any parameters were passed
	if [ $CMD ]
	then
	  case "$CMD" in


			nmap1)	
	echo "<div id="text" align="center">Scan result for $FOLDER7:</div>"
echo "<div id="block" align="left"><pre>"
	/usr/bin/nmap -T4 -A -F -n "$FOLDER7"
	echo "</div>"		  
              ;;			  

			nmap2)
		echo "<div id="text" align="center">No Ping Scan result for $FOLDER4:</div>"
echo "<div id="block" align="left"><pre>"
	/usr/bin/nmap -n -Pn "$FOLDER4" 
	echo "</div>"		  
              ;;		

			nmap3)
		echo "<div id="text" align="center">No Ping Scan result for $FOLDER5:</div>"
echo "<div id="block" align="left"><pre>"
	/usr/bin/nmap -n -Pn -A "$FOLDER5" 
	echo "</div>"		  
              ;;
			  
			nmap)
			echo "<div id="text" align="center">Scan result for $FOLDER6:</div>"
echo "<div id="block" align="left"><pre>"
	  /usr/bin/nmap -T4 -F -n "$FOLDER6"
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

echo "<div align=left> Please select a tool !</div>"
#echo "<a style="color:#0CE9E9"><small>TIP: Be aware that scan tool scans only your IP address and requires extra time !</small></a> "
        
echo "<form method=get>"

    echo "<p><input type=radio name=cmd value=nmap checked >  <input id="searchbox" type=text placeholder="$REMOTE_ADDR" name=folder6 value= >"
	echo "<input id="submit" value="scan" type=submit></p>"
	
    echo "<p><input type=radio name=cmd value=nmap1>  <input id="searchbox" type=text name=folder7 value= >"
	echo "<input id="submit" value="scan+" type=submit></p>"	
	
    echo "<p><input type=radio name=cmd value=nmap2>  <input id="searchbox" type=text name=folder4>"
    echo "<input id="submit" value='no ping scan' type=submit></p>"
	
	echo "<p><input type=radio name=cmd value=nmap3>  <input id="searchbox" type=text name=folder5>"
    echo "<input id="submit" value='no ping scan+' type=submit></p>"
			
	echo "</form>"
echo " </div> "	

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "	

### FOOTER ###
./footer.cgi
