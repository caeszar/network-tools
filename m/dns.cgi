#!/bin/bash

POST=$(</dev/stdin)

./head.cgi


	# read in our parameters
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
		
	# test if any parameters were passed
	if [ $CMD ]
	then
	  case "$CMD" in

            a)
	echo "<div id="text" align="center"><p>DNS A record for $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
/usr/bin/host -t a "$FOLDER" 2> /dev/null
	echo "</div>"			  			  
				;;
				
            mx)
		echo "<div id="text" align="center"><p>DNS MX record for $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
/usr/bin/host -t mx "$FOLDER" 2> /dev/null
	echo "</div>"	
              ;;
 
			spf)

		echo "<div id="text" align="center"><p>DNS SPF record for $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
/usr/bin/host -t txt "$FOLDER" 2> /dev/null
	echo "</div>"			  
              ;;

			ns)
	echo "<div id="text" align="center"><p>DNS NS record for $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
/usr/bin/host -t ns "$FOLDER" 2> /dev/null
	echo "</div>"			 				
              ;;			  

			soa)
	echo "<div id="text" align="center"><p>DNS SOA record for $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
/usr/bin/host -t soa "$FOLDER" 2> /dev/null
	echo "</div>"			 				
              ;;		
			
			cname)
	echo "<div id="text" align="center"><p>DNS CNAME record for $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
/usr/bin/host -t cname "$FOLDER" 2> /dev/null
	echo "</div>"			 				
              ;;		
          
			ttl)
		echo "<div id="text" align="center"><p>DNS TTL records for $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
/usr/bin/host -v "$FOLDER" 2> /dev/null
	echo "</div>"			  
              ;;		
			all)
	echo "<div id="text" align="center"><p>All DNS record for $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
/usr/bin/host -a "$FOLDER" 2> /dev/null
	echo "</div>"			 				
              ;;		              
			trace)
		echo "<div id="text" align="center"><p>DNS+Trace record for $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
              /usr/bin/dig +trace "$FOLDER" 2> /dev/null
	echo "</div>"			  
              ;;	                                                
	     *)
	      		echo "<div id="text" align="center"><p>DNS+Trace record for $FOLDER:</p></div>"
	echo "<div id="block" align="left"><pre>"
              echo "Please select a port!"
	echo "</div>"
	      ;;
	  esac
	fi
	
	echo " </div> "	
	echo " </div> "	

	

### SEARCH BLOCK ###	
echo "<div class="search_block">"	

####  SEARCH FORMS ###
echo "<div class="left">"	

echo "<div align=left><p> Please select a DNS record !</p></div>"

cat << EOF 
<form method=POST>
<select id="select" name="cmd" value=cmd>
    <option value="----">Select DNS record</option>
		<option value="a">A</option>
        <option value="mx">MX</option>
		<option value="spf">SPF</option>
        <option value="ns">NS</option>
        <option value="soa">SOA</option>
        <option value="cname">CNAME</option>
        <option value="ttl">TTL</option>
        <option value="all">ALL</option>
        <option value="trace">TRACE</option>

</select>
	<p><input id="searchbox" type=text placeholder="domain.tld"  name=folder>
	<input id="submit" value="record" type=submit><p>
</form>

EOF
echo " </div> "	

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "

./footer.cgi   
