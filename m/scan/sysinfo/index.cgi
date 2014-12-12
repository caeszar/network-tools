#!/bin/bash
echo "Content-type: text/html"


used=`free -m | awk 'NR==3' | awk '{ printf $3}'`
total=`free -m | awk 'NR==2' | awk '{ printf $2}'`
all=`echo "$used*100/$total" | bc`

used1=`free -m | awk 'NR==3' | awk '{ printf $4}'`
total1=`free -m | awk 'NR==2' | awk '{ printf $2}'`
all1=`echo "$used1*100/$total1" | bc`



cat << EOF

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
<!--	<meta http-equiv="refresh" content="30" />  -->
    <title>System Info for `hostname -f` </title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/style.css">


	
</head>
  <body>
    <div class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a href="./" class="navbar-brand">`hostname -f`</a>
        </div>
		
		
        <div class="navbar-collapse collapse" id="navbar-main">
          <ul class="nav navbar-nav">
          
            <li>
              <a href="http://`echo $SERVER_ADDR`">`echo $SERVER_ADDR`</a>
            </li>
         
          </ul>

          <ul class="nav navbar-nav navbar-right">
            <li><a href="https://github.com/caezsar/sysinfo" target="_blank">GitHub</a></li>    
          </ul>
        </div>
      </div>
    </div>


    <div class="container">
      <div class="page-header" id="banner">
        <div class="row">
          <div class="col-lg-10">


        <div class="row">
          <div class="col-lg-12">
            <h3>System Info generated on `date` </h3> 
          </div>
        </div>
		





<div class="page-header" ></div>   
<h4>CPU Statistics</h4>	
		  
             <div class="bs-component" align="center">
			<h6 id="progress-stacked"><p class="text-warning"> Idle, User, System, Iowait </p></h6>
              <div class="progress">

                <div class="progress-bar progress-bar-success" style="width:`iostat | awk 'NR==4' | awk '{ printf $6}'`%"> `iostat | awk 'NR==4' | awk '{ printf $6}'`% Idle </div> Idle
            </div> 

              <div class="progress">
<div class="progress-bar progress-bar-info" style="width:`iostat | awk 'NR==4' | awk '{ printf $1}'`%"> `iostat | awk 'NR==4' | awk '{ printf $1}'`% </div> User      
            </div> 

              <div class="progress">
<div class="progress-bar progress-bar-warning" style="width:`iostat | awk 'NR==4' | awk '{ printf $3}'`%"> `iostat | awk 'NR==4' | awk '{ printf $3}'`% </div> System    
            </div> 

              <div class="progress">
<div class="progress-bar progress-bar-danger" style="width:`iostat | awk 'NR==4' | awk '{ printf $4}'`%"> `iostat | awk 'NR==4' | awk '{ printf $4}'`% </div> Iowait    
            </div> 





	
