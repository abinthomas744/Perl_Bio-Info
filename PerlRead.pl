#!/usr/bin/perl
$proteinfilename = 'NM_123.pep';
open(PROTEINFILE,$proteinfilename);
$protein=<PROTEINFILE>;
print "1st Line \n $protein \n";
$protein=<PROTEINFILE>;
print"2nd Line \n $protein \n";
close PROTEINFILE;
exit;