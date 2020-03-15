from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
my_seq=Seq("GCCATTGTAATGGAATTAGTGGGTAACCCAGGGTAAACCTACCACCCCAGCCACCTCAG",IUPAC.unambiguous_dna)

#my_seq[5]="G" This line won't work becuase the object(Seq) is immutable
from Bio.Seq import MutableSeq

mutable_seq=MutableSeq("GCCATTGTAATGGAATTAGTGGGTAACCCAGGGTAAACCTACCACCCCAGCCACCTCAG",IUPAC.unambiguous_dna)
mutable_seq[5]="C"
mutable_seq.remove("T")

mutable_seq.reverse()

k=my_seq.count('G')
mut_newseq=my_seq.tomutable()
for i in range(k):
    mut_newseq.remove("G")

my_seq=Seq("AGCTTCCATTTGGGTCATGATCC")

print(my_seq.complement());
my_seq.count("T")

GC_count=100*float(my_seq.count("G"))+my_seq.count("C")/len(my_seq);
print(GC_count);


#Slicing a sequence
my_seq1=Seq("GATTATTTCCCCGCGCCCAGTCAAGGTAGTGCCATAACCGTCCCTG",IUPAC.unambiguous_dna);
print(my_seq1[4:12]);

print(my_seq[0::3]);
print(my_seq[1::3]);
print(my_seq[2::3]);
print(my_seq[::-1]);

#Concatenation
protein_seq=Seq("EVRNAK",IUPAC.protein);
dna_seq=Seq("ACGT",IUPAC.unambiguous_dna);
#print(protein_seq+dna_seq);

from Bio.Alphabet import generic_alphabet;
protein_seq.alphabet=generic_alphabet;
dna_seq.alphabet=generic_alphabet;
print(protein_seq+dna_seq);

from Bio.Alphabet import generic_nucleotide
nuc_seq=Seq("GATCGATGC",generic_nucleotide);
dna_seq=Seq("ACGT",IUPAC.unambiguous_dna);
print(nuc_seq+dna_seq);

from Bio.Alphabet import generic_dna
list_of_seqs=[Seq("ACGT",generic_dna),Seq("AACC",generic_dna),Seq("GGTT",generic_dna)]

concatenated=Seq("",generic_dna)
for s in list_of_seqs:
    concatenated+=s 
    print(concatenated);