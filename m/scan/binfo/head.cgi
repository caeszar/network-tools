#!/bin/bash

runlev=`/sbin/runlevel | awk '{print $2}'`



cat << EOF
<!DOCTYPE html>
<html lang="en">

                              <!-- HEAD
================================================== -->   

	<head>
		<meta http-equiv="content-type" content="text/html; charset=UTF-8">
		<meta charset="utf-8">
		<title>System Information for `hostname -f` </title>
		<meta name="generator" content="Bootply" />
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<!--[if lt IE 9]>
			<script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
		<![endif]-->
		<link href="css/styles.css" rel="stylesheet">
		<link rel="stylesheet" type="text/css" href="css/icons.css" />
		
		<script type="text/javascript" src="js/paging.js"></script>
		<script type="text/javascript" src="js/paging1.js"></script>		
	</head>

                              <!-- BODY
================================================== -->   

	<body>
<div class="wrapper">
    <div class="box">
        <div class="row row-offcanvas row-offcanvas-left">
                      
          
            <!-- sidebar -->
            <div class="column col-sm-2 col-xs-1 sidebar-offcanvas" id="sidebar">


              
                                <!-- RIGHT VERTICAL MENU
===================================================================================================================== -->       
               
                <ul class="nav hidden-xs" id="lg-menu">
				<li><a class="metro" href="./index.cgi"><span class="icon-power"></span> RAM Usage </a></li>				
				<li><a class="metro" href="./load.cgi"><span class="icon-loading"></span> System Load </a></li>	
				<li><a class="metro" href="./cpu.cgi"><span class="icon-busy"></span> CPU Usage </a></li>
				<li><a class="metro" href="./disk.cgi"><span class="icon-laptop"></span> Disk Usage </a></li>			   
				<li><a class="metro" href="./diskstat.cgi"><span class="icon-bars"></span> Disk Stats </a></li>	
				<li><a class="metro" href="./net.cgi"><span class="icon-broadcast"></span> Network </a></li>	
				<li><a class="metro" href="./process.cgi"><span class="icon-spin"></span> Processes </a></li>	
				<li><a class="metro" href="./users.cgi"><span class="icon-user"></span> Users </a></li>	
                <li><a class="metro" href="./a-logs.cgi"><span class="icon-wordpress"></span> Apache </a></li>	
                </ul>



                <ul class="list-unstyled hidden-xs" id="sidebar-footer">
                    <li>
		       <h6> Runlevel: `/sbin/runlevel` </h6>
               <h6> Uptime: `uptime | cut -d"p" -f2|cut -d"," -f1`</h6> 
			   <h6> `who -b` </h6>
			   <h6> Boot Services: `ls /etc/rc"$runlev".d/ | grep S | wc -l` / `ls /etc/rc"$runlev".d/ | grep -v README | wc -l`  </h6>		
                    </li>
                </ul>                          
            </div>


                                     <!-- NAVIGATION BAR BLUE
========================================================================================================================== -->      


            <div class="column col-sm-10 col-xs-11" id="main">
                
                <!-- top nav -->
              	<div class="navbar navbar-blue navbar-static-top">  
                    <div class="navbar-header">
                      <button class="navbar-toggle" type="button" data-toggle="collapse" data-target=".navbar-collapse">
                        <span class="sr-only">Toggle</span>
                        <span class="icon-bar"></span>
          				<span class="icon-bar"></span>
          				<span class="icon-bar"></span>
                      </button>
                  
                  	</div>
                  	<nav class="collapse navbar-collapse" role="navigation">
                   
                   
                   
              
                   
                    <ul class="nav navbar-nav">
 
		     <li>
                        <a class="metro" ><span class="badge"><span  class="icon-tux">  `cat /etc/issue.net` </span></span></a>
                      </li>
		     <li>
                        <a><span class="badge"> `uname -sr` </span></a>
                      </li>
                      <li>
                        <a href="http://`hostname -f`"> @ `hostname -f`</a>
                      </li>
                     <li>
                        <a href="http://`echo $SERVER_ADDR`"># `echo $SERVER_ADDR` </a>
                      </li>
              <li class="dropdown">
                        <a href="#" class="metro" class="dropdown-toggle" data-toggle="dropdown"><span class="icon-plus-2"></span> Menu </a>
                        <ul class="dropdown-menu">
                          <li><a href="./apache.cgi">Apache Env</a></li>
						  <li><a href="./a-logs.cgi">Apache Log</a></li>
						  <li><a href="./goaccess.cgi">Goaccess</a></li>
						  <li><a href="./logwatch.cgi">Logwatch </a></li>
						 
                        </ul>
                      </li>             
                      <li>
                        <a href="http://`echo $REMOTE_ADDR`"><span class="badge"> `echo $REMOTE_ADDR` </span></a>
                      </li>
 

                    </ul>

                              <!-- NAV BAR BLUE RIGHT ITEMS
================================================== -->   

                    <ul class="nav navbar-nav navbar-right">
				
                      <li class="dropdown">
					 
                        <a href="#" class="metro" class="dropdown-toggle" data-toggle="dropdown"><span class="icon-arrow-down"></span></a>
                        <ul class="dropdown-menu">
						 
                          <li><a href="apache.cgi">Apache Environment</a></li>
						  <li><a target=_blank href="../webalizer/index.html">Webalizer </a></li>
						  <li><a target=_blank href="../sysinfo/">Graphics </a></li>
						  <li><a target=_blank href="../info/">Dash info </a></li>
						  <li><a target=_blank href="../logwatch.cgi">Logwatch </a></li>
						  <li><a target=_blank href="../logs.cgi">Logs Goaccess</a></li>
                        </ul>
                      </li>
					  
					   <li class="dropdown">
                        <a target="_blank" href="https://github.com/caezsar" class="metro"><span class="icon-github"></span></a>
                      </li>
					  
                    </ul>
                  	</nav>
                </div>

                <!-- /top nav -->
      
 
EOF
