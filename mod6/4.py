import json
from collections import Counter
from itertools import groupby
from datetime import datetime

# Read logs from the file
def read_logs(file_path):
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            log = json.loads(line)
            logs.append(log)
    return logs

# Load logs from the file
logs = read_logs('skillbox_json_messages.log')

# Task 1: Count messages for each level
level_counts = Counter(log['level'] for log in logs)
print("Task 1: Messages count for each level:")
for level, count in level_counts.items():
    print(f"{level}: {count}")

# Task 2: Find the hour with the most logs
hour_logs = [(log['time'], log) for log in logs]
hour_logs.sort(key=lambda x: x[0])
hour_groups = groupby(hour_logs, key=lambda x: x[0][:2])
hour_counts = [(hour, len(list(group))) for hour, group in hour_groups]
max_hour, max_count = max(hour_counts, key=lambda x: x[1])
print(f"Task 2: The hour with the most logs: {max_hour} ({max_count} logs)")

# Task 3: Count CRITICAL logs between 05:00:00 and 05:20:00
critical_logs = [log for log in logs if log['level'] == 'CRITICAL']
filtered_critical_logs = [log for log in critical_logs if '05:00:00' <= log['time'] <= '05:20:00']
print(f"Task 3: Number of CRITICAL logs between 05:00:00 and 05:20:00: {len(filtered_critical_logs)}")

# Task 4: Count messages containing the word "dog"
dog_logs = [log for log in logs if 'dog' in log['message'].lower()]
print(f"Task 4: Number of logs containing the word 'dog': {len(dog_logs)}")

# Task 5: Find the most frequent word in WARNING messages
warning_logs = [log for log in logs if log['level'] == 'WARNING']
warning_words = [word.lower() for log in warning_logs for word in log['message'].split()]
word_counts = Counter(warning_words)
most_common_word, most_common_count = word_counts.most_common(1)[0]
print(f"Task 5: Most common word in WARNING messages: '{most_common_word}' ({most_common_count} occurrences)")