<div class="page-header"></div>   
<h4>RAM Memory</h4>
		   
             <div class="bs-component" align="center">
			<h6 id="progress-stacked"><p class="text-warning"> RAM BAR - Used, Shared, Buffered, Cached, Free </p></h6>
              <div class="progress">

                <div class="progress-bar progress-bar-success" style="width:`free -m | awk '/Mem/ { printf("%3.1f%%", $3/$2*100) }'`"> `free -m | awk '/Mem/ { printf("%3.1f%%", $3/$2*100) }'` </div>
                <div class="progress-bar progress-bar-info" style="width:`free -m | awk '/Mem/ { printf("%3.1f%%", $5/$2*100) }'`"> `free -m | awk '/Mem/ { printf("%3.1f%%", $5/$2*100) }'` </div>
                <div class="progress-bar progress-bar-warning" style="width:`free -m | awk '/Mem/ { printf("%3.1f%%", $6/$2*100) }'`"> `free -m | awk '/Mem/ { printf("%3.1f%%", $6/$2*100) }'` </div>
                <div class="progress-bar progress-bar-danger" style="width: `free -m | awk '/Mem/ { printf("%3.1f%%", $7/$2*100) }'`"> `free -m | awk '/Mem/ { printf("%3.1f%%", $7/$2*100) }'` </div>				
             `free -m | awk '/Mem/ { printf("%3.1f%%", $4/$2*100) }'` / `free -h | awk '/Mem/ { print $2 }'`
			  </div>
   

             <div class="bs-component" align="center">
			<h6 id="progress-stacked"><p class="text-warning"> RAM Bars </p></h6>
              <div class="progress">
                <div class="progress-bar progress-bar-info" style="width:`echo $all1%`"> `echo $all1%` </div>  Free: `free -h | grep "buffers/cache" | awk '{print $4}'` / `free -h | awk '/Mem/ { print $2 }'`				    
			  </div>

              <div class="progress">
                <div class="progress-bar progress-bar-success" style="width:`echo $all%`"> `echo $all%` </div>  Used: `free -h | grep "buffers/cache" | awk '{print $3}'` / `free -h | awk '/Mem/ { print $2 }'`				    
			  </div>

              <div class="progress">
                <div class="progress-bar progress-bar-info" style="width:`free -m | awk '/Mem/ { printf("%3.1f%%", $5/$2*100) }'`"> `free -m | awk '/Mem/ { printf("%3.1f%%", $5/$2*100) }'` </div>  Shared: `free -h | awk '/Mem/ { print $5 }'` / `free -h | awk '/Mem/ { print $2 }'`				    
			  </div>

              <div class="progress">
                <div class="progress-bar progress-bar-warning" style="width:`free -m | awk '/Mem/ { printf("%3.1f%%", $6/$2*100) }'`"> `free -m | awk '/Mem/ { printf("%3.1f%%", $6/$2*100) }'` </div>  Bufferd: `free -h | awk '/Mem/ { print $6 }'` / `free -h | awk '/Mem/ { print $2 }'`				    
			  </div>
              <div class="progress">
                <div class="progress-bar progress-bar-danger" style="width:`free -m | awk '/Mem/ { printf("%3.1f%%", $7/$2*100) }'`"> `free -m | awk '/Mem/ { printf("%3.1f%%", $7/$2*100) }'` </div>  Cached: `free -h | awk '/Mem/ { print $7 }'` / `free -h | awk '/Mem/ { print $2 }'`				    
			  </div>
         </div> 






<div class="page-header"></div>   
<h4>System Load</h4>	
	  
             <div class="bs-component" align="center">
			<h6 id="progress-stacked"><p class="text-warning"> 5min 10 min 15 min </p></h6>
              <div class="progress">
                <div class="progress-bar progress-bar-success" style="width:`/bin/cat /proc/loadavg | /usr/bin/awk '{print $1}'`%"> `/bin/cat /proc/loadavg | /usr/bin/awk '{print $1}'`% </div> 5 Min
            </div> 

              <div class="progress">
<div class="progress-bar progress-bar-info" style="width:`/bin/cat /proc/loadavg | /usr/bin/awk '{print $2}'`%"> `/bin/cat /proc/loadavg | /usr/bin/awk '{print $2}'`% </div> 10 Min      
            </div> 

              <div class="progress">
<div class="progress-bar progress-bar-warning" style="width:`/bin/cat /proc/loadavg | /usr/bin/awk '{print $3}'`%"> `/bin/cat /proc/loadavg | /usr/bin/awk '{print $3}'`% </div> 15 Min    
            </div> 



        
<div class="page-header"></div>  
<h4>Disk Space</h4>      

EOF
     

for i in `mount | grep "^/" | awk '{print $1}'`; do

echo "<div class="bs-component" align="center"><h6 id="progress-stacked"><p class="text-warning"> `df -h $i  | awk '{print $1}' | awk 'NR==2'` mounted on `df -h $i  | awk '{print $6}' | awk 'NR==2'` </p></h6>"
echo "<div class="progress">"

pr=`df -h $i  | awk '{print $5}' | awk 'NR==2'`

echo -e "<div class="progress-bar progress-bar-danger" style="width:"$pr"">$pr</div>`df -h $i  | awk '{print $2}' | awk 'NR==2'`"			
echo "</div>  </div>"         		
done	 



		lsblk -l | grep xvda 2>&1 > /dev/null
				ans=`echo $?`

						if [ $ans == 1 ]; then

cat << EOF
<div class="page-header"></div>  
<h4>Disk Read</h4>      

EOF
     

