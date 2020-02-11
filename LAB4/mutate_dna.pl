#!/usr/bin/perl -w

use strict; use warnings;

my$dna='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA';
my $i;
my $mutant;

srand(time|$$);
$mutant=mutate($dna);
print"\nMutate DNA:\n\n";
print"\nHere is the Original DNA:\n\n";
print"$dna\n\n";
print"\nHere is the Mutant DNA:\n\n";
print"$mutant\n";
print"\nHere are 10 more Successive Mutations:\n\n";

for($i=0;$i<10;++$i)
{
    $mutant=mutate($mutant);
    print"$mutant\n";
}
exit;

sub mutate
{
    my($dna)=@_;
    my(@nucleotides)=('A','C','G','T');
    my($position)=randomposition($dna);
    my($newbase)=randomnucleotide(@nucleotides);
    substr($dna,$position,1,$newbase);
    return $dna;

}

sub randomelement
{
    my(@array)=@_;
    return $array[rand@array];
}

sub randomnucleotide
{
    my(@nucleotides)=('A','C','G','T');
    return randomelement(@nucleotides);
}

sub randomposition
{
    my($string)=@_;
    return int(rand(length($string)));
}