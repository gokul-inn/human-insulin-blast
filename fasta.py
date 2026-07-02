from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
#reading the fasta file using biopython library
record=SeqIO.read("humaninsulin.fasta","fasta")
print(record.id)
print(record.name)
#the fasta is taken as dna sequence 
dna=record.seq
print("the DNA is",dna)
#the g and c count is taken and gc perecnt is found
g_count=dna.count("G")
C_count=dna.count("C")
gc_count= g_count + C_count
total_nucleotide=len(dna)
gc_percent= (gc_count/total_nucleotide)*100
print("the GC percent is",round(gc_percent,2))
#the dna sequence is transcribed to rna and rna is translated to protein
rna=dna.transcribe()
protein=rna.translate()
print("the RNA is",rna)
print("the PROTEIN is",protein)
protein_length=len(protein)
print("the lenght of the protein",protein_length)
#the lenght of the protein is found and and min sequence is rejected
min=90
min_percent=45
if protein_length<min:
    print("the protein doesnt have required lenght")
elif protein_length<min_percent:
    print(" the gc perecnt is less")
else:
    print("the protein have required length and gc perecnt")
# using the blast the similar protein are found and taken in xml form.in this the blastp programm is taken
result=NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence=str(protein)
)
with open("blast_record03.xml","w")as b:
    b.write(result.read())
print("blast is successful")
#once the blast program is succesful the result is readed and the no of similar proteins is found
with open("blast_record03.xml")as b:
    blast_record02=NCBIXML.read(b)
print("the no.of.similar sequence",len(blast_record02.alignments))
#the first alignment is readed and file is taken and in that the each hsp can be taken
first_alignments = blast_record02.alignments[0]
print("the most similar protein sequence",first_alignments)
#the score,expect,subject,match are found
first_hsps=first_alignments.hsps[0]
print("the score of the first similar protein",first_hsps.score)
print("the expect value of the first similar protein",first_hsps.expect)
print("the subject of the first similar protein",first_hsps.sbjct)
print("the match for the similar protein",first_hsps.match)