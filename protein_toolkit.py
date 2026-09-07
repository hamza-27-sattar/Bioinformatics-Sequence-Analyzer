# 1. AA Validation
def validate():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    allowed = ("A", "R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V")
    for val in AA:
        if val not in allowed:
            print("Invalid Amino Acid Sequence entered")
            return
    print("Valid Amino Acid Sequence")
# 2. Sequence length
def base():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    print("Sequence:",len(AA),"Amino Acids")
# 3. Amino Acid Counter
def aa_counter():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    print("Alanine:",AA.count("A"))
    print("Arginine:",AA.count("R"))
    print("Asparagine:",AA.count("N"))
    print("Aspartic Acid:",AA.count("D"))
    print("Cysteine:",AA.count("C"))
    print("Glutamic Acid:",AA.count("E"))
    print("Glutamine:",AA.count("Q"))
    print("Glycine:",AA.count("G"))
    print("Histidine:",AA.count("H"))
    print("Isoleucine:",AA.count("I"))
    print("Leucine:",AA.count("L"))
    print("Lysine:",AA.count("K"))
    print("Methionine:",AA.count("M"))
    print("Phenylalanine:",AA.count("F"))
    print("Proline:",AA.count("P"))
    print("Serine:",AA.count("S"))
    print("Threonine:",AA.count("T"))
    print("Tryptophan:",AA.count("W"))
    print("Tyrosine:",AA.count("Y"))
    print("Valine:",AA.count("V"))
# 4. Amino Acid Frequency
def most_frequent():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    highest = 0
    amino = ""
    allowed = ("A","R","N","D","C","E","Q","G","H","I","L","K","M","F","P","S","T","W","Y","V")
    for val in allowed:
        if AA.count(val) > highest:
            highest = AA.count(val)
            amino = val
    print("Most Frequent Amino Acid:", amino)
    print("Count:", highest)
# 5. Amino Acid Composition
def composition():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    highest = 0
    amino = ""
    allowed = ("A","R","N","D","C","E","Q","G","H","I","L","K","M","F","P","S","T","W","Y","V")
    for val in allowed:
        if AA.count(val) > highest:
            highest = AA.count(val)
            amino = val
    percent = (highest / len(AA)) * 100
    print("Most Frequent Amino Acid:", amino)
    print("Composition:", round(percent,2), "%")
# 6. Molecular Weight of Sequence
def mol_weight():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    mol_weight = 0
    for val in AA:
        if val == "A":
            mol_weight += 71.1
        elif val == "R":
            mol_weight += 156.2
        elif val == "N":
            mol_weight += 114.1
        elif val == "D":
            mol_weight += 115.1
        elif val == "C":
            mol_weight += 103.1
        elif val == "E":
            mol_weight += 129.1
        elif val == "Q":
            mol_weight += 128.1
        elif val == "G":
            mol_weight += 57.1
        elif val == "H":
            mol_weight += 137.1
        elif val == "I":
            mol_weight += 113.2
        elif val == "L":
            mol_weight += 113.2
        elif val == "K":
            mol_weight += 128.2
        elif val == "M":
            mol_weight += 131.2
        elif val == "F":
            mol_weight += 147.1
        elif val == "P":
            mol_weight += 97.1
        elif val == "S":
            mol_weight += 87.1
        elif val == "T":
            mol_weight += 101.1
        elif val == "W":
            mol_weight += 186.2
        elif val == "Y":
            mol_weight += 163.2
        elif val == "V":
            mol_weight += 99.1
    print("Peptide Weight:",mol_weight,"Da or g/mol")
    print("Free Molecular Weight:",(18.02*len(AA)) + mol_weight,"Da or g/mol")
    return mol_weight
# 7. Polarity Residue
def polarity():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    polar_aa = ("T","S","C","Y","N","Q","D","E","K","R","H")
    polar = 0
    hydrophobic_aa = ("A","G","V","L","I","P","F","M","W")
    hydrophobic = 0
    for val in AA:
        if val in polar_aa:
                polar += 1
        elif  val in hydrophobic_aa:
                hydrophobic += 1
    print("Polar Amino Acids:",polar)
    print("Hydrophobic Amino Acids:",hydrophobic)
# 8. Acidic vs Basic Nature
def ph():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    acidic_aa = ("D","E")
    acidic = 0
    basic_aa = ("K","R","H")
    basic = 0
    for val in AA:
        if val in acidic_aa:
                acidic += 1
        elif  val in basic_aa:
                basic += 1
    print("Acidic Amino Acids:",acidic)
    print("Basic Amino Acids:",basic)
# 9. Aromatic AA
def aromatic():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    aromatic_aa = ("F","W","Y")
    aroma = 0
    for val in AA:
        if val in aromatic_aa:
            aroma += 1
    print(aroma,"Aromatic Amino Acids found in sequence")
    return 
