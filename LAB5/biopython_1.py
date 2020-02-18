import Bio.Alphabet
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq

pro_letter=Bio.Alphabet.ThreeLetterProtein.letters;
print(pro_letter);
print("\n");

pro_iupac=IUPAC.IUPACProtein.letters;
print(pro_iupac);
print("\n");

pro_unamb_iupac=IUPAC.unambiguous_dna.letters;
print(pro_unamb_iupac);
print("\n");

pro_amb_iupac=IUPAC.ambiguous_dna.letters;
print(pro_amb_iupac);
print("\n");

pro_extend_letter=IUPAC.ExtendedIUPACProtein.letters;
print(pro_extend_letter);
print("\n");    