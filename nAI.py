#!/usr/bin/python

import wolframalpha
import sys

# Get a free API key here http://products.wolframalpha.com/api/
# This is a fake ID, go and get your own, instructions on my blog.
app_id='3PRYPU-18WR6WQLRU'

client = wolframalpha.Client(app_id)

query = raw_input(">")
res = client.query(query)

if len(res.pods) > 0:
    answer = ""
    pod = res.pods[1]
    if pod.text:
        answer = pod.text
    else:
        answer = "I have no answer for that"
    # to skip ascii character in case of error
    texts = texts.encode('ascii', 'ignore')
    print answer
else:
    print "Sorry, I'm unable to answer that."
