# Dedline API 🇺🇸
🗳 A simple API for US election deadline info 🗳

This is a [static api](https://www.seancdavis.com/posts/lets-talk-about-static-apis/), taken from the JSON file in [dedline.io](dedline.io), that anyone can access for election information (Updated for 2026!)

**Base URL:** `https://dedline-api.netlify.app/`

**Features:**
- ✅ All 50 states + DC
- ✅ Primary and general election deadlines
- ✅ Official voter registration websites
- ✅ Same-day registration info
- ✅ Online registration availability
- ✅ Free and open source!

Check out [dedline.io](https://www.dedline.io) to see it in action, or use our [embeddable widgets](https://github.com/dedline-io/dedline-io/blob/main/WIDGET_DOCS.md)!

## Endpoints:

### Get All States

**`GET /states.json`**

Returns an array of all US states (including DC) with their voter registration information.

**Example Request:**
```bash
curl https://dedline-api.netlify.app/states.json
```

**Response Format:**

```json
{
  "states": [
    {
      "label": "California",
      "value": "CA",
      "deadline": "20261019",
      "primaryDeadline": "20260518",
      "primaryDate": "20260602",
      "generalElectionDate": "20261103",
      "url": "https://www.sos.ca.gov/elections/voter-registration/",
      "onlineAccepted": true,
      "lastMinuteAccepted": true,
      "emoji": "🌴🌴🌴🌴🌴",
      "notes": "In California, those convicted of felonies can register and vote after serving their sentence."
    }
  ]
}
```

**Field Descriptions:**
- `label` - Full state name (string)
- `value` - Two-letter state abbreviation (string)
- `deadline` - General election voter registration deadline in YYYYMMDD format (string)
- `primaryDeadline` - Primary election voter registration deadline in YYYYMMDD format (string)
- `primaryDate` - Primary election date in YYYYMMDD format (string)
- `generalElectionDate` - General election date in YYYYMMDD format (string) - November 3, 2026 for most states
- `url` - Official state voter registration website (string)
- `onlineAccepted` - Whether voters can register online (boolean)
- `lastMinuteAccepted` - Whether voters can register on election day (boolean)
- `emoji` - State-themed emoji (string)
- `notes` - Additional details about state registration (string, optional)
 
### Get Specific State

**`GET /states/[STATE_ABBREVIATION].json`**

Returns voter registration information for a specific state.

**Example Request:**
```bash
curl https://dedline-api.netlify.app/states/ca.json
```

**Response Format:**
```json
{
  "label": "New York",
  "value": "NY",
  "deadline": "20261024",
  "primaryDeadline": "20260528",
  "primaryDate": "20260623",
  "generalElectionDate": "20261103",
  "url": "https://www.ny.gov/services/register-vote",
  "onlineAccepted": true,
  "lastMinuteAccepted": false,
  "emoji": "🗽🗽🗽🗽🗽",
  "notes": "In New York, those with felony convictions get their voting rights restored after serving their sentence!"
}
```

### Get Same-Day Registration States

**`GET /lastMinuteAccepted.json`**

Returns states that allow voter registration on election day.

**Example Request:**
```bash
curl https://dedline-api.netlify.app/lastMinuteAccepted.json
```

**Response Format:**

```
['STATE', 'STATE_2', STATE_3']
```


### Get States Without Online Registration

**`GET /onlineNotAccepted.json`**

Returns states that require voters to register in person or by mail (no online registration available).

**Example Request:**
```bash
curl https://dedline-api.netlify.app/onlineNotAccepted.json
```

**Response Format:**

```
['STATE', 'STATE_2', STATE_3']
```


### Get Upcoming Deadlines

**`GET /upcoming.json`**

Returns states with primary or general registration deadlines in the next 30 days.

**Example Request:**
```bash
curl https://dedline-api.netlify.app/upcoming.json
```

**Response Format:**
```json
{
  "primary": [
    {
      "state": "TX",
      "label": "Texas",
      "deadline": "20260202",
      "daysUntil": 8
    }
  ],
  "general": []
}
```

### Get Statistics

**`GET /stats.json`**

Returns summary statistics about voter registration across all states.

**Example Request:**
```bash
curl https://dedline-api.netlify.app/stats.json
```

**Response Format:**
```json
{
  "totalStates": 51,
  "onlineRegistrationAvailable": 41,
  "sameDayRegistrationAvailable": 21,
  "lastUpdated": "2026-01-25"
}
```

## Usage Examples

### JavaScript/Node.js
```javascript
// Fetch all states
fetch('https://dedline-api.netlify.app/states.json')
  .then(res => res.json())
  .then(data => console.log(data.states));

// Fetch specific state
fetch('https://dedline-api.netlify.app/states/ny.json')
  .then(res => res.json())
  .then(data => console.log(data));
```

### Python
```python
import requests

# Fetch all states
response = requests.get('https://dedline-api.netlify.app/states.json')
states = response.json()['states']

# Fetch specific state
response = requests.get('https://dedline-api.netlify.app/states/ca.json')
california = response.json()
```

## CORS & Rate Limiting

- **CORS:** Enabled for all origins - safe to use from browsers
- **Rate Limiting:** Please be respectful with requests. This is a free, community resource!

## Attribution

If you use this API in your project, we'd appreciate a link back to [dedline.io](https://www.dedline.io) or this repository. Thanks for helping spread the word about voter registration! 🗳️

## Ideas/Issues
Feel free to open any [issues](https://github.com/dedline-io/dedline-api/issues) or ideas for new endpoints, new data to be added, etc!

## Contact
dedline-io@protonmail.com
