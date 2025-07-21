import csv
import sys
import os

def get_first_column_entries(filename):
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        return set(row[0] for row in reader if row)

def main():
    if len(sys.argv) < 3:
        print("Usage: python filter_csv.py <main.csv> <filter1.csv> [<filter2.csv> ...]")
        sys.exit(1)

    main_file = sys.argv[1]
    filter_files = sys.argv[2:]

    # Build exclusion set from all filter files
    excluded_entries = set()
    for f in filter_files:
        excluded_entries.update(get_first_column_entries(f))

    # Output file name
    base_name = os.path.basename(main_file)
    output_file = f"filtered_{base_name}"

    # Filter and write
    with open(main_file, encoding='utf-8') as f_in, open(output_file, 'w', newline='', encoding='utf-8') as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        for row in reader:
            if row and row[0] not in excluded_entries:
                writer.writerow(row)

    print(f"Filtered output written to {output_file}")

if __name__ == "__main__":
    main()
