import matplotlib.pyplot as plt

start_codon_dna='ATG'
stop_codons_dna=['TAA','TAG','TGA']
input_fa='Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
pie_output=''# Pie Chart Output File Name (varies with the input stop codon)

#store the headers and corresponding complete sequence (key:header, value:complete DNA sequence)
fasta_data={}
current_header=''
current_seq=''
#read FASTA file and splice the sequences across several lines

open_fil=open(input_fa,'r',encoding='utf-8')
for line in open_fil:
    line=line.strip()#remove line breaks, spaces, and tabs at the beginning and end of lines
    if not line: #skip blank lines
        continue
    #identify header lines (starting with >)
    if line[0]=='>':
        #If the sequence for the current gene already exists, store it in the dictionary first.
        if current_header and current_seq:
            fasta_data[current_header]=current_seq
        # Update the current header and sequence (remove '>' from the header)
        current_header=line[1:]
        current_seq=''
    else:
        current_seq+=line
# Store the sequence of the last gene (no > at the end of the file, requiring separate handling)
if current_header and current_seq:
    fasta_data[current_header]=current_seq

# Get and validate user input
while True:
    user_stop = input("Enter stop codon to analyze (TAA/TAG/TGA only): ").strip().upper()
    if user_stop in stop_codons_dna:
        pie_output = f"{user_stop}_codon_frequency.png"
        break
    else:
        print(f"Invalid input! Please enter only one from {stop_codons_dna}, try again:")

# Store all valid codons upstream of the stop codon
all_codons = []

# Iterate through each gene
for header, dna_seq in fasta_data.items():
    seq_length = len(dna_seq)
    # Store all ORFs ending with the specified stop codon for this gene
    gene_orfs = {}
    # Find all start codon (ATG) positions
    start_positions = [i for i in range(seq_length - 2) if dna_seq[i:i+3] == start_codon_dna]
    if not start_positions:
        continue
    # Search for the specified stop codon from each start codon in triplets
    for start_idx in start_positions:
        for current_idx in range(start_idx, seq_length - 2, 3):
            current_triplet = dna_seq[current_idx:current_idx+3]
            if current_triplet == user_stop:
                # Extract ORF sequence (from start to stop, inclusive)
                orf_seq = dna_seq[start_idx:current_idx+3]
                gene_orfs[orf_seq] = len(orf_seq)
                break
    # Skip if no valid ORF found
    if not gene_orfs:
        continue
    # Find the longest ORF for this gene
    longest_orf = max(gene_orfs, key=gene_orfs.get)
    # Extract upstream codons: remove start (first 3) and stop (last 3) codons
    if len(longest_orf) >= 6:
        upstream_seq = longest_orf[3:-3]
        # Split into triplets and add to the list
        for i in range(0, len(upstream_seq), 3):
            codon = upstream_seq[i:i+3]
            if len(codon) == 3:
                all_codons.append(codon)

# Count codon frequency
codon_count = {}
for codon in all_codons:
    codon_count[codon] = codon_count.get(codon, 0) + 1

# Exit if no codons found
if not codon_count:
    print(f"No genes with in-frame {user_stop} stop codon found. Cannot calculate frequency.")
    exit()

# Print frequency results
print(f"Codon frequency upstream of stop codon {user_stop}:")
for codon, count in sorted(codon_count.items(), key=lambda x: x[1], reverse=True):
    percentage = (count / len(all_codons)) * 100
    print(f"{codon}: {count} times, {percentage:.2f}%")

# Prepare pie chart data
labels = list(codon_count.keys())
sizes = list(codon_count.values())
# Highlight the largest segment
explode = [0.1 if s == max(sizes) else 0 for s in sizes]

# Create plot
fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct='%1.2f%%',
    shadow=True,
    startangle=90,
    textprops={'fontsize': 10}
)

# Set title
ax.set_title(f'Frequency of In-frame Codons Upstream of {user_stop} Stop Codon', fontsize=16, pad=20)
ax.axis('equal')

# Save figure
plt.tight_layout()
plt.savefig(pie_output, dpi=300, bbox_inches='tight')
plt.close()

print(f"Pie chart saved as: {pie_output}")
