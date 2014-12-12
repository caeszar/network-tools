#!/bin/bash
echo "Content-type: text/html"
echo ""

POST=$(</dev/stdin)

cat head_pass.html    
./head.cgi

### SEARCH BLOCK ###	
echo "<div class="search_block">"	
####  SEARCH FORMS ###
echo "<div class="left">"
echo "<div class="span9"> <p class="description">"
  
echo "Please enter password lenght: "

echo "<div class="container" style="padding: -0px 0px">"

### GOOGLE ADS RIGHT ###
cat advertise_left.html
### ENG GOOGLE ADS RIGHT


echo "<div class="grid fluid">"
echo "<div class="row"> "


	echo "<form method=POST>"
	echo "<p><input type=radio name=cmd value=simple>  <input id="searchbox" type=text placeholder="8" name=folder >"
	echo "<input id="submit" name="simple" value="simple" type=submit></p>"
  
	echo "<p><input type=radio name=cmd value=complex>  <input id="searchbox" type=text placeholder="8" name=folder1 >"
	echo "<input id="submit" value="complex" type=submit></p>"
	echo "</form>"

	echo " </div> "
    echo "<a style="color:#067D98"><small>TIP: After entering the lenght value refresh page to generate another password!</small></a> "           
    echo " </div></div>"

## Fereastra ###     
   echo "</pre><div class="window"><div class="caption"><span class="icon icon-windows"></span><div class="title">Window Result</div><button class="btn-min"></button><button class="btn-max"></button><button class="btn-close"></button></div>"
   echo "<div class="content">"

	echo "<div id="code2" align="right">"

	# read in our parameters in form method get
    	CMD=`echo "$POST" | sed -n 's/^.*cmd=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
	FOLDER=`echo "$POST" | sed -n 's/^.*folder=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	FOLDER1=`echo "$POST" | sed -n 's/^.*folder1=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"| sed "s/%2F/\//g"`
	
	# test if any parameters were passed
	if [ $CMD ]
		then
	  case "$CMD" in
		
		complex)  
    genpass() {
        local l=$1
        [ "$l" == "" ] && l="$FOLDER1"
        tr -dc A-Za-z0-9_\!\(\)\-\.\?\[\]\{\}\~\`\!@\#\$\%\&\* 2> /dev/null < /dev/urandom | head -c ${l} 2> /dev/null | xargs 2> /dev/null
				}
echo "Your password has $FOLDER1 characters lenght :<pre><div align="left">"
echo "--------------------------------------------------------------------------------"
echo -e "Your generated password is :\n <p><strong><a style="color:#AE0C32">`genpass`</a></strong></p>"
echo "--------------------------------------------------------------------------------"
echo "</pre>"	
	;;
           simple)           
    genpass() {
        local l=$1
        [ "$l" == "" ] && l="$FOLDER"
        tr -dc A-Za-z0-9 2> /dev/null < /dev/urandom | head -c ${l} 2> /dev/null | xargs 2> /dev/null
				}
echo "Your password has $FOLDER characters lenght :<pre><div align="left">"
echo "--------------------------------------------------------------------------------"
echo -e "Your generated password is :\n <p><strong><a style="color:#AE0C32">`genpass`</a></strong></p>"
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
echo "</div>"

./footer.cgi
