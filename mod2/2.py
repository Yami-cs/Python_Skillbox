import sys
import os

def get_mean_size(lines):
    # Skip the first line (header) if it exists
    if lines and lines[0].startswith("total"):
        lines = lines[1:]

    # Extract file sizes from the lines
    file_sizes = []
    for line in lines:
        columns = line.split()
        if len(columns) >= 5:
            size = columns[4]
            file_sizes.append(int(size))

    # Calculate the mean size
    total_size = sum(file_sizes)
    num_files = len(file_sizes)
    if num_files > 0:
        mean_size = total_size / num_files
        return mean_size
    else:
        return None

if __name__ == "__main__":
    # Read input lines from stdin
    input_lines = sys.stdin.readlines()

    # Calculate the mean size
    result = get_mean_size(input_lines)
    if result is not None:
        print(f"Mean file size: {result} bytes")
    else:
        print("No files found or unable to retrieve their sizes.")
