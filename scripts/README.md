# API Data Generation Scripts

These scripts automatically generate dynamic API endpoints from the static `states.json` data.

## Scripts

### `generate-upcoming.py`

Generates `/upcoming.json` with states that have registration deadlines in the next 30 days.

**Smart switching logic:**
- Before primary season ends: Shows upcoming primary registration deadlines
- After primary season ends: Shows upcoming general election registration deadlines
- Automatically determines the switch by finding the latest primary date

**Output:**
```json
{
  "primary": [...],
  "general": [...]
}
```

### `generate-stats.py`

Generates `/stats.json` with summary statistics about voter registration.

**Output:**
```json
{
  "totalStates": 51,
  "onlineRegistrationAvailable": 43,
  "sameDayRegistrationAvailable": 24,
  "lastUpdated": "2026-01-25"
}
```

## Automation

These scripts run automatically via GitHub Actions:

- **Schedule:** Daily at 6 AM UTC (2 AM ET)
- **Workflow:** `.github/workflows/update-data.yml`
- **Trigger:** Can also be manually triggered from the Actions tab

When the data changes, the workflow commits the updated JSON files, which triggers a Netlify rebuild and deploys the new data.

## Manual Usage

To regenerate the files locally:

```bash
# From the dedline-api directory
python3 scripts/generate-upcoming.py
python3 scripts/generate-stats.py
```

## When to Update

You don't need to manually run these scripts in most cases. The GitHub Action handles it automatically.

**Manual updates needed when:**
- You update `states.json` with new deadline information
- You want to test changes to the generation logic
- You need to force an immediate update before the next scheduled run
