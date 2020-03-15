from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
my_seq=Seq("GCCATTGTAATGGAATTAGTGGGTAACCCAGGGTAAACCTACCACCCCAGCCACCTCAG",IUPAC.unambiguous_dna)

# my_seq[5]="G"
from Bio.Seq import MutableSeq

mutable_seq=MutableSeq("GCCATTGTAATGGAATTAGTGGGTAACCCAGGGTAAACCTACCACCCCAGCCACCTCAG",IUPAC.unambiguous_dna)
mutable_seq[5]="C"
mutable_seq.remove("T")

mutable_seq.reverse()

k=my_seq.count('G')
mut_newseq=my_seq.tomutable()
for i in range(k):
    mut_newseq.remove("G")
