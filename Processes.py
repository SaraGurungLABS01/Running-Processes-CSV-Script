import os
import psutil
import csv

# Create an empty list to store information about running processes.
process_list = []

# Get a list of all running processes and collect specific attributes (pid, name, exe, cpu_percent, memory_info).
for p in psutil.process_iter(attrs=['pid', 'name', 'exe', 'cpu_percent', 'memory_info']):
    p_info = p.info
    process_list.append(p_info)

# Define the name of the CSV file where we'll save the process information.
csv_file = 'processes.csv'

# Define the column headers for the CSV file.
headers = ['Process ID', 'Name', 'Executable Path', 'CPU Usage (%)', 'Memory Usage (bytes)']

# Create a list of dictionaries, where each dictionary represents process information.
rows = [
    {
        "Process ID": process["pid"],
        "Name": process["name"],
        "Executable Path": process["exe"],
        "CPU Usage (%)": process["cpu_percent"],
        "Memory Usage (bytes)": process["memory_info"].rss
    }
    for process in process_list
]

# Open the CSV file for writing in text mode and ensure newlines are handled properly.
with open(csv_file, "w", newline="") as csvfile:
    # Create a CSV writer that uses the specified headers.
    writer = csv.DictWriter(csvfile, fieldnames=headers)

    # Write the header row to the CSV file.
    writer.writeheader()

    # Write the process information for each process in the list.
    writer.writerows(rows)

# Print a message to confirm that the process list has been saved to the CSV file.
print(f"Process list saved to {csv_file}")
