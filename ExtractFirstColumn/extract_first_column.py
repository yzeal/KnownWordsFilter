import csv
import os
import sys

def extract_first_column(input_filename):
    # Create output filename
    base, ext = os.path.splitext(input_filename)
    output_filename = f"{base}_1c.csv"
    
    # Open input and output files
    with open(input_filename, newline='', encoding='utf-8') as infile, \
         open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            if row:  # Make sure row is not empty
                writer.writerow([row[0]])

    print(f"First column written to {output_filename}")

# If run from command line
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_first_column.py <input_file.csv>")
    else:
        extract_first_column(sys.argv[1])
