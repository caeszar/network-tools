#!/bin/bash
echo ""

VHOST_PATTERN="tools.tecmint.com"
APACHE_ACCESS_LOG_FILE="/var/log/apache2/tools.tecmint.com-access.log"


bper=`/bin/cat 2>/dev/null $APACHE_ACCESS_LOG_FILE | /bin/grep -v "(internal dummy connection)" 2>/dev/null | head -1 | /usr/bin/awk '{print $4}' | /usr/bin/cut -d"[" -f2 2>/dev/null | /usr/bin/cut -d: -f1 2>/dev/null | sed 's/\//./g' 2>/dev/null`
fper=`/bin/cat 2>/dev/null $APACHE_ACCESS_LOG_FILE | /bin/grep -v "(internal dummy connection)" 2>/dev/null | tail -1 | /usr/bin/awk '{print $4}' | /usr/bin/cut -d"[" -f2 2>/dev/null | /usr/bin/cut -d: -f1 2>/dev/null | sed 's/\//./g' 2>/dev/null`
uniq=`cat $APACHE_ACCESS_LOG_FILE | /usr/bin/awk '{print $1}'| sort | uniq -c |wc -l`
hits=`/bin/cat $APACHE_ACCESS_LOG_FILE | grep -v "::1" | /usr/bin/awk '{print $1}' | sort | wc -l 2>/dev/null`

no_gzip_logs() {

cat << EOF
  <table class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
        <th><a class="text-info">Start Date</a></th>
        <th><a class="text-info">End Date</a></th>
        <th><a class="text-info">Uniq IP</a></th>
        <th><a class="text-info">Total Hits</a></th>
      </tr>
    </thead>
EOF

for i in `ls /var/log/apache2/ | grep $VHOST_PATTERN | grep -v error | grep -v gz`; do

start_date=`/bin/cat 2>/dev/null /var/log/apache2/$i | /bin/grep -v "(internal dummy connection)" 2>/dev/null | head -1 | /usr/bin/awk '{print $4}' | /usr/bin/cut -d"[" -f2 2>/dev/null | /usr/bin/cut -d: -f1`
end_date=`/bin/cat 2>/dev/null /var/log/apache2/$i | /bin/grep -v "(internal dummy connection)" 2>/dev/null | tail -1 | /usr/bin/awk '{print $4}' | /usr/bin/cut -d"[" -f2 2>/dev/null | /usr/bin/cut -d: -f1`
uniq_ip=`cat /var/log/apache2/$i | grep -v "internal dummy connection" | cut -d" " -f1 | sort -nr | uniq -c | wc -l`
hits=`/bin/cat /var/log/apache2/$i| grep -v "::1" | /usr/bin/awk '{print $1}' | sort | wc -l 2>/dev/null`

cat << EOF

    <tbody>
      <tr bgcolor="#ffffff">
        <td><h5><a class="text-success">$start_date</a><h5></td>
        <td><h5><a class="text-success">$end_date</a><h5></td>
        <td><h5><a class="text-success">$uniq_ip</a><h5></td>
        <td><h5><a class="text-success">$hits</a><h5></td>
      </tr>
   
    </tbody>

EOF

done
echo "  </table>"
echo "</section>"
}


gzip_logs() {

cat << EOF
  <table class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
        <th><a class="text-info">Start Date</a></th>
        <th><a class="text-info">End Date</a></th>
        <th><a class="text-info">Uniq IP</a></th>
        <th><a class="text-info">Total Hits</a></th>
      </tr>
    </thead>
EOF

for i in `ls /var/log/apache2/ | grep $VHOST_PATTERN | grep -v error | grep gz`; do

start_date=`/bin/zcat 2>/dev/null /var/log/apache2/$i | /bin/grep -v "(internal dummy connection)" 2>/dev/null | head -1 | /usr/bin/awk '{print $4}' | /usr/bin/cut -d"[" -f2 2>/dev/null | /usr/bin/cut -d: -f1`
end_date=`/bin/zcat 2>/dev/null /var/log/apache2/$i | /bin/grep -v "(internal dummy connection)" 2>/dev/null | tail -1 | /usr/bin/awk '{print $4}' | /usr/bin/cut -d"[" -f2 2>/dev/null | /usr/bin/cut -d: -f1`
uniq_ip=`zcat /var/log/apache2/$i | grep -v "internal dummy connection" | cut -d" " -f1 | sort -nr | uniq -c | wc -l`
hits=`/bin/zcat /var/log/apache2/$i| grep -v "::1" | /usr/bin/awk '{print $1}' | sort | wc -l 2>/dev/null`

cat << EOF

    <tbody>
      <tr bgcolor="#ffffff">
        <td><h5><a class="text-success">$start_date</a><h5></td>
        <td><h5><a class="text-success">$end_date</a><h5></td>
        <td><h5><a class="text-success">$uniq_ip</a><h5></td>
        <td><h5><a class="text-success">$hits</a><h5></td>
      </tr>
   
    </tbody>

EOF

done
echo "  </table>"
echo "</section>"
}



