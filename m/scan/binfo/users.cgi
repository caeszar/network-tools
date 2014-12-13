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

local_users() {
cat << EOF

   <table id="results" class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
		<th><a class="text-info"></a></th>
		<th><a class="text-info">User</a></th>
		<th><a class="text-info">UUID</a></th>
		<th><a class="text-info">Home</a></th>
		<th><a class="text-info">Shell</a></th>		
      </tr>
    </thead>

EOF

echo "<tbody>"
echo "<tr bgcolor="#ffffff">"
./users
echo "  </table>"

cat << EOF
<div id="pageNavPosition"></div>   
    <script type="text/javascript"><!--
        var pager = new Pager('results', 10); 
        pager.init(); 
        pager.showPageNav('pager', 'pageNavPosition'); 
        pager.showPage(1);
    //--></script>
EOF

echo "</section>"
}

system_users() {
cat << EOF

   <table id="results1" class="table table-bordered">
    <thead>
      <tr bgcolor="#f4f4f4">
		<th><a class="text-info"></a></th>
		<th><a class="text-info">User</a></th>
		<th><a class="text-info">UUID</a></th>
		<th><a class="text-info">Home</a></th>
		<th><a class="text-info">Shell</a></th>		
      </tr>
    </thead>

EOF

echo "<tbody>"
echo "<tr bgcolor="#ffffff">"
./susers
echo "  </table>"

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
 
</div><!--/panel-body-->
</div><!--/panel-->                              
</div><!--/col-->

<div>

                            <!-- SECOND RAW 
================================================== -->  
    
       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Online Users - Table output</a>
            `users_online`
        </div>
      </div>  
    
       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active">Local Users - Table output</a>
            `local_users`
        </div>
      </div> 

       <div class="panel-body">
          <div class="list-group">
            <a  class="list-group-item active"> System Users - Table output</a>
            `system_users`
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
