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

# Counter    
def file_len(data_text):
    with open (data_text) as f:
        for i, l in enumerate (f):
            pass
    return i + 1

def fileCount():
	filelog = []
	leastcommon = []
	with open(data_text) as logs:
		for line in logs:
			try:
				filelog.append(line[line.index("GET")+4:line.index("HTTP")]) # Files between GET requests and HTTP protocol
			except:
				pass
	counter = collections.Counter(filelog)
	for count in counter.most_common(1):														
		print("Most commonly requested file: {} with {} requests.".format(str(count[0]), str(count[1])))
	for count in counter.most_common():					# Occur once? - Least requested
		if str(count[1]) == '1':
			leastcommon.append(count[0])
	if leastcommon:										# Lots of single requests - we didnt want to print all so asked 													
		response = input("Looks like there were {} file(s) that were requested only once, show all? (yes/no)".format(len(leastcommon)))
		if response == 'yes' or response == 'Yes':
			for file in leastcommon:
				print(file)
# If the file isn't already there
if not os.path.isfile(data_text):
    # Download the file - save it to data_text
    urlretrieve(URL, data_text)

# Counter Stuff
total = 0
year_count = 0

for line in open(data_text):
    items = line.split()
    if len(items) < 9: # Total Logs
        continue

    year = items[3].split(':')[0][-4:] # Total logs since 1995
    if year == "1995":
        year_count = year_count + 1
    total = total + 1

# Regex Pattern
pattern = r'(.*?) - (.*) \[(.*?)\] \"(.*?) (.*?)\"? (.+?) (.+) (.+)'

# List per line of file
lines = open(data_text, 'r').readlines()