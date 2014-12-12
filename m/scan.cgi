#!/bin/bash

POST=$(</dev/stdin)
  
./head.cgi


#### Check port function 
             
      check_port() {
         if test "$#" != "2" ; then
                echo -e " Use script like this:\n"$O" host port "
                exit 1
         else
           nc -z -w 5 $1 $2 2> /dev/null
                result=`echo $?`
				
        case "$result" in 
        
        1)        
echo -e "<p style="color:#FE642E">FAILURE!</p>Port "$2" is NOT OPEN on host "$1"!"
        ;;
        
        0)
echo -e "<p style="color:#F7FE2E">SUCCESS!</p>Port <a style="color:#F7FE2E">"$2"</a> is <a style="color:#F7FE2E">OPEN</a> on host "$1"!"
        ;;
         
       *)
echo -e "Error...!\nPort "$2" not open on host "$1"!"
        ;;
                esac
        fi
               }
## end of check port ###
	 
	# read in our parameters
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER7=`echo "$POST" | sed -n 's/^.*folder7=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER5=`echo "$POST" | sed -n 's/^.*folder5=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER6=`echo "$POST" | sed -n 's/^.*folder6=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	# test if any parameters were passed
	if [ $CMD ]
	then
	  case "$CMD" in		  

			port)
		echo "<div id="text" align="center">Result for port $FOLDER5 on $FOLDER4:</div>"
	echo "<div id="block" align="left"><pre>"
               check_port "$FOLDER4" "$FOLDER5"
	echo "</div>"				  
              ;;		
			
			nmap)
		echo "<div id="text" align="center">Results for $FOLDER6 scan:</div>"
	echo "<div id="block" align="left"><pre>"
               /usr/bin/nmap -T4 -F -n "$REMOTE_ADDR" 2> /dev/null
	echo "</div>"					  
              ;;		
                
	     *)
	      echo "Unknown command $CMD<br>"
	      ;;
	  esac
	fi
echo " </div> "	
	 

### SEARCH BLOCK ###	
echo "<div class="search_block">"	

####  SEARCH FORMS ###
echo "<div class="left">"

echo "<div align=left> please select a tool</div>"
echo "<a style="color:#2B5486"><small>TIP: Scan tool scans only your IP address and requires extra time !</small></a> "
        
echo "<form method=POST>"
	
    echo "<p><input type=radio name=cmd value=port><input id="searchbox1" type=text name=folder4 placeholder="domain.tld"> <input id="searchbox2" type=text name=folder5 placeholder="80">"
	echo "<input id="submit" value='check  port' type=submit></p>"

    echo "<p><input type=radio name=cmd value=nmap checked ><input id="searchbox" type=text name=folder6 value='$REMOTE_ADDR' >"
	echo "<input id="submit" value="scan" type=submit></p>"
	
## Disabled scan plus ##
    #echo "<p><input type=radio name=cmd value=nmap1>  <input id="searchbox" type=text name=folder7 value= >"
	#echo "<input id="submit" value="scan+" type=submit></p>"		
			
echo "</form>"
echo " </div> "	

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "	

 ./footer.cgi
