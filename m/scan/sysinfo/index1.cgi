#!/bin/bash
echo "Content-type: text/html"

bper=`/bin/cat 2>/dev/null /var/log/apache2/tools.tecmint.com-access.log | /bin/grep -v "(internal dummy connection)" 2>/dev/null | head -1 | /usr/bin/awk '{print $4}' | /usr/bin/cut -d"[" -f2 2>/dev/null | /usr/bin/cut -d: -f1 2>/dev/null | sed 's/\//./g' 2>/dev/null`
fper=`/bin/cat 2>/dev/null /var/log/apache2/tools.tecmint.com-access.log | /bin/grep -v "(internal dummy connection)" 2>/dev/null | tail -1 | /usr/bin/awk '{print $4}' | /usr/bin/cut -d"[" -f2 2>/dev/null | /usr/bin/cut -d: -f1 2>/dev/null | sed 's/\//./g' 2>/dev/null`
uniq=`cat /var/log/apache2/tools.tecmint.com-access.log | /usr/bin/awk '{print $1}'| sort | uniq -c |wc -l`
eth0_rx=`/sbin/ifconfig | grep "RX bytes" | head -1 | /usr/bin/awk '{print $3, $4}'| cut -d"(" -f2 | cut -d")" -f1`
eth0_tx=`/sbin/ifconfig | grep "RX bytes" | head -1 | /usr/bin/awk '{print $7, $8}'| cut -d"(" -f2 | cut -d")" -f1`


cat << EOF

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>System Info for `hostname -f` </title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/style.css">
    <script>

     var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-23019901-1']);
      _gaq.push(['_setDomainName', "bootswatch.com"]);
        _gaq.push(['_setAllowLinker', true]);
      _gaq.push(['_trackPageview']);

     (function() {
       var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
       ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
       var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
     })();

    </script>
	
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

            <li><a href="http://tools.tecmint.com/m/scan/info" target="_blank">Sysinfo</a></li>
    
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
            <div class="bs-component">
              <div class="alert alert-dismissable alert-warning">       
                <h4> `cat /etc/issue.net` </h4> 
                <p> `uname -a` with `nproc`  cores</p>
				`cat /proc/cmdline`
              </div>
            </div>
          </div>
        </div>
		
        <div class="row">
          <div class="col-lg-4">
            <div class="bs-component">
              <div class="alert alert-dismissable alert-warning">             
				<p> Uptime: <strong> `uptime | cut -d"p" -f2|cut -d"," -f1` </strong></p>
				<p> Reboot: <strong> `who -b` </p></strong>
				<p> Runlevel : <strong> `/sbin/runlevel` </strong></p>
				<p>Swap Usage: <strong> `free -m | awk '/Swap/ { printf("%3.1f%%", $3/$2*100) }'` from `free -h | grep Swap | awk '{print $2}'` </strong></p>
              </div>
            </div>
          </div>
		  
          <div class="col-lg-4">
            <div class="bs-component">
              <div class="alert alert-dismissable alert-warning">
                 <p> 1 Minute Load: <strong>`/bin/cat /proc/loadavg | /usr/bin/awk '{print $1}' 2>/dev/null` %</strong></p>
				  <p> 5 Minute Load: <strong>`/bin/cat /proc/loadavg | /usr/bin/awk '{print $2}' 2>/dev/null` %</strong></p>
				   <p> 15 Minute Load: <strong>`/bin/cat /proc/loadavg | /usr/bin/awk '{print $3}' 2>/dev/null` %</strong></p>
              	   <p> Total Process: <strong> `ps aux | wc -l` </strong><p>
				   <p> Total Process: <strong> `ls /etc/rc2.d/ | grep S | wc -l` / `ls /etc/rc2.d/ | grep -v README | wc -l` </strong></p>
			  </div>
            </div>
          </div>
		  
          <div class="col-lg-4">
            <div class="bs-component">
              <div class="alert alert-dismissable alert-warning">            
				<p> Apache Web Uniq Visitors: <strong> `echo $uniq 2>/dev/null` </strong></p>
				<p> Time: <strong> `echo $bper` - `echo $fper 2>/dev/null` </strong></p>
				 <p> IP : <a href="http://`echo $SERVER_ADDR`" ><strong>`echo $SERVER_ADDR` </strong></a></p>
				 <p><strong> RX: <span> `echo $eth0_rx 2>/dev/null` </span>&nbsp;&nbsp;|&nbsp;&nbsp; TX: <span> `echo $eth0_tx 2>/dev/null` </strong></p>
              </div>
            </div>
          </div>      		  
        </div>
		
	
  
	
