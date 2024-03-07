import sys

def get_mean_size(lines):
    if lines and lines[0].startswith("total"):
        lines = lines[1:]

    file_sizes = []
    for line in lines:
        columns = line.split()
        if len(columns) >= 5:
            size = columns[4]
            file_sizes.append(int(size))

    total_size = sum(file_sizes)
    num_files = len(file_sizes)
    if num_files > 0:
        mean_size = total_size / num_files
        return mean_size
    else:
        return 0

if __name__ == "__main__":
    input_lines = sys.stdin.readlines()

    result = get_mean_size(input_lines)
    print(f"Mean file size: {result} bytes")
