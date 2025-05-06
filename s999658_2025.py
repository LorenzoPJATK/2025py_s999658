import random

# --------------------------------------------------------
# Purpose of the Program:
# This program generates a random DNA sequence of user-specified length,
# inserts the user's name at a random position (not counted in statistics),
# and saves it to a FASTA format file with proper metadata and formatting.
# It also calculates and displays base composition and CG ratio.
# --------------------------------------------------------

def generate_dna_sequence(length):
    # Generates a random DNA sequence of specified length using A, C, G, and T
    return ''.join(random.choices('ACGT', k=length))

def insert_name(sequence, name):
    # Inserts the user's name at a random location within the sequence
    insert_position = random.randint(0, len(sequence))
    return sequence[:insert_position] + name + sequence[insert_position:]

def calculate_statistics(sequence):
    # Calculates the percentage of each nucleotide and CG content
    filtered_seq = ''.join([nuc for nuc in sequence if nuc in 'ACGT'])
    total = len(filtered_seq)
    stats = {nuc: round((filtered_seq.count(nuc) / total) * 100, 1) for nuc in 'ACGT'}
    cg_ratio = round(((filtered_seq.count('C') + filtered_seq.count('G')) / total) * 100, 1)
    return stats, cg_ratio

def save_fasta_file(filename, header, sequence):
    # Saves the sequence to a FASTA file with 60-character line formatting

    # ORIGINAL:
    # with open(filename, 'w') as f:
    #     f.write(f">{header}\n{sequence}\n")
    # MODIFIED (adds standard 60-character line breaks to conform with FASTA format):
    with open(filename, 'w') as f:
        f.write(f">{header}\n")
        for i in range(0, len(sequence), 60):
            f.write(sequence[i:i+60] + '\n')

def main():
    # Main program logic to collect input, generate sequence, insert name, and display stats

    # ORIGINAL:
    # length = int(input("Enter the sequence length: "))
    # MODIFIED (adds validation to ensure a positive integer is entered):
    while True:
        try:
            length = int(input("Enter the sequence length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer for the sequence length.")

    seq_id = input("Enter the sequence ID: ")
    description = input("Provide a description of the sequence: ")
    name = input("Enter your name: ")

    raw_sequence = generate_dna_sequence(length)  # Generate random DNA sequence
    final_sequence = insert_name(raw_sequence, name)  # Insert name at a random location
    stats, cg_ratio = calculate_statistics(final_sequence)  # Get sequence stats

    filename = f"{seq_id}.fasta"  # Filename uses sequence ID
    header = f"{seq_id} {description}"  # FASTA header includes ID and description
    save_fasta_file(filename, header, final_sequence)  # Save to file

    print(f"\nThe sequence was saved to the file {filename}")
    print("Sequence statistics:")

    # ORIGINAL:
    # for nuc in 'ACGT':
    #     print(f"{nuc}: {stats[nuc]}%")
    # MODIFIED (adds aligned output for readability):
    for nuc in 'ACGT':
        print(f"{nuc}: {stats[nuc]:>5.1f}%")
    print(f"%CG: {cg_ratio:>5.1f}")

if __name__ == "__main__":
    main()  # Execute main only when script is run directly