<div class="page-header"></div>   
<h3>Ram Memory</h3>	
		  
             <div class="bs-component" align="center">
			<h6 id="progress-stacked"><p class="text-warning"> RAM BAR - Used, Shared, Buffered, Cached, Free </p></h6>
              <div class="progress">
                <div class="progress-bar progress-bar-success" style="width:`free -m | awk '/Mem/ { printf("%3.1f%%", $3/$2*100) }'`"> `free -m | awk '/Mem/ { printf("%3.1f%%", $3/$2*100) }'` </div>
                <div class="progress-bar progress-bar-info" style="width:`free -m | awk '/Mem/ { printf("%3.1f%%", $5/$2*100) }'`"> `free -m | awk '/Mem/ { printf("%3.1f%%", $5/$2*100) }'` </div>
                <div class="progress-bar progress-bar-warning" style="width:`free -m | awk '/Mem/ { printf("%3.1f%%", $6/$2*100) }'`"> `free -m | awk '/Mem/ { printf("%3.1f%%", $6/$2*100) }'` </div>
                <div class="progress-bar progress-bar-danger" style="width: `free -m | awk '/Mem/ { printf("%3.1f%%", $7/$2*100) }'`"> `free -m | awk '/Mem/ { printf("%3.1f%%", $7/$2*100) }'` </div>				
             `free -m | awk '/Mem/ { printf("%3.1f%%", $4/$2*100) }'` / `free -m | awk '/Mem/ { print $2 }'`
			  </div>
            </div> 
			
            <div class="panel panel-warning">
                <div class="panel-heading">
                  <h3 class="panel-title">RAM - Raw Format</h3>
                </div>
                <pre>`free -h` </pre>
              </div>
         
<div class="page-header"></div>  
<h3>Disk Space</h3>      

EOF
     

for i in ` mount | grep "^/" | awk '{print $3}'`; do

echo "<div class="bs-component" align="center"><h6 id="progress-stacked"><p class="text-warning"> `df -h $i  | awk '{print $1}' | awk 'NR==2'` mounted on `df -h $i  | awk '{print $6}' | awk 'NR==2'` </p></h6>"
echo "<div class="progress">"

pr=`df -h $i  | awk '{print $5}' | awk 'NR==2'`

echo -e "<div class="progress-bar progress-bar-danger" style="width:"$pr"">$pr</div>`df -h $i  | awk '{print $2}' | awk 'NR==2'`"			
echo "</div>  </div>"         		
done	 

cat << EOF
              <div class="panel panel-warning">
                <div class="panel-heading">
                  <h3 class="panel-title">Disk Space - Raw Format</h3>
                </div>
                <pre>`df -h` </pre>
              </div>
	
             <div class="panel panel-warning">
                <div class="panel-heading">
                  <h3 class="panel-title">I/O Stat - Raw Format</h3>
                </div>
                <pre> `iostat -hm 2>/dev/null` </pre>
              </div>
	
<div class="page-header"></div>   
<h3>Network</h3>

             <div class="panel panel-warning">
                <div class="panel-heading">
                  <h3 class="panel-title">Servers - Raw Format</h3>
                </div>
                <pre>`netstat -tuln`  </pre>
              </div>
			  
             <div class="panel panel-warning">
                <div class="panel-heading">
                  <h3 class="panel-title">Traffic - Raw Format</h3>
                </div>
                <pre>`vnstat -i eth0` </pre>
              </div>

             <div class="panel panel-warning">
                <div class="panel-heading">
                  <h3 class="panel-title">Open Sockets</h3>
                </div>
                <pre>`netstat -tun`  </pre>
              </div>
			  
			  <div class="panel panel-warning">
                <div class="panel-heading">
                  <h3 class="panel-title">Interfaces - Raw</h3>
                </div>
                <pre>`/sbin/ifconfig` </pre>
              </div>
			  			  
<div class="page-header"></div>   
<h3>Users</h3>

             <div class="panel panel-warning">
                <div class="panel-heading">
                  <h3 class="panel-title">Online Users</h3>
                </div>
                <pre> `w -s` </pre>
              </div>
			  
			  <div class="panel panel-warning">
                <div class="panel-heading">
                  <h3 class="panel-title">Last Logins - Raw</h3>
                </div>
                <pre>`last -i` </pre>
              </div>
			  
<div class="page-header"></div>   
<h3>Processes</h3>

			<div class="panel panel-warning">
                <div class="panel-heading">
                  <h3 class="panel-title">Boot Services - Raw Format</h3>
                </div>
				<span id="os-hostname"> <pre> `ls /etc/rc2.d/ | grep S | cut -d"S" -f2 | cut -b 3-20 | sort` </pre></span>			
            </div>
			
             <div class="panel panel-warning">
                <div class="panel-heading">
                  <h3 class="panel-title">All process</h3>
                </div>
                <pre> `ps aux` </pre>
              </div>

      <footer>
        <div class="row">
          <div class="col-lg-12">    
            <p>Based on <a href="http://getbootstrap.com" rel="nofollow">Bootstrap</a>. Icons from <a href="http://fortawesome.github.io/Font-Awesome/" rel="nofollow">Font Awesome</a>. Web fonts from <a href="http://www.google.com/webfonts" rel="nofollow">Google</a>.</p>
            <a href="http://builtwithbootstrap.com/" target="_blank">Built With Bootstrap</a>
            <a href="https://wrapbootstrap.com/?ref=bsw" target="_blank">WrapBootstrap</a>
		</div>
        </div>

      </footer>
    </div>

    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
 
  </body>
</html>


EOF
