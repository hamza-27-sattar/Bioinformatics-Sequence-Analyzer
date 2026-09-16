# 1. Open FASTA File
lines = []
def open_file():
    global lines
    path = input("Enter FASTA file name: ")
    with open(path, "r") as f:
        content = f.read()
        lines = content.split("\n")
    print("FASTA loaded successfully.")

# 2. Display Header
def header():
    for val in lines:
        if val.startswith(">"):
            print(val)

# 3. Display Sequence
def seq():
    for val in lines:
        if val.startswith(">"):
            pass
        else:
            return val

# 4. Sequence Length
def length():
    sequence = seq()
    print("Count:", len(sequence))

# 5. Validate Sequence
def validate():
    sequence = seq()
    allowed = ("A", "R", "N", "D", "C", "E", "Q", "G", "H",
               "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V")
    for val in sequence:
        if val not in allowed:
            print("Invalid Fasta Sequence entered")
            return
    print("Valid Fasta Sequence")
# 6. Menu / Exit
def fasta_tool():
    while True:
        print("""
    ===== FASTA Reader =====
    1. Open FASTA
    2. Display Header
    3. Display Sequence
    4. Sequence Length
    5. Validate Sequence
    6. Exit
    """)

        choice = int(input("Choose: "))

        if choice == 1:
            open_file()
        elif choice == 2:
            header()
        elif choice == 3:
            print(seq())
        elif choice == 4:
            length()
        elif choice == 5:
            validate()
        elif choice == 6:
            print("You have exited")
            break
        else:
            print("Invalid Choice")