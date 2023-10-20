protein_dict = {}
for seq_name, dna_sequence in seq_dict.items():
    protein_sequence = translate(dna_sequence)
    protein_dict[seq_name] = protein_sequence

for seq_name, protein_sequence in protein_dict.items():
    print(f"Sequence Name: {seq_name}")
    print(f"Protein Sequence: {protein_sequence}")
    print()


with open("protein.txt", "w") as protein_file:
    for seq_name, protein_sequence in protein_dict.items():
        protein_file.write(f"Sequence Name: {seq_name}\n")
        protein_file.write(f"Protein Sequence: {protein_sequence}\n\n")

print("protein_dict 内容已写入 protein.txt 文件。")
