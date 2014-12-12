#!/bin/bash
echo ""

disk_iostat() {
for j in `cat /proc/partitions | grep -v name | awk '{print $4}'`; do
iostat -md $j | grep $j
done
}


disk_read() {

for j in `cat /proc/partitions | grep -v name | awk '{print $4}'`; do
pr=`iostat -d $j | grep $j | awk '{print $3}'`
tps=`iostat -d $j | grep $j | awk '{print $2}'`
echo "<hr>"
echo "<div align="center"><h5 id="progress-stacked"><p class="text-info"><strong> $j </strong></p></h5>"
echo "<div align="left"><h5 id="progress-stacked"><p class="text-success"> $pr Kb/s </p></h5>"

echo "<a class="text-danger"> <h6>$tps <a class="text-info"> Transactions/s </a></h6></a>"

echo "<div class="progress"><div class="progress-bar progress-bar-warning" style="width:$tps%"> </div>"
echo "<p align="right" class="text-success" >`iostat -m $j | grep $j | awk '{print $5}'` Mb </p>"			
echo "</div></div></div>"         		
done
}

disk_write() {

for j in `cat /proc/partitions | grep -v name | awk '{print $4}'`; do
pr=`iostat -d $j | grep $j | awk '{print $4}'`
tps=`iostat -d $j | grep $j | awk '{print $2}'`
echo "<hr>"
echo "<div align="center"><h5 id="progress-stacked"><p class="text-danger"><strong> $j </strong></p></h5>"
echo "<div align="left"><h5 id="progress-stacked"><p class="text-success"> $pr Kb/s </p></h5>"

echo "<a class="text-danger"> <h6>$tps <a class="text-info"> Transactions/s </a></h6></a>"

echo "<div class="progress"><div class="progress-bar progress-bar-warning" style="width:$tps%"> </div>"
echo "<p align="right" class="text-info" >`iostat -m $j | grep $j | awk '{print $6}'` Mb </p>"			
echo "</div></div></div>"         		
done
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
                      	
                
              <div class="panel panel-default">
                  <div class="panel-heading"><h4> Disk Statistics </h4></div>
                  <div class="panel-body">
     

<h4>Disk Read</h4>      
`disk_read`

  
<hr>
	 
<h4>Disk Write</h4>      
`disk_write`
     
 
 
</div><!--/panel-body-->
</div><!--/panel-->                                  
</div><!--/col-->
 </div><!--/row-->



                            <!-- SECOND RAW 
================================================== -->  

  <div class="row">
  
      
 
     
        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Disk Stats - Raw output</a>
			<a  class="list-group-item"><pre><strong><font color=#2D3C86> `iostat -md` </font></strong></pre></a>
            <a  class="list-group-item"><pre><strong><font color=#2D3C86> `disk_iostat` </font></strong></pre></a> 
        </div>
      </div>
      
 
EOF
        
./footer.cgi
         	
                      	
