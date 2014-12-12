#!/bin/bash

POST=$(</dev/stdin)


smtp() {
nc $FOLDER 25 2> /dev/null<< EOF
EHLO $FOLDER
MAIL FROM:<postmaster@$FOLDER>
RCPT TO:<test@domain.tld>
QUIT
EOF
}

smtp_ssl() {
nc $FOLDER 465 2> /dev/null << EOF
EHLO $FOLDER
MAIL FROM:<postmaster@$FOLDER>
RCPT TO:<test@domain.tld>
QUIT
EOF
}

smtp_tls() {
nc $FOLDER 587 2> /dev/null << EOF
EHLO $FOLDER
MAIL FROM:<postmaster@$FOLDER>
RCPT TO:<test@domain.tld>
QUIT
EOF
}

pop3() {
nc $FOLDER 110 2> /dev/null << EOF
USER postmaster@$FOLDER
PASS password
LIST
QUIT
EOF
}

pop3s() {
openssl s_client -connect $FOLDER:995 2> /dev/null << EOF
USER postmaster@$FOLDER
PASS password
QUIT
EOF
}

imap() {
nc $FOLDER 143 2> /dev/null << EOF
a1 LOGIN postmaster@$FOLDER password
a2 LOGOUT
EOF
}

imaps() {
openssl s_client -connect $FOLDER:993 2> /dev/null << EOF
a1 LOGIN postmaster@$FOLDER password
a2 LOGOUT
EOF
}


./head.cgi


	# read in our parameters
	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
		
	# test if any parameters were passed
	if [ $CMD ]
	then
	  case "$CMD" in

            25)
	echo "<div id="text" align="center"><p>SMTP Mail test for <strong><a href="http://$FOLDER" target="_blank" style="color:red">$FOLDER</a></strong> on port $CMD :</p></div>"
	echo "<div id="block" align="left"><pre>"
smtp "$FOLDER" 
	echo "</div>"			  			  
				;;
				
            465)
		echo "<div id="text" align="center"><p>SMTP SSL test for <strong><a href="http://$FOLDER" target="_blank" style="color:red">$FOLDER</a></strong> on port $CMD :</p></div>"
	echo "<div id="block" align="left"><pre>"
smtp_ssl "$FOLDER" 
	echo "</div>"	
              ;;
 
			587)

		echo "<div id="text" align="center"><p>SMTP TLS test for <strong><a href="http://$FOLDER" target="_blank" style="color:red">$FOLDER</a></strong> on port $CMD :</p></div>"
	echo "<div id="block" align="left"><pre>"
smtp_tls "$FOLDER"
	echo "</div>"			  
              ;;

			110)
	echo "<div id="text" align="center"><p>POP3 Mail test for <strong><a href="http://$FOLDER" target="_blank" style="color:red">$FOLDER</a></strong> on port $CMD :</p></div>"
	echo "<div id="block" align="left"><pre>"
pop3 "$FOLDER"
	echo "</div>"			 				
              ;;			  

			995)
	echo "<div id="text" align="center"><p>POP3 SSL for <strong><a href="http://$FOLDER" target="_blank" style="color:red">$FOLDER</a></strong> on port $CMD :</p></div>"
	echo "<div id="block" align="left"><pre>"
pop3s "$FOLDER"
	echo "</div>"			 				
              ;;		
			
			143)
	echo "<div id="text" align="center"><p>IMAP Mail for <strong><a href="http://$FOLDER" target="_blank" style="color:red">$FOLDER</a></strong> on port $CMD :</p></div>"
	echo "<div id="block" align="left"><pre>"
imap "$FOLDER"
	echo "</div>"			 				
              ;;		
          
			993)
		echo "<div id="text" align="center"><p>IMAP SSL test for <strong><a href="http://$FOLDER" target="_blank" style="color:red">$FOLDER</a></strong> on port $CMD :</p></div>"
	echo "<div id="block" align="left"><pre>"
imaps "$FOLDER"
	echo "</div>"			  
              ;;		
	                                                
	     *)
	    echo "<div id="text" align="center"><p>IMAP Mail for <strong><a href="http://$FOLDER" target="_blank" style="color:red">$FOLDER</a></strong> on port $CMD :</p></div>"
	echo "<div id="block" align="left"><pre>"
	echo "Please choose a port!"
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

echo "<div align=left><p> Please select a port !</p></div>"

cat << EOF 
<form method=POST>
<select id="select" name="cmd" value=cmd>
    <option value="----">Select Port</option>
	<option value="25">25 SMTP</option>
        <option value="465">465 SMTP SSL</option>
	<option value="587">587 SMTP TLS</option>
        <option value="110">110 POP3</option>
        <option value="995">995 POP3S</option>
        <option value="143">143 IMAP</option>
        <option value="993">993 IMAPS</option>


</select>
	<p><input id="searchbox" type=text placeholder="domain.tld"  name=folder>
	<input id="submit" value='Test Server' type=submit><p>
</form>

EOF
echo " </div> "	

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "

./footer.cgi   
