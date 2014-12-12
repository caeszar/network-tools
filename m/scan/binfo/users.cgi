#!/bin/bash
echo ""

users_online() {
cat << EOF

   <table class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
		<th><a class="text-info"></a></th>
		<th><a class="text-info">User</a></th>
		<th><a class="text-info">TTY</a></th>
		<th><a class="text-info">Date</a></th>
		<th><a class="text-info">Hour</a></th>		
		<th><a class="text-info">From</a></th>		
      </tr>
    </thead>

EOF

echo "<tbody>"
echo "<tr bgcolor="#ffffff">"
./users_table
echo "  </table>"
echo "</section>"
}


last_logins() {
result=`last -i`
        while read -r line; do
        echo  "<table>"
        echo "<pre><font color=#2D3C86 ><strong> $line </font></strong>"
        done <<< "$result"               
	echo "</pre> </table>"
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
 
</div><!--/panel-body-->
</div><!--/panel-->                              
</div><!--/col-->

<div>

                            <!-- SECOND RAW 
================================================== -->  
    
       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Online Users - Raw output</a>
            `users_online`
        </div>
      </div>  
    
       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Last Logis - Raw output</a>
            <a  class="list-group-item"> `last_logins` </a>
        </div>
      </div>  


EOF
        
./footer.cgi
