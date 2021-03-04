from urllib.request import urlretrieve
import os
import re
import collections 
import urllib.request

months_count ={
  "Jan": 0,
  "Feb": 0,
  "Mar": 0,
  "Apr": 0,
  "May": 0,
  "Jun": 0,
  "Jul": 0,
  "Aug": 0,
  "Sep": 0,
  "Oct": 0,
  "Nov": 0,
  "Dec": 0
}

janlogs=open("january.txt", "a+"); 
feblogs=open("february.txt", "a+"); 
marlogs=open("march.txt", "a+"); 
aprlogs=open("april.txt", "a+"); 
maylogs=open("may.txt", "a+"); 
junlogs=open("june.txt", "a+");
jullogs=open("july.txt", "a+"); 
auglogs=open("august.txt", "a+"); 
seplogs=open("september.txt", "a+")
octlogs=open("october.txt", "a+"); 
novlogs=open("november.txt", "a+"); 
declogs=open("december.txt", "a+")   

i=0

redirectCounter = 0
errorCounter = 0

# URL of the file
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
# Save our log file
data_text = 'http_access_log'

#Call URL and save to local
data_exists = os.path.exists(data_text)
if not data_exists:
    web_url = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
    raw_data = web_url.read().decode('utf-8')
    with open(data_text, "w+") as myfile:
        myfile.write(raw_data)