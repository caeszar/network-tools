#!/bin/bash
echo "Content-type: text/html"
echo ""
POST=$(</dev/stdin)
	
cat head_net.html   
./head.cgi

### SEARCH BLOCK ###	
echo "<div class="search_block">"	
####  SEARCH FORMS ###
echo "<div class="left">"

echo " <div class="span9"> <p class="description">"

echo "Choose a tool !"           
echo "<div class="container">"

### GOOGLE ADS RIGHT ###
cat advertise_left.html
### ENG GOOGLE ADS RIGHT

      echo "<div class="grid fluid">"
      echo "<div class="row"> "

	echo "<form method=post>"      
	echo "<p><input type=radio name=cmd value=ping checked>  <input id="searchbox" type=text placeholder="$REMOTE_ADDR" name=folder >"
	echo "<input id="submit" value="Ping" type=submit></p>"

    echo "<p><input type=radio name=cmd value=traceroute>  <input id="searchbox" type=text name=folder1 value= >"
	echo "<input id="submit" value="Traceroute" type=submit></p>"

    echo "<p><input type=radio name=cmd value=tracerouten>  <input id="searchbox" type=text name=folder2 value= >"
	echo "<input id="submit" value='Traceroute n' type=submit></p>"	

    echo "<p><input type=radio name=cmd value=tracepath>  <input id="searchbox" type=text name=folder3 value= >"
	echo "<input id="submit" value="Tracepath" type=submit></p>"		
	
    echo "<p><input type=radio name=cmd value=tracepathn>  <input id="searchbox" type=text name=folder4 value= >"
	echo "<input id="submit" value='Tracepath n' type=submit></p>"	
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

echo "<a style="color:#067D98"><small>TIP: Be aware that some routers are configured to ignore ICMP replay packets and traceroute, tracepath and mtr can take extra time !</small></a> "

echo "</div></div>"
      
      ## Fereastra ###     
echo "</pre><div class="window"><div class="caption"><span class="icon icon-windows"></span><div class="title">Window Result</div><button class="btn-min"></button><button class="btn-max"></button><button class="btn-close"></button></div>"
   
echo "<div class="content">"

echo "<pre class="prettyprint linenums no-phone" style="margin-top: 15px""    

echo "<div id="code2" align="left">"

	 
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
              echo "Ping result for  $FOLDER :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              
		/bin/ping -c4 "$FOLDER" 2> /dev/null

			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"	
				;;
				
            traceroute)
              echo "Traceroute result for $FOLDER1 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              /usr/bin/traceroute "$FOLDER1" 2> /dev/null
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;
 
			tracerouten)
              echo "Traceroute numerical $FOLDER2 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              /usr/bin/traceroute -n "$FOLDER2" 2> /dev/null               
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;

			tracepath)
              echo "Tracepath result for $FOLDER3 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              /usr/bin/tracepath "$FOLDER3" 2> /dev/null          
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;			  

			tracepathn)
              echo "Tracepath numerical result for $FOLDER4 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              result=`/usr/bin/tracepath -n "$FOLDER4" 2> /dev/null` 
         while read -r line; do
        echo "................................................................................" 
        echo "<strong> $line </strong>"
        done <<< "$result"               
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;
                                  
	     *)
	      echo "Unknown command $CMD<br>"
	      ;;
	  esac
	fi


	# read in our parameters
	CMD1=`echo "$POST" | sed -n 's/^.*cmd1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDERA=`echo "$POST" | sed -n 's/^.*foldera=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
		
	# test if any parameters were passed
	if [ $CMD1 ]
	then
	  case "$CMD1" in

            dns)
              echo "MTR output for $FOLDERA: :<pre><div align="left">"
			  echo "------------------------------------------------------------------------------------"
              mtr --report "$FOLDERA" 2> /dev/null         
			  echo "------------------------------------------------------------------------------------"
              echo "</pre>"
			  			  
				;;
				
            nodns)
              echo "MTR output for <strong><a href="http://$FOLDERA" target="_blank" style="color:red">$FOLDERA</a></strong>:<pre><div align="left">"
			  echo "-------------------------------------------------------------------------------------"
              mtr --report --no-dns "$FOLDERA" 2> /dev/null          
			  echo "-------------------------------------------------------------------------------------"
              echo "</pre>"
			  
              ;;
	                                                
	     *)
	      echo "Unknown command $CMD1<br>"
	      ;;
	  esac
	fi


echo "</div>"
echo "</div>"
echo "</div>"
echo "</div>"

./footer.cgi
