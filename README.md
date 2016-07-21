# Tweeper

What: A HTTP event collector based twitter input for Splunk (6.4+)
Why: I was lacking a simple way to stream twitter (1%) into Splunk for a sentiment analysis project
How: Use tweepy to create a stream listener, track some words, send them in via the HEC.

## Setup
Just look at `tweeper.conf.example` to see where you will put your
 - consumer key
 - consumer secret
 - access keys
 - access secret
that you generated from [apps.twitter.com](apps.twitter.com).

You just need `tweepy` and `requests` installed.

Simply pip install, e.g.:
```
pip install --user tweepy
```

Secondly, you'll need to set your
 - splunk endpoint (ip or dns via http)
 - HTTP Event Collector (HEC) token
 - HTTP Event Collector (HEC) port

Optionally, you can also set the Splunk metadata:
 - host
 - source
 - sourcetype
 - index

If you don't set the metadata, the defaults will be applied from when you setup
the HEC as a data input.

Finally, just run it as a script, no arguments.

# License
MIT
