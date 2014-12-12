#!/bin/bash

top_mem() {
cat << EOF

   <table class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
		<th><a class="text-info"></a></th>
		<th><a class="text-info">Program</a></th>
		<th><a class="text-info">MEM Usage %</a></th>
		<th><a class="text-info">RSS Memory</a></th>
		<th><a class="text-info">PID</a></th>			
      </tr>
    </thead>

EOF

echo "<tbody>"
echo "<tr bgcolor="#ffffff">"
./ram_table
echo "  </table>"
echo "</section>"
}


top_ram=`ps -Ao pmem,rss,comm,pid --sort=-pmem | head -n 11`


used=`free -m | awk 'NR==3' | awk '{ printf $3}'`
total=`free -m | awk 'NR==2' | awk '{ printf $2}'`
all=`echo "$used*100/$total" | bc`

used1=`free -m | awk 'NR==3' | awk '{ printf $4}'`
total1=`free -m | awk 'NR==2' | awk '{ printf $2}'`
all1=`echo "$used1*100/$total1" | bc`


cat << EOF

                            <!-- BEGIN CONTENT PAGE
================================================== -->     
              
                <div class="padding">
                    <div class="full col-sm-9">
                      
                        <!-- content -->                      
                      	<div class="row">
                      	
                      	
                            <!-- MEMORY RAM 
================================================== -->                      	
                      	
                
              <div class="panel panel-default">
                  <div class="panel-heading"><h4>RAM Usage <a class="text-danger" >
		<p><h5> Total Available: `free -h | awk '/Mem/ { print $2 }'` </h5></p>
		<p><h5> Swap Usage: `free -h | grep Swap | awk '{print $3}'` from `free -h | grep Swap | awk '{print $2}'` </h5></p>
		</a></h4></div>
                  <div class="panel-body">
                    
                    <small> <a class="text-success">Free: `echo $all1%` - `free -h | grep "buffers/cache" | awk '{print $4}'`  </a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow=" " aria-valuemin="0" aria-valuemax="100" style="width: `echo $all1%`">         
                      </div>
                    </div>


                    <small><a class="text-danger"> Used: `echo $all%` - `free -h | grep "buffers/cache" | awk '{print $3}'` </a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="`echo $all%`" aria-valuemin="0" aria-valuemax="100" style="width: `echo $all%`">
                      </div>
                    </div>


               <small> <a class="text-warning">Cached: `free -m | awk '/Mem/ { printf("%3.1f%%", $7/$2*100) }'` - `free -h | awk '/Mem/ { print $7 }'`</a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: `free -m | awk '/Mem/ { printf("%3.1f%%", $7/$2*100) }'`">
                      </div>
                    </div>    
            
                    
            <small><a class="text-info"> Bufferd: `free -m | awk '/Mem/ { printf("%3.1f%%", $6/$2*100) }'` - `free -h | awk '/Mem/ { print $6 }'`</a></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-disabled" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: `free -m | awk '/Mem/ { printf("%3.1f%%", $6/$2*100) }'`">               
                      </div>
                    </div>


                    <small><a class="text-info"> Shared: `free -m | awk '/Mem/ { printf("%3.1f%%", $5/$2*100) }'` - `free -h | awk '/Mem/ { print $5 }'`</p></small>
                    <div class="progress">
                      <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: `free -m | awk '/Mem/ { printf("%3.1f%%", $5/$2*100) }'`">
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
            <a  class="list-group-item active">Top 20 RAM Usage</a>
				`top_mem`
        </div>
      </div>
	  
        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Top 10 Memory - Raw output</a>
            <pre><strong><font color=#2D3C86> $top_ram </font></strong></pre>
        </div>
      </div>
     
        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">RAM - Raw output</a>
            <a  class="list-group-item"><pre><strong><font color=#2D3C86> `free -h` </font></strong></pre></a>
  

        </div>
      </div>

EOF
