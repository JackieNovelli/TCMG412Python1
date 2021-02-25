import os
import urllib.request

def main():
    dataExists = os.path.exists("data.txt") 
    if not dataExists:
        webUrl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
        rawData = webUrl.read().decode('utf-8')
        with open("data.txt", "w+") as myfile:
            myfile.write(rawData)


if __name__ == '__main__':
    main()
