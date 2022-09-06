# Dedline API 🇺🇸
🗳 A simple API for US election deadline info 🗳

This is a [static api](https://www.seancdavis.com/posts/lets-talk-about-static-apis/), taken from the JSON file in [dedline.io](dedline.io), that anyone can access for election information (2022 currently, hopefully will be updated in the future!)

If you need the base URL, just give me an email at dedline-io@protonmail.com - it's free and I'm hoping that people can use this info towards a good cause. :) Also, feel free to fork this repo and use this JSON for your own projects! 

## Endpoints:

**GET ALL INFO**

`/states.json`

This returns an array of all US states (including DC), as objects, in the following format:

```
 {
  "states: [
    {
      "label": STATE NAME (string)
      "value": STATE ABBREVIATION (string)
      "deadline": GENERAL ELECTION VOTER REGISTRATION DEADLINE IN YYYYMMDD FORMAT (string)
      "primaryDeadline": PRIMARY ELECTION VOTER REGISTRATION DEADLINE IN YYYYMMDD FORMAT (string)
      "primaryDate": PRIMARY ELECTION DATE IN YYYYMMDD FORMAT (string)
      "url": OFFICIAL STATE VOTER REGISTRATION WEBSITE (or info page if voters can't register online) (string)
      "onlineAccepted": WHETHER OR NOT VOTERS CAN REGISTER ONLINE (boolean)
      "lastMinuteAccepted": WHETHER OR NOT VOTERS CAN REGISTER DAY OF ELECTION (boolean)
      "emoji": Just some cute state themed-emoji (string)
      "notes": Optional, returns details about this state, like whether 16 year olds can register to vote, or voting rules for those with felonies
    },
  ]

```
 
 **GET STATE SPECIFIC INFO**
 
 `/states/[STATE ABBREVIATION].json`
 
 This returns the state that you passed in's specific object in the array above. So, the response looks like
 
```
  {
      "label": STATE NAME (string)
      "value": STATE ABBREVIATION (string)
      "deadline": GENERAL ELECTION VOTER REGISTRATION DEADLINE IN YYYYMMDD FORMAT (string)
      "primaryDeadline": PRIMARY ELECTION VOTER REGISTRATION DEADLINE IN YYYYMMDD FORMAT (string)
      "primaryDate": PRIMARY ELECTION DATE IN YYYYMMDD FORMAT (string)
      "url": OFFICIAL STATE VOTER REGISTRATION WEBSITE (or info page if voters can't register online) (string)
      "onlineAccepted": WHETHER OR NOT VOTERS CAN REGISTER ONLINE (boolean)
      "lastMinuteAccepted": WHETHER OR NOT VOTERS CAN REGISTER DAY OF ELECTION (boolean)
      "emoji": Just some cute state themed-emoji (string)
      "notes": Optional, returns details about this state, like whether 16 year olds can register to vote, or or voting rules for those with felonies
    },

```

**GET STATES THAT ALLOW REGISTRATION ON ELECTION DAY**

`/lastMinuteAccepted.json`

This returns an array of states (just their abbreviations, as strings) that allow for last minute voter registration on election day. (They all have their own rules so it might be a good idea to check their websites listed under their `state` object!)

```
['STATE', 'STATE_2', STATE_3']
```


**GET STATES THAT DON'T SUPPORT ONLINE VOTER REGISTRATION**

`/onlineNotAccepted.json`

This returns an array of states (also just their abbreviations, as strings) that require voters to register in person or via the mail (or whatever, just not online)!.

```
['STATE', 'STATE_2', STATE_3']
```


## Ideas/Issues:
Feel free to open any issues or ideas for new endpoints, new data to be added, etc in the issue section!

## Contact:
dedline-io@protonmail.com

 
