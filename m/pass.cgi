#!/bin/bash

POST=$(</dev/stdin)
 
./head.cgi

	# read in our parameters in form method get
    	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
	# test if any parameters were passed
	if [ $CMD ]
		then
	  case "$CMD" in
		
		complex)  
    genpass() {
        local l=$1
        [ "$l" == "" ] && l="$FOLDER"
        tr -dc A-Za-z0-9_\!\(\)\-\.\?\[\]\{\}\~\`\!@\#\$\%\&\* 2> /dev/null < /dev/urandom | head -c ${l} 2> /dev/null | xargs 
				}
				
 echo "<div id="text" align="center"><p>Your generated $FOLDER characters long password is:</p></div>"
	echo "<div id="block" align="left"><pre>"
echo  "`genpass`"	
echo "</div>"	
	;;
           simple)           
    genpass() {
        local l=$1
        [ "$l" == "" ] && l="$FOLDER"
        tr -dc A-Za-z0-9 2> /dev/null < /dev/urandom | head -c ${l} 2> /dev/null | xargs 
				}
 echo "<div id="text" align="center"><p>Your generated $FOLDER characters long password is:</p></div>"
	echo "<div id="block" align="left"><pre>"
echo  "`genpass`"	
echo "</div>"		
    ;;
		*)
	    echo "Unknown command $CMD<br>"
	;;
	  esac
	fi
            	
echo "</div>"

### SEARCH BLOCK ###	
echo "<div class="search_block">"	

####  SEARCH FORMS ###
echo "<div class="left">"

echo "Please choose password complexity and lenght: "
echo "<p><a style="color:#379DF6"><small> After entering the lenght value refresh page to generate another password!</small></a></p> "           

cat << EOF 
	<form method=POST>
<select id="select" name="cmd" value=cmd>
    <option value="----">Password Complexity</option>
	<option value="simple">Simple</option>
        <option value="complex">Complex</option>
</select>
	<p><input id="searchbox2" type=text placeholder="10 "  name=folder>
	<input id="submit" value="password" type=submit></p>
</form>

EOF
echo " </div> "	

### LEFT ADVERTISE ###
cat advertise_left.html
echo " </div> "
./footer.cgi
