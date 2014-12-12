#!/bin/bash


cat << EOF

                              <!-- FOOTER
================================================== -->                    	
                      	
  
                       </div><!--/row-->
                      
      <div class="list-group">
            <a  class="list-group-item active">
		<div align="center"><font size="1"><p>System: `uname -a`</p>		
		<p>$HTTP_USER_AGENT</p>
		<p>Information generated at: `date`</p></font></div>
			</a>
		
	</div><!-- /padding -->
	
	<!-- script references -->
		<script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.2/jquery.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/scripts.js"></script>
	</body>
</html>

EOF
                 	
                      	
