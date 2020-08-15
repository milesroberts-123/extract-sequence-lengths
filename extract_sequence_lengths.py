from Bio import SeqIO
import sys

#Create genome file for bedtools
print("Extracting chromosome lengths from %s ..." % str(sys.argv[1]))
ids = []
lengths = []
for rec in SeqIO.parse(str(sys.argv[1]), "fasta"):
	ids.append(rec.id)
	lengths.append(len(rec))

print("Writing lengths to %s ..." % sys.argv[2])
with open(sys.argv[2], "w") as f:
	for id, length in zip(ids, lengths):
		chrom = [id, str(length)]
		f.write("\t".join(chrom) + "\n")

	f.close()
print("Extraction complete.")
