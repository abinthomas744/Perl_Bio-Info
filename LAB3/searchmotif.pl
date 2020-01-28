#!/usr/bin/perl -w

print"Please type the filename of the protein sequence data:";
$proteinfilename=<STDIN>;
chomp $proteinfilename;
unless(open(PROTEINFILE,$proteinfilename))
{
	print"Cannot Open file\n$proteinfilename\n\n";
	exit
}

@protein=<PROTEINFILE>;

close PROTEINFILE;

$protein=join('',@protein);
$protein=~s/\s//g;
do
{
	print"Enter a motif to search for:";
	$motif=<STDIN>;


chomp $motif;

if ($protein=~ /$motif/)
{
	print"I found it\n\n";
}

else
{
	print"I Couldn\'t find it.\n\n";
}

}

until($motif=~/^\s*$/);

exit