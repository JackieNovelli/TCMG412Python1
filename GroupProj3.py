import os
import urllib.request


def main():
    data_exists = os.path.exists("data.txt")
    if not data_exists:
        web_url = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
        raw_data = web_url.read().decode('utf-8')
        with open("data.txt", "w+") as myfile:
            myfile.write(raw_data)
    
    total = 0
    year_count = 0

    for line in open("data.txt"):
        items = line.split()
        if len(items) < 9:
            continue

        year = items[3].split(':')[0][-4:]
        if year == "1995":
            year_count = year_count + 1
        total = total + 1

    print("Logs since January 1995: " + str(year_count))
    print("Total Logs: " + str(total))


if __name__ == '__main__':
    main()