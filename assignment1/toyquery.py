############################################
# Python for Data Science
# ---------------------------------
# Created by  : Adam Nguyen
# Updated by  : Adam Nguyen
# Created at  : 03/01/2014
# Updated at  : xx/xx/xxxx
# Description : Intro to Data Science
############################################

import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")

pyresponse = json.load(response)

results = pyresponse["results"]

print results[0]


