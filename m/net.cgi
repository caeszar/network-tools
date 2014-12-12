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
	if [ $CMD ]
	then
	  case "$CMD" in

            ping)
 

		echo "<div id="text" align="center"><p>Ping result for $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
/bin/ping -c4 $FOLDER 2> /dev/null
	echo "</div>"		
				;;
				
            traceroute)
		echo "<div id="text" align="center"><p>Traceroute result for $FOLDER1:</p></div>"
	echo "<div id="block" align="left"><pre>"
              /usr/bin/traceroute "$FOLDER1" 2> /dev/null
	echo "</div>"			  
              ;;
 
			tracerouten)
		echo "<div id="text" align="center"><p>Traceroute numerical result for $FOLDER2:</p></div><pre>"
		result=`/usr/bin/traceroute -n "$FOLDER2" 2> /dev/null`
         while read -r line; do
        echo "<div id="block" align="left">$line</div>"
        done <<< "$result" 
              ;;

			tracepath)	
		echo "<div id="text" align="center"><p>Tracepath result for $FOLDER3:</p></div>"
	echo "<div id="block" align="left"><pre>"
              /usr/bin/tracepath "$FOLDER3" 2> /dev/null
	echo "</div>"			  
              ;;			  

			tracepathn)
		echo "<div id="text" align="center"><p>Tracepath numerical result for $FOLDER4:</p></div><pre>"
		 result=`/usr/bin/tracepath -n "$FOLDER4" 2> /dev/null`
         while read -r line; do
        echo "<div id="block" align="left">$line</div>"
        done <<< "$result"               
              ;;
                                  
	     *)
	      echo "Unknown command $CMD<br>"
	      ;;
	  esac
	fi
#echo "</div>"
#echo "</div>"
 

	# read in our parameters
	CMD1=`echo "$POST" | sed -n 's/^.*cmd1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDERA=`echo "$POST" | sed -n 's/^.*foldera=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
		
	# test if any parameters were passed
	if [ $CMD1 ]
	then
	  case "$CMD1" in

            dns)
	echo "<div id="text" align="center"><p> MTR output for $FOLDERA:</p></div>"
	echo "<div id="block" align="left"><pre>"
mtr --report "$FOLDERA" 2> /dev/null
	echo "</div>"			  			  
				;;
				
            nodns)
		echo "<div id="text" align="center"><p>MTR output for <strong><a href="http://$FOLDERA" target="_blank" style="color:red">$FOLDERA</a></strong>:</p></div>"
	echo "<div id="block" align="left"><pre>"
mtr --report --no-dns "$FOLDERA" 2> /dev/null
	echo "</div>"	
              ;;
	                                                
	     *)
	      echo "Unknown command $CMD1<br>"
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
	echo "<form method=POST>"
       
	echo "<p><input type=radio name=cmd value=ping checked ><input id="searchbox" type=text placeholder='domain.tld' name=folder >"
	echo "<input id="submit" value="ping" type=submit></p>"

    	echo "<p><input type=radio name=cmd value=traceroute><input id="searchbox" type=text name=folder1 value= >"
	echo "<input id="submit" value="traceroute" type=submit></p>"

    	echo "<p><input type=radio name=cmd value=tracerouten><input id="searchbox" type=text name=folder2 value= >"
	echo "<input id="submit" value='traceroute n' type=submit></p>"	

    	echo "<p><input type=radio name=cmd value=tracepath><input id="searchbox" type=text name=folder3 value= >"
	echo "<input id="submit" value="tracepath" type=submit></p>"		
	
    	echo "<p><input type=radio name=cmd value=tracepathn><input id="searchbox" type=text name=folder4 value= >"
	echo "<input id="submit" value='tracepath n' type=submit></p>"
			
	echo "</form>"

cat << EOF 

<form method=POST>

<select id="select" name="cmd1" value=cmd1>
    <option value="nodns">Select Output</option>
        <option value="nodns">No DNS</option>
	<option value="dns">Normal</option>
</select>
	<input id="searchbox" type=text placeholder="domain.tld"  name=foldera>
	<input id="submit" value='MTR' type=submit>
</form>

EOF

echo " </div> "	

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "	
	
./footer.cgi