for j in `mount | grep "^/" | awk '{print $1}' | cut -d/ -f3`; do
mounted=`cat /etc/mtab | grep $j | awk '{print $2}'`
echo "<div class="bs-component" align="center"><h6 id="progress-stacked"><p class="text-warning"> `echo $j` mounted on $mounted </p></h6>"
echo "<div class="progress">"

pr=`iostat -m $j | grep $j | awk '{print $3}'`

echo -e "<div class="progress-bar progress-bar-warning" style="width:"$pr%""> $pr Mb/s </div> `iostat -m $j | grep $j | awk '{print $5}'`
Mb read "			
echo "</div>  </div>"         		
done		 

cat << EOF

 

<div class="page-header"></div>  
<h4>Disk Write</h4>      

EOF
     

for j in `mount | grep "^/" | awk '{print $1}' | cut -d/ -f3`; do
mounted=`cat /etc/mtab | grep $j | awk '{print $2}'`
echo "<div class="bs-component" align="center"><h6 id="progress-stacked"><p class="text-warning"> `echo $j` mounted on $mounted </p></h6>"
echo "<div class="progress">"

pr=`iostat -m $j | grep $j | awk '{print $4}'`

echo -e "<div class="progress-bar progress-bar-warning" style="width:"$pr%""> $pr Mb/s </div> `iostat -m $j | grep $j | awk '{print $6}'`
Mb read "			
echo "</div>  </div>"         		
done		 
	 
						else

cat << EOF
<div class="page-header"></div>  
<h4>Disk Read</h4>      

EOF


for j in `lsblk -l | awk '{print $7,$1}' | grep -v NAME | grep -v MOUNTPOINT | sed '/^\ /d' | awk '{print $2}'`; do

mount=`lsblk /dev/$j | awk '{print $7}' | grep -v NAME | grep -v MOUNTPOINT`
echo "<div class="bs-component" align="center"><h6 id="progress-stacked"><p class="text-warning"> `echo $j` mounted on $mount </p></h6>"
echo "<div class="progress">"

pr=`iostat $j | grep $j | awk '{print $3}'`

echo -e "<div class="progress-bar progress-bar-warning" style="width:"$pr%""> $pr Kb/s </div> `iostat -m $j | grep $j | awk '{print $5}'`
Mb read "
echo "</div>  </div>"
done             
     

cat << EOF
<div class="page-header"></div>  
<h4>Disk Write</h4>      

EOF


for j in `lsblk | awk '{print $1}' | grep -v NAME`; do
mount=`lsblk /dev/$j | awk '{print $7}' | grep -v NAME | grep -v MOUNTPOINT` 
echo "<div class="bs-component" align="center"><h6 id="progress-stacked"><p class="text-warning"> `echo $j` mounted on $mount</p></h6>"
echo "<div class="progress">"

pr=`iostat $j | grep $j | awk '{print $4}'`

echo -e "<div class="progress-bar progress-bar-warning" style="width:"$pr%""> $pr Kb/s </div>`iostat -m $j | grep $j | awk '{print $6}'`
Mb write "
echo "</div>  </div>"
done             
 

					fi

cat << EOF




 <div class="page-header"></div>  
<h4>Processes</h4>      

EOF
     
users=`ps aux | grep -v USER | awk '{print $1}' | sort | uniq`
total_process=`ps aux | wc -l`

get_process() {
for i in $users; do
echo "<div class="bs-component" align="center"><h6 id="progress-stacked"><p class="text-warning"> `echo $i | awk '{print $1}'` </p></h6>"
echo "<div class="progress">"
user_process=`ps aux | grep $i | wc -l`


a=`echo $total_process`
b=`echo $user_process`

percent=`echo "$b*100/$a" | bc`

echo -e "<div class="progress-bar progress-bar-warning" style="width:"$percent%""> $percent% </div> $b from $a
 "		
echo "</div>  </div>"         		
done		 

}

get_process


cat << EOF
  	  			  
<div class="page-header"></div>   

      <footer>
        <div class="row">
          <div class="col-lg-12">    
            <p>System: `uname -a`.  Made by <a href="https://github.com/caezsar" rel="nofollow">caezsar</a> </p> 
		</div>
        </div>

      </footer>
    </div>
  </body>
</html>


EOF
