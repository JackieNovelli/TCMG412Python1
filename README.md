# TCMG412Python1

## Python Project 1
The goal of this project is to familiarize yourself with Python syntax, and some basic tasks that are common in systems 
programming and administration. The program will be invoked from the command line on a fresh Linux machine, so if you 
introduce any library dependencies beyond the Python Standard Library (not recommended), you must provide very clear 
instructions to recreate your environment. I would suggest using Vagrant (Links to an external site.) or a GCP (Links to
an external site.) VM to develop in Linux if you are on a Windows machine. Another option is to install the Windows 
Subsystem for Linux (Links to an external site.) and setup a Python environment (Links to an external site.). It is your
responsibility to ensure the program runs as expected in the operational environment described.

Here’s the scenario: you work for a medium sized company that sells widgets directly to consumers through brick-and-mortar
retail stores. The marketing department wants to try a new promotional campaign to ramp up direct internet sales, but needs
better data about current traffic to your website. Your boss has asked you to take the HTTP server logs from the webserver
and provide some analytics to Marketing.

## Python Project 2

Marketing was very happy with the data you provided them. Now they want more. They have asked that you answer more questions
so they have a better idea about the nature of the visitors that are coming to the company website.

Marketing is asking for answer to the following questions:

How many requests were made on each day? 
How many requests were made on a week-by-week basis? Per month?
What percentage of the requests were not successful (any 4xx status code)?
What percentage of the requests were redirected elsewhere (any 3xx codes)?
What was the most-requested file?
What was the least-requested file?

Finally, it was decided that the logs should be broken into separate files by month, so that staff in the marketing department
can do further analysis. Your program should split the log file into 12 smaller files, where the data stored in each file are
the log events for a single month. These should be written to disk in the same directory as your program file, in a logical
and consistent manner.

Your program should be created and developed using GitHub (I will be examining the commit logs to see your work). When the
project is due, submit your repository URL so I can clone the repo and test your program.

## Python Project 3

The goal of this project will be to build a simple REST API in Python and containerize it using Docker. This container image
will then be uploaded to the Docker public repository and I will be downloading this image to run it in my local Docker 
environment for testing. You are free to use any Python web framework you want, but I strongly recommend Flask 
(http://flask.pocoo.org (Links to an external site.)) for its simplicity and ease of use. Your API should run on the default
Flask port (5000) and expose the following URIs:

/md5/<string>
This endpoint will return the MD5 hash of the string that is passed as the input. Ex.: for a string of Hello World the MD5 
hash should be b10a8db164e0754105b7a99be72e3fe5. Don’t forget to handle spaces and other special HTTP characters correctly!

/factorial/<int>
This endpoint will return the factorial (product of the integer and all integers below it) for the integer that is passed 
as input. If the input is not a positive integer, the output should contain and error description.

/fibonacci/<int>
This input will return an array of integers with all the Fibonacci numbers (in order) that are less than or equal to the 
input number. If the input is not a positive integer, return an error description. 

/is-prime/<int>
This endpoint will return a boolean value depending on whether the input is a prime number. Again, return a descriptive 
error if the input is invalid.

/slack-alert/<string>
This endpoint is the only one that has a side-effect. Your API should attempt to post the value of the input into a 
Slack channel in our class Slack team, then return a boolean value that indicates whether the message was successfully 
posted to the channel. 
