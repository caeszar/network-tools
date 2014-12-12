#!/bin/bash
echo ""

top_cpu=`ps -Ao pcpu,comm,pmem,pid --sort=-pcpu | head -n 11`

top_proc() {
cat << EOF

   <table class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
		<th><a class="text-info"></a></th>
		<th><a class="text-info">Program</a></th>
		<th><a class="text-info">CPU Usage %</a></th>
		<th><a class="text-info">CPU Memory</a></th>
		<th><a class="text-info">PID</a></th>		
      </tr>
    </thead>

EOF

echo "<tbody>"
echo "<tr bgcolor="#ffffff">"
./cpu_table
echo "  </table>"
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
                      	
                      	
                            <!-- CPU USAGE
================================================== -->                      	
                      	
                
              <div class="panel panel-default">
                  <div class="panel-heading"><h4>CPU Usage <a class="text-danger" >
		<p><h5> Model: `cat /proc/cpuinfo | grep "model name" | cut -d: -f2 | head -1` with `nproc` cores </h5></p>
		
		</a></h4></div>
                  <div class="panel-body">
                    
                    <small> <a class="text-success"> `iostat | awk 'NR==4' | awk '{ printf $6}'`% Idle </a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow=" " aria-valuemin="0" aria-valuemax="100" style="width: `iostat | awk 'NR==4' | awk '{ printf $6}'`%">
                      </div>
                    </div>


                    <small> <a class="text-danger"> `iostat | awk 'NR==4' | awk '{ printf $1}'`% User </a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow=" " aria-valuemin="0" aria-valuemax="100" style="width: `iostat | awk 'NR==4' | awk '{ printf $1}'`%">
                      </div>
                    </div>


               <small> <a class="text-warning"> `iostat | awk 'NR==4' | awk '{ printf $3}'`% System </a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow=" " aria-valuemin="0" aria-valuemax="100" style="width: `iostat | awk 'NR==4' | awk '{ printf $3}'`%">
                      </div>
                    </div>    
            
                    
            <small> <a class="text-info"> `iostat | awk 'NR==4' | awk '{ printf $4}'`% Iowait </a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow=" " aria-valuemin="0" aria-valuemax="100" style="width: `iostat | awk 'NR==4' | awk '{ printf $4}'`%">         
                      </div>
                    </div>

            <small> <a class="text-info"> `iostat | awk 'NR==4' | awk '{ printf $2}'`% Nice </a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-disabled" role="progressbar" aria-valuenow=" " aria-valuemin="0" aria-valuemax="100" style="width: `iostat | awk 'NR==4' | awk '{ printf $2}'`%">         
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
            <a  class="list-group-item active">Top 10 CPU Usage</a>
				`top_proc`
        </div>
      </div>
     
  
       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Top 10 CPU - Raw output</a>
            <pre><strong><font color=#2D3C86> $top_cpu </font></strong></pre>
        </div>
      </div>
     
        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">CPU Usage - Raw output</a>
            <a  class="list-group-item"><pre><strong><font color=#2D3C86>  `iostat -c` </font></strong></pre></a>
        </div>
      </div>
      
      
        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">CPU Info - Raw output</a>
            <a  class="list-group-item"><pre><strong><font color=#2D3C86> `lscpu` </font></strong></pre></a>
        </div>
      </div>

EOF
        
./footer.cgi
