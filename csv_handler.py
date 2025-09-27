"""
Handles reading and writing the schedule CSV file.
"""
import csv
import copy

def read_schedule(csv_path):
    schedule = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            schedule.append(row)
    return schedule

def update_status(csv_path, entry, new_status):
    rows = read_schedule(csv_path)
    updated = False
    for row in rows:
        if all(row[k] == entry[k] for k in entry if k != 'status'):
            row['status'] = new_status
            updated = True
    if updated:
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    return updated
