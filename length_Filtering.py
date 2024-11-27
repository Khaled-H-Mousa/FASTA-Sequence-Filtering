# Script to parse a FASTA file and filter sequences based on length

# Define input file: Path to the FASTA file
FastaFile = "/home/khaled/Documents/testme/sequence.fasta"

# Initialize a dictionary to store sequences
seqs = {}

# Parse the FASTA file and store sequences
with open(FastaFile) as f:
    header = ""  # Variable to store the current sequence header
    for line in f:
        line = line.strip()  # Remove leading and trailing whitespace
        if line.startswith(">"):  # Check if the line is a header (starts with ">")
            header = line  # Save the header
            seqs[header] = ""  # Initialize an empty sequence for this header
        else:
            seqs[header] += line  # Append the line to the current sequence

# Filter and print sequences with length greater than 80 amino acids
for h in seqs.keys():
    Seq_length = len(seqs[h])  # Calculate the length of the sequence
    if Seq_length > 80:  # Check if the sequence length is greater than 80
        print(f"{h}\n{seqs[h]}")
        # Uncomment below to include additional information about the sequence
        # print(f"ID: {h}")
        # print(f"Sequence: {seqs[h]}")
        # print(f"Length: {Seq_length}\n")

