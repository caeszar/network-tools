#!/usr/bin/perl -wT
    use CGI qw(:standard);
    use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
    use strict;
    use Socket;

    print header;
    print start_html("Remote Host");

    my $hostname = gethostbyaddr(inet_aton($ENV{REMOTE_ADDR}), AF_INET);
    print "$hostname";

    print end_html;


