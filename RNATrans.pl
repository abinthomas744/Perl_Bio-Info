#!/usr/bin/perl
$DNA='AGTAGTGTCCGGTCCAATAG';
print"DNA=$DNA\n";

$RNA=$DNA;
$RNA=~s/T/U/g;
print"RNA=$RNA\n";
exit

