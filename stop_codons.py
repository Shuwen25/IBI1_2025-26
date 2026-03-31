#define the DNA sequence encoding the start codon and stop codons
start_codon_dna='ATG'
stop_codons_dna=['TAA','TAG','TGA']
#input/output the file name
input_fa='Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_fa='stop_genes.fa'
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

#store the results (key:gene name+DNA sequence encoding stop codons, value: complete DNA sequence)
result_data={}

#traverse headers and sequences of each gene
for header, dna_seq in fasta_data.items():
    # Extract gene name: the content before the first space in the header (standard format for yeast FASTA)
    gene_name=header.split()[0]
    seq_length=len(dna_seq)
    # Store the in-frame stop codons contained in this gene (deduplicate)
    gene_stop_codons=set()#create a list
    #1.find ATG
    start_position=[]
    for i in range(seq_length-2):
        if dna_seq[i:i+3]==start_codon_dna:
            start_position.append(i)
    # skip if ATG cannot be found
    if not start_position:
        continue
    #2.Starting from each start codon, search for in-frame stop codons by reading in triplets.
    for start_idx in start_position:
        for current_idx in range(start_idx,seq_length-2,3):
            current_triplet=dna_seq[current_idx:current_idx+3]
            if current_triplet in stop_codons_dna:
                gene_stop_codons.add(current_triplet)
    #3.Only retain genes containing at least one in-frame stop codon
    if gene_stop_codons:
        #splice new header line
        stop_codons_str=','.join(sorted(gene_stop_codons))
        new_header=f"{gene_name}({stop_codons_str})"
        result_data[new_header]=dna_seq

open_fil_2=open(output_fa,'w',encoding="utf-8")
for new_header, dna_seq in result_data.items():
    #write headers
    open_fil_2.write(f">{new_header}\n")
    #Wrap the sequence at 80 characters to avoid overly long single lines
    for i in range(0,len(dna_seq),80):
        open_fil_2.write(f"{dna_seq[i:i+80]}\n")
    