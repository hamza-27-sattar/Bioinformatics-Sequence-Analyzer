# 1.Validate DNA
def validate():
    DNA = (input("Please enter DNA sequence: ")).upper()
    allowed = ("A", "T", "G", "C")
    for val in DNA:
        if val not in allowed:
            print("Invalid DNA Sequence  entered")
            return
    print("Valid DNA Sequence")
# 2. Complement
def complement_DNA(DNA=None):
    if DNA is None:
        DNA = input("Please enter DNA sequence: ").upper()
    else:
        DNA = DNA.upper()
    complement = ""
    for val in DNA:
        if val == "A":
            complement += "T"
        elif val == "T":
            complement += "A"
        elif val == "G":
            complement += "C"
        elif val == "C":
            complement += "G"
    return complement
# 3. Reverse Sequencing
def r_seq():
    DNA = (input("Please enter DNA sequence: ")).upper()
    print("Reverse Sequence:",DNA[::-1])
# 4. Reverse Complement
def rev_comp():
    DNA = (input("Please enter DNA sequence: ")).upper()
    complement = ""
    for val in DNA:
        if val == "A":
                complement += "T"
        elif val == "T":
                complement += "A"
        elif val == "G":
                complement += "C"
        elif val == "C":
                complement += "G"
    print("Complementary Strand's Reverse:",complement[::-1])
# 5.Transcription
def transcription():
    DNA = (input("Please enter DNA sequence: ")).upper()
    RNA = DNA.replace("T","U")
    print("DNA -> RNA:",RNA)
# 6.AT Counter
def AT():
    DNA = (input("Please enter DNA sequence: ")).upper()
    print("Sequence:",DNA.count("A")+DNA.count("T"),"AT bases")
# 7.GC Counter
def GC():
    DNA = (input("Please enter DNA sequence: ")).upper()
    print("Sequence:",DNA.count("G")+DNA.count("C"),"GC bases")
# 8.base counter
def base():
    DNA = (input("Please enter DNA sequence: ")).upper()
    print("Sequence:",len(DNA),"bases")
# 9. Molecular Weight
def mol_weight():
    DNA = (input("Please enter DNA sequence: ")).upper()
    mol_weight = 0
    for val in DNA:
        if val == "A":
            mol_weight += 313.21
        elif val == "T":
            mol_weight += 304.20
        elif val == "C":
            mol_weight += 289.18
        elif val == "G":
            mol_weight += 329.21
    print("Sequence Weight:",mol_weight,"g/mol")
# 10. Save Results
def save_results():
    DNA = input("Please enter DNA sequence: ").upper()
    with open("dna_results.txt", "a") as f:
        f.write("=========================\n")
        f.write(f"DNA: {DNA}\n")
        f.write(f"Complement: {complement_DNA(DNA)}\n")
        f.write(f"Reverse: {DNA[::-1]}\n")
        f.write(f"Reverse Complement: {complement_DNA(DNA)[::-1]}\n")
        f.write(f"RNA: {DNA.replace('T','U')}\n")
        f.write(f"AT Count: {DNA.count('A') + DNA.count('T')}\n")
        f.write(f"GC Count: {DNA.count('G') + DNA.count('C')}\n")
        f.write(f"Base Count: {len(DNA)}\n")
        f.write("=========================\n\n")
    print("Results saved successfully!")
# 11. Loading Previous Analysis
def load_results():
    try:
        with open("dna_results.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No previous analyses found.")
# 12. Exit

def dna_tool():
    while True:

        print("""
        ===== DNA TOOLKIT =====
        1. Validate DNA
        2. Complementary Strand
        3. Reverse Sequence
        4. Reverse Complement
        5. Transcription
        6. AT Base Count
        7. GC Base Count
        8. Bases Count
        9. Molecular Weight
        10.Save Results
        11.Load Previous Analysis
        12.Exit
        """)

        choice = int(input("Choose: "))
        if choice == 1:
            validate()
        elif choice == 2:
            print("Complementary Strand:",complement_DNA())
        elif choice == 3:
            r_seq()
        elif choice == 4:
            rev_comp()
        elif choice == 5:
            transcription()
        elif choice == 6:
            AT()
        elif choice == 7:
            GC()
        elif choice == 8:
            base()
        elif choice == 9:
            mol_weight()
        elif choice == 10:
            save_results()
        elif choice == 11:
            load_results()
        elif choice == 12:
            print("You have exited")
            break
        else:
            print("Invalid Choice")