total_gip() {
cd /var/log/apache2/
string=`ls | grep $VHOST_PATTERN | grep -v error | grep gz | xargs echo -n`
uniq_ip=`zcat $string 2> /dev/null | grep -v "internal dummy connection" | cut -d" " -f1 | sort -nr | uniq -c | wc -l`
echo $uniq_ip
}

total_ip() {
cd /var/log/apache2/
string=`ls | grep $VHOST_PATTERN | grep -v error | grep -v gz | xargs echo -n`
uniq_ip=`cat $string | grep -v "internal dummy connection" | cut -d" " -f1 | sort -nr | uniq -c | wc -l`
echo $uniq_ip
}

total_ips() {
echo "`total_gip` + `total_ip`" | bc
}


total_ghits() {
cd /var/log/apache2/

string=`ls | grep $VHOST_PATTERN | grep -v error | grep gz | xargs echo -n`
uniq_hits=`/bin/zcat 2> /dev/null /var/log/apache2/$string | grep -v "::1" | /usr/bin/awk '{print $1}' | sort | wc -l`
echo $uniq_hits
}

total_hits() {
cd /var/log/apache2/
string=`ls | grep $VHOST_PATTERN | grep -v error | grep -v gz | xargs echo -n`
uniq_hits=`/bin/cat /var/log/apache2/$string | grep -v "::1" | /usr/bin/awk '{print $1}' | sort | wc -l`
echo $uniq_hits
}

total_apache_hits() {
echo "`total_ghits` + `total_hits`" | bc
}


404_ips() {
cat $APACHE_ACCESS_LOG_FILE | grep 404 | awk '{print $1, $9, $7, $4}' | grep -v 200 | sed 's/\[/\ /g' | cut -d: -f1 | awk '{print $4, $1}' | uniq -c | sort -nr
}

404_ips_files() {
cat $APACHE_ACCESS_LOG_FILE | grep 404 | awk '{print $1, $9, $7, $4}' | grep -v 200 | sed 's/\[/\   /g' | cut -d: -f1 | awk '{print $4, $1, $3}' | uniq -c | sort -nr
 }
 
 

./head.cgi

cat << EOF

                            <!-- BEGIN CONTENT PAGE
================================================== -->     
              
                <div class="padding">
                    <div class="full col-sm-9">
                      
                        <!-- content -->                      
                      	<div class="row">
                      	
                      	
                            <!-- MEMORY RAM 
================================================== -->                      	
                      	
                
      
                  <div class="panel-body">
				
               
</div><!--/panel-body-->
</div><!--/panel-->                              
</div><!--/col-->

<div>

                            <!-- SECOND RAW 
================================================== -->  

	  
       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Apache Stats</a>
            <a  class="list-group-item"> $bper - $fper </a>
			<a  class="list-group-item"> Visitors:`echo $uniq 2>/dev/null` </a>
			<a  class="list-group-item">Total Hits: `echo $hits 2>/dev/null` </a>
			<a  class="list-group-item">Total Server IPs: `total_ips` </a>
			<a  class="list-group-item">Total Server Hits: `total_apache_hits` </a>
			<a  class="list-group-item">Apache Logs Usage: `du -sh /var/log/apache2/ 2> /dev/null | awk '{print $1}' 2> /dev/null` </a>
			<a  class="list-group-item"> Total Logs Usage: `du -sh /var/log/ 2> /dev/null | awk '{print $1}' 2> /dev/null` </a>
        </div>
      </div>  
     
        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Apache Log Stats - Current Log</a>
         `no_gzip_logs`
        </div>
      </div>

         <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Apache Archive Log Stats</a>
         `gzip_logs`
        </div>
      </div>

        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Apache Hack IPs - Current Log</a>
         <a  class="list-group-item"><pre><strong><font color=#2D3C86>`404_ips` </font></strong></pre></a>
        </div>
      </div>

        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Apache Hack IPs - Current Log</a>
         <a  class="list-group-item"><pre><strong><font color=#2D3C86>`404_ips_files` </font></strong></pre></a>
        </div>
      </div>	  
EOF
        
./footer.cgi
