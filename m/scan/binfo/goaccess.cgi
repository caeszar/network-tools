#!/bin/bash
echo ""

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
            <a  class="list-group-item active">Apache Goaccess - HTML output</a>
            <a  class="list-group-item"> `cat ../log.html` </a>
        </div>
      </div>  

EOF
        
./footer.cgi
         	
                      	
