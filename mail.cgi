#!/bin/bash
echo "Content-type: text/html"
echo ""
POST=$(</dev/stdin)

smtp() {
nc -w 20 $FOLDER 25 2> /dev/null << EOF
EHLO $FOLDER
MAIL FROM:<postmaster@$FOLDER>
RCPT TO:<test@domain.tld>
QUIT
EOF
}

smtp_ssl() {
nc -w 20 $FOLDER1 465 2> /dev/null << EOF
EHLO $FOLDER1
MAIL FROM:<postmaster@$FOLDER1>
RCPT TO:<test@domain.tld>
QUIT
EOF
}

smtp_tls() {
nc -w 20  $FOLDER2 587 2> /dev/null << EOF
EHLO $FOLDER2
MAIL FROM:<postmaster@$FOLDER2>
RCPT TO:<test@domain.tld>
QUIT
EOF
}

pop3() {
nc -w 20 $FOLDER3 110 2> /dev/null << EOF
USER postmaster@$FOLDER3
PASS password
LIST
QUIT
EOF
}

pop3s() {
openssl s_client -connect $FOLDER4:995 2> /dev/null << EOF
USER postmaster@$FOLDER4
PASS password
QUIT
EOF
}

imap() {
nc -w 20 $FOLDER5 143 2> /dev/null << EOF
a1 LOGIN postmaster@$FOLDER5 password
a2 LOGOUT
EOF
}

imaps() {
openssl s_client -connect $FOLDER6:993 2> /dev/null << EOF
a1 LOGIN postmaster@$FOLDER6 password
a2 LOGOUT
EOF
}

cat head_mail.html   
./head.cgi

### SEARCH BLOCK ###	
echo "<div class="search_block">"
	
####  SEARCH FORMS ###
echo "<div class="left">"

echo " <div class="span9"> <p class="description">"
 
echo "Choose a Mail Port ! "           
echo "<div class="container">"

### GOOGLE ADS RIGHT ###
cat advertise_left.html
### ENG GOOGLE ADS RIGHT

echo "<div class="grid fluid">"
echo "<div class="row">"

echo "<form method="post">"
	echo "<p><input type=radio name=cmd value=25>  <input id="searchbox" type=text placeholder='domain.tld' name=folder >"
	echo "<input id="submit" value='25 SMTP' type=submit></p>"

    echo "<p><input type=radio name=cmd value=465>  <input id="searchbox" type=text name=folder1 value= >"
	echo "<input id="submit" value='465 SSL' type=submit></p>"

    echo "<p><input type=radio name=cmd value=587>  <input id="searchbox" type=text name=folder2 value= >"
	echo "<input id="submit" value='587 TLS' type=submit></p>"	

    echo "<p><input type=radio name=cmd value=110>  <input id="searchbox" type=text name=folder3 value= >"
	echo "<input id="submit" value='110 POP3' type=submit></p>"		
	
    echo "<p><input type=radio name=cmd value=995>  <input id="searchbox" type=text name=folder4 value= >"
	echo "<input id="submit" value='995 POP3S' type=submit></p>"

    echo "<p><input type=radio name=cmd value=143>  <input id="searchbox" type=text name=folder5 value= >"
	echo "<input id="submit" value='143 IMAP' type=submit></p>"

    echo "<p><input type=radio name=cmd value=993>  <input id="searchbox" type=text name=folder6 value= >"
	echo "<input id="submit" value='993 IMAPS' type=submit></p>"
	
	
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

            25)
              echo "SMTP test for  $FOLDER :<pre><div align="left">"
			  echo "-------------------------------------------------------------------------------"
              smtp "$FOLDER"
			  echo "-------------------------------------------------------------------------------"
              echo "</pre>"	
				;;
				
            465)
              echo "SMTP SSL test for $FOLDER1 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              smtp_ssl "$FOLDER1"
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;
 
			587)
              echo "STMP TLS test for $FOLDER2 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              smtp_tls "$FOLDER2" 
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;

			110)
              echo "POP3 Mail test for $FOLDER3 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              pop3 "$FOLDER3"
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;			  

			995)
              echo "POP3 SSL Mail test for $FOLDER4 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              pop3s "$FOLDER4"
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;		
			
			143)
              echo "IMAP Mail test for $FOLDER5 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              imap "$FOLDER5"
			  echo "--------------------------------------------------------------------------------"
              echo "</pre>"			 				
              ;;		
          
			993)
              echo "IMAP SSL Mail test for $FOLDER6 :<pre><div align="left">"
			  echo "--------------------------------------------------------------------------------"
              imaps "$FOLDER6"
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

