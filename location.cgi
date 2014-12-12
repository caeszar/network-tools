#!/bin/bash
echo "Content-type: text/html"
echo ""

cat head.html  
./head.cgi

echo " <div class="span9"> <p class="description">"
 
cat location.php

./footer.cgi
