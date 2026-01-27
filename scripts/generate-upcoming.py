#!/usr/bin/env python3
import json
from datetime import datetime, timedelta

# Read states data
with open('public/states.json', 'r') as f:
    data = json.load(f)

today = datetime.now()
thirty_days_from_now = today + timedelta(days=30)

# Convert YYYYMMDD string to datetime
def parse_date(date_str):
    return datetime.strptime(date_str, '%Y%m%d')

# Calculate days until deadline
def days_until(deadline_str):
    deadline = parse_date(deadline_str)
    delta = deadline - today
    return delta.days

# Find the latest primary date to determine if primary season is over
primary_dates = [parse_date(state['primaryDate']) for state in data['states'] if 'primaryDate' in state and state['primaryDate']]
latest_primary = max(primary_dates) if primary_dates else today

# Determine if we should show primary or general deadlines
show_primary = today <= latest_primary

upcoming = {
    "primary": [],
    "general": []
}

for state in data['states']:
    # Check primary deadlines
    if show_primary and 'primaryDeadline' in state and state['primaryDeadline']:
        deadline = parse_date(state['primaryDeadline'])
        if today <= deadline <= thirty_days_from_now:
            upcoming['primary'].append({
                'state': state['value'],
                'label': state['label'],
                'deadline': state['primaryDeadline'],
                'daysUntil': days_until(state['primaryDeadline'])
            })

    # Check general deadlines (show if primary season is over OR always include in the data)
    if 'deadline' in state and state['deadline']:
        deadline = parse_date(state['deadline'])
        if today <= deadline <= thirty_days_from_now:
            upcoming['general'].append({
                'state': state['value'],
                'label': state['label'],
                'deadline': state['deadline'],
                'daysUntil': days_until(state['deadline'])
            })

# Sort by deadline date
upcoming['primary'].sort(key=lambda x: x['deadline'])
upcoming['general'].sort(key=lambda x: x['deadline'])

# Write to file
with open('public/upcoming.json', 'w') as f:
    json.dump(upcoming, f, indent=2)

print(f"Generated upcoming.json - Primary season active: {show_primary}")
print(f"Found {len(upcoming['primary'])} upcoming primary deadlines")
print(f"Found {len(upcoming['general'])} upcoming general deadlines")
