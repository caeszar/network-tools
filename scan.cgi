#!/bin/bash
echo "Content-type: text/html"
echo ""

POST=$(</dev/stdin)

cat head_scan.html    
./head.cgi

### SEARCH BLOCK ###	
echo "<div class="search_block">"	
####  SEARCH FORMS ###
echo "<div class="left">"

echo " <div class="span9"> <p class="description">"

echo "Choose a tool !"           
echo "<div class="container" style="padding: -0px 0px">"

### GOOGLE ADS RIGHT ###
cat advertise_left.html
### ENG GOOGLE ADS RIGHT


echo " <div class="grid fluid">"
echo "<div class="row"> "

echo "<form method=POST>"
	
    echo "<p><input type=radio name=cmd value=port> <input id="searchbox" type=text name=folder4 placeholder="domain.tld"> <input id="searchbox2" type=text name=folder5 placeholder="80">"
	echo "<input id="submit" value='check port' type=submit></p>"

    echo "<p><input type=radio name=cmd value=nmap checked>  <input id="searchbox" type=text placeholder="$REMOTE_ADDR" name=folder6 value='$REMOTE_ADDR' >"
	echo "<input id="submit" value="scan" type=submit></p>"
	
## Disabled scan plus ##
    #echo "<p><input type=radio name=cmd value=nmap1>  <input id="searchbox" type=text name=folder7 value= >"
	#echo "<input id="submit" value="scan+" type=submit></p>"		
			
echo "</form>"
echo "</div> "
	
echo "<a style="color:#067D98"><small>TIP: Be aware that scan tool scans only your IP address and requires extra time !</small></a> "
    
echo "</div></div>"
      
## Fereastra ###     
   echo " </pre><div class="window"><div class="caption"><span class="icon icon-windows"></span><div class="title">Window Result</div><button class="btn-min"></button><button class="btn-max"></button><button class="btn-close"></button></div>"
   
   echo " <div class="content">"
   echo "<pre class="prettyprint linenums no-phone" style="margin-top: 15px""    
   echo "<div id="code2" align="left">"
	 
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


			nmap1)
              echo "Results for $FOLDER7 scan+:<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
                /usr/bin/nmap -A -T4 -F "$FOLDER7" 2> /dev/null
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;			  

			port)
              echo "Result for port $FOLDER5 on $FOLDER4 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              check_port "$FOLDER4" "$FOLDER5" 2> /dev/null
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;		
			
			nmap)
              echo "Results for $FOLDER6 scan:<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
               /usr/bin/nmap -T4 -F -n "$REMOTE_ADDR" 2> /dev/null
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