# 10. Three Letter Sequence
def three_letters_expand():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    three_letters = ""
    for val in AA:
        if val == "A":
            three_letters += "Ala-"
        elif val == "R":
            three_letters += "Arg-"
        elif val == "N":
            three_letters += "Asn-"
        elif val == "D":
            three_letters += "Asp-"
        elif val == "C":
            three_letters += "Cys-"
        elif val == "E":
            three_letters += "Glu-"
        elif val == "Q":
            three_letters += "Gln-"
        elif val == "G":
            three_letters += "Gly-"
        elif val == "H":
            three_letters += "His-"
        elif val == "I":
            three_letters += "Ile-"
        elif val == "L":
            three_letters += "Leu-"
        elif val == "K":
            three_letters += "Lys-"
        elif val == "M":
            three_letters += "Met-"
        elif val == "F":
            three_letters += "Phe-"
        elif val == "P":
            three_letters += "Pro-"
        elif val == "S":
            three_letters += "Ser-"
        elif val == "T":
            three_letters += "Thr-"
        elif val == "W":
            three_letters += "Trp-"
        elif val == "Y":
            three_letters += "Tyr-"
        elif val == "V":
            three_letters += "Val-"
    print(three_letters)
# 11. Full Length AA Sequence
def full_expand():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    full_names = ""
    for val in AA:
        if val == "A":
            full_names += "Alanine-"
        elif val == "R":
            full_names += "Arginine-"
        elif val == "N":
            full_names += "Asparagine-"
        elif val == "D":
            full_names += "Aspartic Acid-"
        elif val == "C":
            full_names += "Cysteine-"
        elif val == "E":
            full_names += "Glutamic Acid-"
        elif val == "Q":
            full_names += "Glutamine-"
        elif val == "G":
            full_names += "Glycine-"
        elif val == "H":
            full_names += "Histidine-"
        elif val == "I":
            full_names += "Isoleucine-"
        elif val == "L":
            full_names += "Leucine-"
        elif val == "K":
            full_names += "Lysine-"
        elif val == "M":
            full_names += "Methionine-"
        elif val == "F":
            full_names += "Phenylalanine-"
        elif val == "P":
            full_names += "Proline-"
        elif val == "S":
            full_names += "Serine-"
        elif val == "T":
            full_names += "Threonine-"
        elif val == "W":
            full_names += "Tryptophan-"
        elif val == "Y":
            full_names += "Tyrosine-"
        elif val == "V":
            full_names += "Valine-"
    print(full_names)
# 12. Save Results
def save_results():
    AA = (input("Please enter any of the 20 Amino Acids sequence: ")).upper()
    weight = 0
    for val in AA:
        if val == "A":
            weight += 71.1
        elif val == "R":
            weight += 156.2
        elif val == "N":
            weight += 114.1
        elif val == "D":
            weight += 115.1
        elif val == "C":
            weight += 103.1
        elif val == "E":
            weight += 129.1
        elif val == "Q":
            weight += 128.1
        elif val == "G":
            weight += 57.1
        elif val == "H":
            weight += 137.1
        elif val == "I":
            weight += 113.2
        elif val == "L":
            weight += 113.2
        elif val == "K":
            weight += 128.2
        elif val == "M":
            weight += 131.2
        elif val == "F":
            weight += 147.1
        elif val == "P":
            weight += 97.1
        elif val == "S":
            weight += 87.1
        elif val == "T":
            weight += 101.1
        elif val == "W":
            weight += 186.2
        elif val == "Y":
            weight += 163.2
        elif val == "V":
            weight += 99.1
    with open("protein_results.txt","a") as f:

        f.write("\n===============================\n")
        f.write("Protein Toolkit Report\n")
        f.write("===============================\n")
        f.write(f"Sequence : {AA}\n")
        f.write(f"Length   : {len(AA)} amino acids\n")
        f.write(f"Polar Residues        : {sum(1 for x in AA if x in ('T','S','C','Y','N','Q','D','E','K','R','H'))}\n")
        f.write(f"Hydrophobic Residues  : {sum(1 for x in AA if x in ('A','G','V','L','I','P','F','M','W'))}\n")
        f.write(f"Acidic Residues : {AA.count('D') + AA.count('E')}\n")
        f.write(f"Basic Residues  : {AA.count('K') + AA.count('R') + AA.count('H')}\n")
        f.write(f"Peptide Molecular Weight : {weight} Da\n")
        f.write(f"GC-like Aromatic Residues : {AA.count('F') + AA.count('W') + AA.count('Y')}\n")
        f.write("===============================\n\n")

    print("Results Saved Successfully!")
# 13. Load Previous Results
def load_results():
    try:
        with open("protein_results.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No previous analyses found.")
# 14. Exit

def protein_tool():
    while True:

            print("""
            ===== Protein TOOLKIT =====
            1. Amino Acid Validation
            2. Sequence length
            3. Amino Acid Counter
            4. Amino Acid Frequency
            5. Amino Acid Composition
            6. Molecular Weight of Sequence
            7. Polarity Residue 
            8. Acidic vs Basic Nature of Amino Acids
            9. Aromatic Amino Acids
            10.Three Letter Sequence
            11.Full Length Sequence
            12.Save Results
            13.Load Previous Results
            14.Exit
            """)

            choice = int(input("Choose: "))

            if choice == 1:
                validate()
            elif choice == 2:
                base()
            elif choice == 3:
                aa_counter()
            elif choice == 4:
                most_frequent()
            elif choice == 5:
                composition()
            elif choice == 6:
                mol_weight()
            elif choice == 7:
                polarity()
            elif choice == 8:
                ph()
            elif choice == 9:
                aromatic()
            elif choice == 10:
                three_letters_expand()
            elif choice == 11:
                full_expand()
            elif choice == 12:
                save_results()
            elif choice == 13:
                load_results()
            elif choice == 14:
                print("You have exited")
                break
            else:
                print("Invalid Choice")