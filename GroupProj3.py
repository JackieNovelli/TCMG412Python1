import os
import urllib.request

def main():
    dataExists = os.path.exists("data.txt") 
    if not dataExists:
        webUrl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
        rawData = webUrl.read().decode('utf-8')
        with open("data.txt", "w+") as myfile:
            myfile.write(rawData)


        year = items[3].split(':'[0][-4:]
        if year == "1995":
            year = year + 1
        total = total +1

print("Logs since January 1995: " + str( YEAR))
print("Total Logs: " + str( TOTAL))

if __name__ == '__main__':
    main()
