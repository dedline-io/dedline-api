#!/usr/bin/env python3
import json
from datetime import datetime

# Read states data
with open('public/states.json', 'r') as f:
    data = json.load(f)

# Calculate statistics
total_states = len(data['states'])
online_available = sum(1 for state in data['states'] if state.get('onlineAccepted', False))
same_day_available = sum(1 for state in data['states'] if state.get('lastMinuteAccepted', False))

stats = {
    'totalStates': total_states,
    'onlineRegistrationAvailable': online_available,
    'sameDayRegistrationAvailable': same_day_available,
    'lastUpdated': datetime.now().strftime('%Y-%m-%d')
}

# Write to file
with open('public/stats.json', 'w') as f:
    json.dump(stats, f, indent=2)

print(f"Generated stats.json")
print(f"Total states: {total_states}")
print(f"Online registration: {online_available}")
print(f"Same-day registration: {same_day_available}")
