#!/bin/bash
echo "Content-type: text/html"
echo ""
POST=$(</dev/stdin)

cat head_dns.html   
./head.cgi

### SEARCH BLOCK ###	
echo "<div class="search_block">"
	
####  SEARCH FORMS ###
echo "<div class="left">"

echo " <div class="span9"> <p class="description">"
 
echo "Choose a DNS Record ! "           
echo "<div class="container">"

### GOOGLE ADS RIGHT ###
cat advertise_left.html
### ENG GOOGLE ADS RIGHT

echo "<div class="grid fluid">"
echo "<div class="row">"

echo "<form method="post">"
	echo "<p><input type=radio name=cmd value=a>  <input id="searchbox" type=text placeholder='domain.tld' name=folder >"
	echo "<input id="submit" value="A" type=submit></p>"

    echo "<p><input type=radio name=cmd value=mx>  <input id="searchbox" type=text name=folder1 value= >"
	echo "<input id="submit" value="MX" type=submit></p>"

    echo "<p><input type=radio name=cmd value=spf>  <input id="searchbox" type=text name=folder2 value= >"
	echo "<input id="submit" value="SPF" type=submit></p>"	

    echo "<p><input type=radio name=cmd value=ns>  <input id="searchbox" type=text name=folder3 value= >"
	echo "<input id="submit" value="NS" type=submit></p>"		
	
    echo "<p><input type=radio name=cmd value=soa>  <input id="searchbox" type=text name=folder4 value= >"
	echo "<input id="submit" value="SOA" type=submit></p>"

    echo "<p><input type=radio name=cmd value=cname>  <input id="searchbox" type=text name=folder5 value= >"
	echo "<input id="submit" value="cname" type=submit></p>"

    echo "<p><input type=radio name=cmd value=ttl>  <input id="searchbox" type=text name=folder6 value= >"
	echo "<input id="submit" value="TTL" type=submit></p>"
	
    echo "<p><input type=radio name=cmd value=all checked >  <input id="searchbox" type=text name=folder7 value= >"
	echo "<input id="submit" value="ALL" type=submit></p>"
 
    echo "<p><input type=radio name=cmd value=trace>  <input id="searchbox" type=text name=folder8 value= >"
	echo "<input id="submit" value="dig+trace" type=submit></p>"	
echo "</form></div>"
echo " </div></div>"
      
      ## Fereastra ###     
echo "</pre><div class="window"><div class="caption"><span class="icon icon-windows"></span><div class="title">Window Result</div><button class="btn-min"></button><button class="btn-max"></button><button class="btn-close"></button></div>"
echo "<div class="content">"
   
echo "<pre class="prettyprint linenums no-phone" style="margin-top: 10px""    

echo "  <div id="code2" align="left">  "

	# read in our parameters
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER1=`echo "$POST" | sed -n 's/^.*folder1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
    FOLDER2=`echo "$POST" | sed -n 's/^.*folder2=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER3=`echo "$POST" | sed -n 's/^.*folder3=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER4=`echo "$POST" | sed -n 's/^.*folder4=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER5=`echo "$POST" | sed -n 's/^.*folder5=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER6=`echo "$POST" | sed -n 's/^.*folder6=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`	
	FOLDER7=`echo "$POST" | sed -n 's/^.*folder7=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`	
	FOLDER8=`echo "$POST" | sed -n 's/^.*folder8=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`		
	
	# test if any parameters were passed
	if [ $CMD ]
	then
	  case "$CMD" in

            a)
              echo "A records for  $FOLDER :<pre><div align="left">"
			  echo "-------------------------------------------------------------------------------"
              /usr/bin/host -t a "$FOLDER" 2> /dev/null
			  echo "-------------------------------------------------------------------------------"
              echo "</pre>"	
				;;
				
            mx)
              echo "MX records for $FOLDER1 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              /usr/bin/host -t mx "$FOLDER1" 2> /dev/null
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;
 
			spf)
              echo "SPF records for $FOLDER2 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              /usr/bin/host -t txt "$FOLDER2" 2> /dev/null
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;

			ns)
              echo "NS records for $FOLDER3 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              /usr/bin/host -t ns "$FOLDER3" 2> /dev/null
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;			  

			soa)
              echo "SOA records for $FOLDER4 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              /usr/bin/host -t soa "$FOLDER4" 2> /dev/null
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;		
			
			cname)
              echo "CNAME records for $FOLDER5 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              /usr/bin/host -t cname "$FOLDER5" 2> /dev/null
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;		
          
			ttl)
              echo "TTL records for $FOLDER6 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              /usr/bin/host -v "$FOLDER6" 2> /dev/null
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;		
			all)
              echo "ALLL records for $FOLDER7 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              /usr/bin/host -a "$FOLDER7" 2> /dev/null
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;		              
			trace)
              echo "Dig+trace records for $FOLDER8 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              /usr/bin/dig +trace "$FOLDER8" 2> /dev/null
			  echo "--------------------------------------------------------------------------------"
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

