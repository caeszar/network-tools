#!/bin/bash
echo ""

ip_conf() {

cat << EOF
  <table class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
        <th><a class="text-info">Interface</a></th>
        <th><a class="text-info">IP</a></th>
        <th><a class="text-info">Up</a></th>
        <th><a class="text-info">Down</a></th>
      </tr>
    </thead>
EOF

for i in `/sbin/ifconfig -a | cut -d" " -f1`; do
int_name=`/sbin/ifconfig $i | /usr/bin/awk '{print $1}' | awk 'NR==1'`
int_ip=`/sbin/ifconfig $i | grep inet | /usr/bin/awk '{print $2}' | /usr/bin/cut -d: -f2`
down=`/sbin/ifconfig $i| grep "RX bytes" | head -1 | /usr/bin/awk '{print $3, $4}'| cut -d"(" -f2 | cut -d")" -f1 2>/dev/null`
up=`/sbin/ifconfig $i| grep "RX bytes" | head -1 | /usr/bin/awk '{print $7, $8}'| cut -d"(" -f2 | cut -d")" -f1 2>/dev/null`

cat << EOF

    <tbody>
      <tr bgcolor="#ffffff">
        <td><h6><font color=#2D3C86 ><strong> $int_name</font><h6></td>
        <td><h6><font color=#801395 ><strong>$int_ip</font><h6></td>
        <td><h6><font color=#801C30 ><strong>$up</font><h6></td>
        <td><h6><font color=#117121 ><strong>$down</font><h6></td>       
      </tr>
   
    </tbody>

EOF
done
echo "  </table>"
echo "</section>"
}


tcp_servers() {
cat << EOF

   <table id="results" class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
		<th><a class="text-info"></a></th>
		<th><a class="text-info">Protocol</a></th>
		<th><a class="text-info">Local Socket</a></th>	
		<th><a class="text-info">Remote Socket</a></th>		
      </tr>
    </thead>

EOF

echo "<tbody>"
echo "<tr bgcolor="#ffffff">"
./tcp_table
echo "</table>"

cat << EOF
<div id="pageNavPosition"></div>
    <script type="text/javascript"><!--
        var pager = new Pager('results', 8); 
        pager.init(); 
        pager.showPageNav('pager', 'pageNavPosition'); 
        pager.showPage(1);
    //--></script>
EOF
echo "</section>"
}


udp_servers() {
cat << EOF

   <table class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
		<th><a class="text-info"></a></th>
		<th><a class="text-info">Protocol</a></th>
		<th><a class="text-info">Local Socket</a></th>	
		<th><a class="text-info">Remote Socket</a></th>		
      </tr>
    </thead>

EOF

echo "<tbody>"
echo "<tr bgcolor="#ffffff">"
./udp_table
echo "  </table>"
echo "</section>"
}


net_conn() {
cat << EOF

   <table id="results1" class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
		<th><a class="text-info"></a></th>
		<th><a class="text-info">Nr</a></th>
		<th><a class="text-info">Protocol</a></th>
		<th><a class="text-info">Local Socket</a></th>	
		<th><a class="text-info">Remote Socket</a></th>		
		<th><a class="text-info">State</a></th>	
      </tr>
    </thead>

EOF

echo "<tbody>"
echo "<tr bgcolor="#ffffff">"
./net_table
echo "</table>"

cat << EOF
<div id="pageNavPosition1"></div>
    <script type="text/javascript"><!--
        var pager1 = new Pager1('results1', 8); 
        pager1.init(); 
        pager1.showPageNav1('pager1', 'pageNavPosition1'); 
        pager1.showPage1(1);
    //--></script>
EOF

echo "</section>"
}

./head.cgi

cat << EOF

                            <!-- BEGIN CONTENT PAGE
================================================== -->     
              
                <div class="padding">
                    <div class="full col-sm-9">
                      
                        <!-- content -->                      
                      	<div class="row">
                      	                      
                            <!-- IP TABLES 
================================================== -->                      	

                  <div class="panel-body">
EOF
 
cat << EOF
                    
</div><!--/panel-body-->
</div><!--/panel-->                              
</div><!--/col-->

<div>
                            <!-- SECOND RAW 
================================================== -->  

        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Interface Table</a>
             `ip_conf` 
        </div>
      </div>

      
        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Servers - Table output</a>
             `tcp_servers` 
        </div>
      </div>

     
       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Connections - Table output</a>
            `net_conn`
        </div>
      </div>  


       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Traffic Info - Raw output</a>
            <a  class="list-group-item"><pre><strong><font color=#2D3C86> `vnstat` </font></strong></pre></a>
        </div>
      </div>

    
       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Network Interfaces - Raw output</a>
            <a  class="list-group-item"><pre><strong><font color=#2D3C86> `/sbin/ifconfig` </font></strong></pre></a>
        </div>
      </div>

       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Servers - Raw output</a>
            <a  class="list-group-item"><pre><strong><font color=#2D3C86> `netstat -tul` </font></strong></pre></a>
	
        </div>
      </div>	  
EOF
        
./footer.cgi
