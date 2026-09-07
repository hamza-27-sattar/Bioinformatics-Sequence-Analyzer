# 1.Validate RNA
def validate():
    RNA = (input("Please enter RNA sequence: ")).upper()
    allowed = ("A", "U", "G", "C")
    for val in RNA:
        if val not in allowed:
            print("Invalid RNA Sequence  entered")
            return
    print("Valid RNA Sequence")
# 2.Reverse Transcription
def rev_transcription():
    RNA = (input("Please enter RNA sequence: ")).upper()
    DNA = RNA.replace("U","T")
    print("RNA -> DNA:",DNA)
# 3.AU Counter
def AU():
    RNA = (input("Please enter RNA sequence: ")).upper()
    print("Sequence:",RNA.count("A")+RNA.count("U"),"AU bases")
# 4.GC Counter
def GC():
    RNA = (input("Please enter RNA sequence: ")).upper()
    print("Sequence:",RNA.count("G")+RNA.count("C"),"GC bases")
# 5.base counter
def base():
    RNA = (input("Please enter RNA sequence: ")).upper()
    print("Sequence:",len(RNA),"bases")
# 6. Molecular Weight
def mol_weight():
    RNA = (input("Please enter RNA sequence: ")).upper()
    mol_weight = 0
    for val in RNA:
        if val == "A":
            mol_weight += 329.21
        elif val == "U":
            mol_weight += 306.17
        elif val == "C":
            mol_weight += 305.18
        elif val == "G":
            mol_weight += 345.21
    print("Sequence Weight:",mol_weight,"g/mol")
# 7. Save Results
def save_results():
    RNA = (input("Please enter RNA sequence: ")).upper()
    with open("rna_results.txt", "a") as f:
        f.write("=========================\n")
        f.write(f"RNA: {RNA}\n")
        f.write(f"DNA: {RNA.replace('U','T')}\n")
        f.write(f"AU Count: {RNA.count('A') + RNA.count('U')}\n")
        f.write(f"GC Count: {RNA.count('G') + RNA.count('C')}\n")
        f.write(f"Base Count: {len(RNA)}\n")
        f.write("=========================\n\n")

    print("Results saved successfully!")
# 8. Loading Previous Analysis
def load_results():
    try:
        with open("rna_results.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No previous analyses found.")
# 9. Exit

def rna_tool():
    while True:

        print("""
        ===== RNA TOOLKIT =====
        1. RNA Validation
        2. Reverse Transcription
        3. AU Base Count
        4. GC Base Count
        5. Bases Count
        6. Sequence Molecular Weight
        7. Save Results
        8. Load Previous Analysis
        9. Exit
        """)

        choice = int(input("Choose: "))

        if choice == 1:
            validate()
        elif choice == 2:
            rev_transcription()
        elif choice == 3:
            AU()
        elif choice == 4:
            GC()
        elif choice == 5:
            base()
        elif choice == 6:
            mol_weight()
        elif choice == 7:
            save_results()
        elif choice == 8:
            load_results()
        elif choice == 9:
            print("You have exited")
            break
        else:
            print("Invalid Choice")