import csv

# Input files
file_a = 'Meitantei Conan.csv'
file_b = 'known.csv'
file_c = 'learning.csv'
output_file = 'A_filtered.csv'  # Output file

# Load first-column entries from B and C
def get_first_column_entries(filename):
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        return set(row[0] for row in reader if row)  # ensure row isn't empty

b_entries = get_first_column_entries(file_b)
c_entries = get_first_column_entries(file_c)
excluded_entries = b_entries.union(c_entries)

# Filter A.csv
with open(file_a, encoding='utf-8') as f_in, open(output_file, 'w', newline='', encoding='utf-8') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    for row in reader:
        if row and row[0] not in excluded_entries:
            writer.writerow(row)

print(f"Filtered file saved as {output_file}")
