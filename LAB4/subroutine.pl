#!/usr/bin/perl -w

$dna='CGACGTCTTCTCAGGCGA';

$longer_dna= addAGCT($dna);

print"I added AGCT to $dna and got $longer_dna\n\n";

exit;

sub addAGCT
{
	my($dna)=@_;
	$dna.='AGCT';
	return $dna;
}

