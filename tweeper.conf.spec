###
### Tweeper.conf will specify how this input streams data.
###


[default]
# this is just the endpoint where we are sending the data
splunk_server = hostname or IP

# The following are the metadata fields for Splunk
host = twitter
source = twitter_script
sourcetype = json

[twitter]
# These need to be created on apps.twitter.com
CONSUMER_KEY=IBRCP73vfttLZbYXGi3ECtUsd
CONSUMER_SECRET=GPdMwqYusMrhEt9ayFycFWCtSpCDnDpgiHrC0CqQN3pxs5iTYD
ACCESS_KEY=20492124-OgZFrSnAbroIYt0hMpZhRCl8zkkc0SlawtOU8FC08
ACCESS_SECRET=ttNXG4CoSBO2QlwVw1pMmhy2LK4lfiTjQ9wH2cn2ArDIQ

# this is a comma separated list of things we want to follow on twitter
# basically any tweets that match these terms come in
# then twitter gives us 1% of the data - which is still a lot :)
TARGETS=bernie,hillary,trump

[HEC]
# these naturally are created in the HTTP Event Collector input in splunk_server
HEC_TOKEN=B5EC1B67-9CDA-4B12-B15B-9ABD807D1DE4
HEC_PORT=8088
