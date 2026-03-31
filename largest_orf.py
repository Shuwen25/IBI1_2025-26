seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
#define the start codon and the stop codons
start_codon='AUG' 
stop_codons=['UAA','UAG','UGA']
#store all the valid ORF (key: the sequence of ORF, value: the length of ORF)
orf_dict={}
#traverse the sequence to find all the start codon 'AUG' 
seq_length=len(seq)
for start_idx in range(seq_length-2):
    #check if the triplet start from the current index is the start codon
    for current_idx in range(start_idx,seq_length-2,3):
        current_triplet=seq[current_idx:current_idx+3]
        #when the stop codon is found, cut the ORF sequence
        if current_triplet in stop_codons:
            orf_seq=seq[start_idx:current_idx+3]
            orf_length=len(orf_seq)
            orf_dict[orf_seq]=orf_length
            #break when the first stop codon is found
            break
#select the largest ORF
if orf_dict:
    largest_orf=max(orf_dict,key=orf_dict.get)
    largest_orf_len=orf_dict[largest_orf]
    #print the result
    print(f'the largest ORF sequence:{largest_orf}')
    print(f'length of the largest ORF sequence:{largest_orf_len}')
else:
    print("Valid ORF sequence cannot be found")