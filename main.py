import dna_toolkit
import rna_toolkit
import protein_toolkit
import fasta_toolkit

while True:

    print("""
   ================================
       BIOINFORMATICS TOOLKIT
   ================================

    1. DNA Toolkit
    2. RNA Toolkit
    3. Protein Toolkit
    4. FASTA Reader
    5. Exit

    """)

    choice = int(input("Choose: "))

    if choice == 1:
        dna_toolkit.dna_tool()
    elif choice == 2:
        rna_toolkit.rna_tool()
    elif choice == 3:
        protein_toolkit.protein_tool()
    elif choice == 4:
        fasta_toolkit.fasta_tool()
    elif choice == 5:
        print("You have exited")
        break
    else:
        print("Invalid Choice")