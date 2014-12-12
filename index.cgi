#!/bin/bash
echo "Content-type: text/html"
echo ""
POST=$(</dev/stdin)

cat head.html   
./head.cgi

### SEARCH BLOCK ###	
echo "<div class="search_block">"	

####  SEARCH FORMS ###
echo "<div class="left">"

echo "<div class="span9"> <p class="description">"

echo "Choose a tool"
 
echo "<div class="container">"

### GOOGLE ADS RIGHT ###
cat advertise_left.html
### ENG GOOGLE ADS RIGHT

echo "<div class="grid fluid">"	  
echo "<div class="row">"

	echo "<form method="post" action="/index.cgi">"
	echo "<p><input type=radio name=cmd value=ip checked >  <input id="searchbox" type=text placeholder="domain.tld" name=folder4 >"
	echo "<input id="submit" name="address" value="address" type=submit></p>"
 
	echo "<p><input type=radio name=cmd value=dig>  <input id="searchbox" type=text name=folder >"
	echo "<input id="submit" value="dig" type=submit></p>"

    echo "<p><input type=radio name=cmd value=host>  <input id="searchbox" type=text name=folder1 value= >"
	echo "<input id="submit" value="host" type=submit></p>"

    echo "<p><input type=radio name=cmd value=nslookup>  <input id="searchbox" type=text name=folder2 value= >"
	echo "<input id="submit" value="nslookup" type=submit></p>"	

    echo "<p><input type=radio name=cmd value=whois>  <input id="searchbox" type=text name=folder3 value= >"
	echo "<input id="submit" value="whois" type=submit></p>"
		
		
##  FARA Radio Buton
		
		##	echo "<p><input id="searchbox" type=text placeholder="domain.tld" name=folder4 >"
	    ## echo "<input id="submit" name="cmd" value="ip" type=submit></p>"
echo "</form>"
echo "</div>"
echo "</div></div>"


		   
## Fereastra ###     
echo " </pre><div class="window"><div class="caption"><span class="icon icon-windows"></span><div class="title">Window Result</div><button class="btn-min"></button><button class="btn-max"></button><button class="btn-close"></button></div>"
   
echo "<div class="content">"
echo  "<pre class="prettyprint linenums no-phone" style="margin-top: 15px""

echo "<div id="code2" align="right">"

	# read in our parameters in form method get
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

            dig)
              echo "Output of dig $FOLDER :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------"
              /usr/bin/dig "$FOLDER" 2> /dev/null
			  echo "--------------------------------------------------------------------------"
              echo "</pre>"	
				;;
				
            host)
              echo "Output of host $FOLDER1 :<pre><div align="left">"
			  echo "---------------------------------------------------------------------------"
              /usr/bin/host "$FOLDER1" 2> /dev/null
			  echo "---------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;
 
			nslookup)
              echo "Output of nslookup $FOLDER2 :<pre><div align="left">"
			  echo "----------------------------------------------------------------------------"
              /usr/bin/nslookup "$FOLDER2" 2> /dev/null
			  echo "----------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;

			whois)
              echo "Output of whois $FOLDER3 :<pre><div align="left">"
			  echo "------------------------------------------------------------------------------"
              /usr/bin/whois "$FOLDER3" 2> /dev/null
			  echo "------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;			  
		
 			ip)
              echo "Domain $FOLDER4 has IP address:<pre><div align="left">"
			  echo "-------------------------------------------------------------------------------"
              /usr/bin/dig +short "$FOLDER4" 2> /dev/null
			  echo "-------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;	
	     *)
	      echo "Unknown command $CMD<br>"
	      ;;
	  esac
	fi
echo "</div>"
echo "</div>"
echo "</div>"
echo "</div>"

./footer.cgi
