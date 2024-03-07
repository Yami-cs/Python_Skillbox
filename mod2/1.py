import os

output_file_path = "output_file.txt"

def get_summary_rss(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()[1:]

    total_rss_bytes = 0
    for line in lines:
        columns = line.split()
        rss_bytes = int(columns[5])  
        total_rss_bytes += rss_bytes

    def format_bytes(size):
        for unit in ["B", "KiB", "MiB", "GiB"]:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} TiB"

    return format_bytes(total_rss_bytes)

if __name__ == "__main__":
    result = get_summary_rss(output_file_path)
    print(f"Total RSS memory usage: {result}")