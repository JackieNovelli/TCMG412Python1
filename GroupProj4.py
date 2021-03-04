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

# Iterate over the lines
for line in lines:
    # Match pattern to the line
    match = re.match(pattern, line)

    # If no match, skip this loop
    if not match:
        continue

    match.group(0) # The original line
    match.group(3) # The timestamp
    timestamp = match.group(3)
    month = timestamp[3:6]
    months_count[month] += 1
    match.group(7) # Status codes
    
    if (match.group(7)[0] == "3"):
        redirectCounter += 1
    elif (match.group(7)[0] == "4"):
        errorCounter += 1
    if (month == "Jan"): 
        janlogs.write(line)
    elif (month == "Feb"): 
        feblogs.write(line)
    elif (month == "Mar"): 
        marlogs.write(line)
    elif (month == "Apr"): 
        aprlogs.write(line)
    elif (month == "May"): 
        maylogs.write(line)
    elif (month == "Jun"): 
        junlogs.write(line)
    elif (month == "Jul"): 
        jullogs.write(line)
    elif (month == "Aug"): 
        auglogs.write(line)
    elif (month == "Sep"): 
        seplogs.write(line)
    elif (month == "Oct"): 
        octlogs.write(line)
    elif (month == "Nov"): 
        novlogs.write(line)
    elif (month == "Dec"): 
        declogs.write(line)
    
    else:
        continue

# ANSWER STUFF
print("~Request Complete!~")
print("Logs since January 1995: " + str(year_count))
print("Total Logs: " + str(total))
tResponses = file_len(data_text)
print("Average number for month:", round(tResponses/12,2))
print("Average number for week: ",round(tResponses/52,2))
print("Average number for day: ", round(tResponses/365,2))
print("Month Count:", months_count)
print("Total number of redirects:",redirectCounter)
print("Percentage of all requests that were redirects (3xx): {0:.2%}".format(redirectCounter/tResponses))
print("Total number of Errors:",errorCounter)
print("Percentage of client error (4xx) requests: {0:.2%}".format(errorCounter/tResponses))	
fileCount()
