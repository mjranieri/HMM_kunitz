from Bio import SeqIO

def filter_common_sequences(file1, file2, output_file):
    # Read sequences from the first FASTA file
    sequences1 = set()
    with open(file1, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequences1.add(str(record.seq))

    # Read sequences from the second FASTA file and filter
    common_sequences = []
    with open(file2, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequence = str(record.seq)
            if sequence not in sequences1:
                common_sequences.append(record)

    # Write the common sequences to the output file
    with open(output_file, "w") as handle:
        SeqIO.write(common_sequences, handle, "fasta")

file1 = "uniprot_ids.fasta" 
file2 = "kunitz_all.fasta"  
output_file = "kunitz_all_clean.fasta"  

filter_common_sequences(file1, file2, output_file)
