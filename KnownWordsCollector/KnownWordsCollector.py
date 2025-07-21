import csv
import os
from glob import glob

def extract_first_column(csv_files):
    entries = []
    for file in csv_files:
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:  # make sure the row is not empty
                    entries.append(row[0].strip('"'))  # remove surrounding quotes if present
    return entries

def main():
    # Folder containing your CSV files (use '.' for current directory)
    folder = '.'
    csv_files = glob(os.path.join(folder, '*.csv'))

    first_column_entries = extract_first_column(csv_files)

    with open('KnownWords.txt', 'w', encoding='utf-8') as out_file:
        for entry in first_column_entries:
            out_file.write(entry + '\n')

if __name__ == '__main__':
    main()
