#!/bin/bash
echo ""


runlev=`/sbin/runlevel | awk '{print $2}'`
boot_serv=`ls /etc/rc"$runlev".d/ | grep S | cut -d"S" -f2 | cut -b 3-20 | sort`


./head.cgi

cat << EOF

                            <!-- BEGIN CONTENT PAGE
================================================== -->     
              
                <div class="padding">
                    <div class="full col-sm-9">
                      
                        <!-- content -->                      
                      	<div class="row">
                      	
                      	
                            <!-- CPU USAGE
================================================== -->                      	
                      	
                
              <div class="panel panel-default">
                  <div class="panel-heading"><h4> System Load <a class="text-danger"><h5>  </h5></a></h4></div>
                  <div class="panel-body">
                    
                    <small> <a class="text-success"> `/bin/cat /proc/loadavg | /usr/bin/awk '{print $1}'`% - 1min </a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow=" " aria-valuemin="0" aria-valuemax="100" style="width: `/bin/cat /proc/loadavg | /usr/bin/awk '{print $1}'`%">             
                      </div>
                    </div>


                    <small> <a class="text-danger">`/bin/cat /proc/loadavg | /usr/bin/awk '{print $2}'`% -  5 min </a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow=" " aria-valuemin="0" aria-valuemax="100" style="width: `/bin/cat /proc/loadavg | /usr/bin/awk '{print $2}'`%">
                      </div>
                    </div>

            
                    
            <small> <a class="text-info"> `/bin/cat /proc/loadavg | /usr/bin/awk '{print $3}'`%  - 15 min </a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow=" " aria-valuemin="0" aria-valuemax="100" style="width: `/bin/cat /proc/loadavg | /usr/bin/awk '{print $3}'`% ">     
                      </div>
                    </div>




            
                    
</div><!--/panel-body-->
</div><!--/panel-->                                  
</div><!--/col-->
 </div><!--/row-->

                            <!-- SECOND RAW 
================================================== -->  

  <div class="row">

        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">System Load - Raw output</a>
            <pre><strong><font color=#2D3C86> `uptime` </font></strong></pre>
        </div>
      </div>

      
         <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Boot Services: `ls /etc/rc"$runlev".d/ | grep S | wc -l` - Raw output</a>
            <pre><font color=#2D3C86 ><strong> $boot_serv </font></strong></pre>
        </div>
      </div> 


        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Installed Services - <strong> init.d </strong> - `ls -l /etc/init.d/ | grep x | wc -l` - Raw output</a>
            <pre><font color=#2D3C86 ><strong> `ls -l /etc/init.d/ | grep x | awk '{print $9}'` </font></strong></pre>
        </div>
      </div> 	  
EOF
        
./footer.cgi
