# 1. 读取 codon.txt 文件并创建密码子字典 codon_dict
codon_dict = {}
with open("codon.txt", "r") as codon_file:
    for line in codon_file:
        codon, amino_acid = line.strip().split()
        codon_dict[codon] = amino_acid
codon_dict["stop"] = "*"  # 添加终止密码子

# 2. 定义 transcript 函数，将 DNA 转录为 mRNA
def transcript(dna_sequence):
    return dna_sequence.replace("T", "U")

# 3. 定义 translate 函数，将 DNA 转录为 mRNA，然后翻译为氨基酸序列
def translate(dna_sequence):
    mrna_sequence = transcript(dna_sequence)
    protein_sequence = ""
    start_codon = "AUG"
    stop_codon = "stop"
    start_index = mrna_sequence.find(start_codon)
    
    if start_index == -1:
        return ""

    while start_index < len(mrna_sequence):
        codon = mrna_sequence[start_index:start_index + 3]
        amino_acid = codon_dict.get(codon, "")
        if amino_acid == stop_codon:
            break
        protein_sequence += amino_acid
        start_index += 3

    return protein_sequence

# 4. 读取 seq.fa 文件并创建序列字典 seq_dict
seq_dict = {}
current_seq_name = ""
current_seq = ""
with open("seq.fa", "r") as seq_file:
    for line in seq_file:
        if line.startswith(">"):
            if current_seq_name:
                seq_dict[current_seq_name] = current_seq
            current_seq_name = line.strip()[1:]
            current_seq = ""
        else:
            current_seq += line.strip()
    if current_seq_name:
        seq_dict[current_seq_name] = current_seq

# 5. 创建 protein_dict 字典，将序列翻译为氨基酸序列
protein_dict = {}
for seq_name, dna_sequence in seq_dict.items():
    protein_sequence = translate(dna_sequence)
    protein_dict[seq_name] = protein_sequence
for seq_name, protein_sequence in protein_dict.items():
    print(f"Sequence Name: {seq_name}")
    print(f"Protein Sequence: {protein_sequence}")
    print()
