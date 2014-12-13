#!/bin/bash
echo ""

### START TABLE FUNCTION ###
process() {
cat << EOF

   <table id="results" class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
		<th><a class="text-info"></a></th>
		<th><a class="text-info">User</a></th>
		<th><a class="text-info">Pid</a></th>
		<th><a class="text-info">CPU%</a></th>	
		<th><a class="text-info">MEM%</a></th>		
		<th><a class="text-info">RSS</a></th>	
		<th><a class="text-info">TTY</a></th>	
		<th><a class="text-info">Stat</a></th>	
		<th><a class="text-info">Command</a></th>	
      </tr>
    </thead>

EOF
##Start table with data##
echo "<tbody>"
echo "<tr bgcolor="#ffffff">"

##Get rest of table from awk script###
./ptable

##Finish table###
echo "  </table>"

##Put pagination##
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
### END TABLES FUNCTION ###


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
                  <div class="panel-heading"><h4> Total Processess Started: `ps aux | wc -l` </h4></div>
                  <div class="panel-body">
     

EOF
     

users=`ps aux | grep -v USER | awk '{print $1}' | sort | uniq`
total_process=`ps aux | wc -l`

get_process() {
for i in $users; do
echo "<div align="right"><h6 id="progress-stacked"><p class="text-info"> `echo $i | awk '{print $1}'` </p></h6>"
echo "<div class="progress">"
user_process=`ps aux | grep $i | wc -l`


a=`echo $total_process`
b=`echo $user_process`

percent=`echo "$b*100/$a" | bc`

echo -e "<div class="progress-bar" style="width:"$percent%""><font color=#464646> $percent% </font></div><p class="text-danger"> $b </p>
 "		
echo "</div>  </div>"         		
done		 

}

## Activate Function
get_process


cat << EOF
           
</div><!--/panel-body-->
</div><!--/panel-->                                  
</div><!--/col-->
 </div><!--/row-->
 
                            <!-- SECOND RAW 
================================================== -->  

  <div class="row">
    
        <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Processes Stats - Raw output</a>
           `process`
        </div>
      </div> 
 
EOF
        
./footer.cgi
