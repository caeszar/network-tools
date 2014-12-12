#!/bin/bash
echo ""

disk_info() {
cat << EOF

   <table class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
		<th><a class="text-info"></a></th>
		<th><a class="text-info">Filesystem </a></th>
		<th><a class="text-info">Size </a></th>	
		<th><a class="text-info">Used </a></th>	
		<th><a class="text-info">Avail </a></th>	
		<th><a class="text-info">Use% </a></th>	
		<th><a class="text-info">Mounted on </a></th>			
      </tr>
    </thead>

EOF

echo "<tbody>"
echo "<tr bgcolor="#ffffff">"
./fs_table
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
                      	
                      	
                            <!-- MEMORY RAM 
================================================== -->                      	

              <div class="panel panel-default">
                  <div class="panel-heading"><h4> Disk Usage </h4></div>
                  <div class="panel-body">

EOF

for i in `df -h | grep "^/" | awk '{print $6}'`; do

echo "<div><h5><p class="text-danger"> `df -h $i  | awk '{print $1}' | awk 'NR==2'` </p></h5>"
echo "<div class="progress">"

pr=`df -h $i  | awk '{print $5}' | awk 'NR==2'`

echo -e "<div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow=" " aria-valuemin="0" aria-valuemax="100"  style="width:$pr">$pr</div> <p class="text-info" >  `df -h $i  | awk '{print $2}' | awk 'NR==2'` </p>"			
echo "</div>  </div> "         		
done	 

cat << EOF
           
</div><!--/panel-body-->
</div><!--/panel-->                              
</div><!--/col-->

</div><!--/row-->
<div>

                            <!-- SECOND RAW 
================================================== -->  
     
        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Disk Table</a>
             `disk_info` 
        </div>
      </div>

      
       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Disk Space - Raw output</a>
            <a  class="list-group-item"><pre><strong><font color=#2D3C86> `df -h` </font></strong></pre></a>
        </div>
      </div>

     
       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Mount - Raw output</a>
            <a  class="list-group-item"><pre><strong><font color=#2D3C86> `mount` </font></strong></pre></a>
        </div>
      </div>     



       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Disk - Raw output</a>
            <a  class="list-group-item"><pre><strong><font color=#2D3C86> `lsblk` </font></strong></pre></a>
        </div>
      </div>         

EOF
        
./footer.cgi