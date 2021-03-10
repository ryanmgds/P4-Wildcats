
# Covid DataBase
This is our trimester 2 project for AP CS Principles. We aspire to create an easy platform for users to get information on COVID-19.

## How to run our Covid Database
To access the website, visit _________ (the public IP address) OR clone it on your own machine:

Install all necessary packages with pip install -r requirements.txt

Run using python run.py

# College Board

## Big Idea 1 Creative Deployment
The journey to deployment began with a failure to connect using a rasperry pi. We then used problem solving to attempt the process at multiple houses to determine that the Pi was broken. We then attempted a seperate server using an old computer, only to finally decide on using AWS to create a live website.

## Big Idea 2 Data
Data curation and live updating was the main idea for our webiste, which we completed by pulling a live covid-19 database from a website API. We then were able to prove the effectiveness of this by showing a "current time of update" counter which only updated if the API did.

## Big Idea 3 Algorithms and Programming
Creating the website was a challenge that was achieved through html and python understanding. Creating the individual containers, changing color values, altering data, creating databases, creating blueprints, and networking was all tied together to create the website.

## Big Idea 4 Computing Systems and Networks
Through using a Simple Mail Transfer Protocol Client to communicate with python SMTP server, we were able to send emails to whoever interacts with the website via user input. The email contains information regarding COVID-19 data pertaining to the united states.

## Big Idea 5 Impact of Computing
Creating this website established a location for someone to be able to look at and recieve information that is genuinely valuable. As such, learning that computing can create opportunities and assist others is an incredibly valuable lesson.

# Complete Goals
-live data table with statistics (ryan)

-subscription option for users to get data (bryce)

-survey option for users to rate website (ryan)

-deployment on AWS (colin)



# Big Ticket Items
This information can be found on our scrum board: https://github.com/ryanmgds/P4-Wildcats/projects/1 



# Techincals

## Survey Table (CRUD)
You can find it in the navbar, and you can fill out a survey report, rating your experience on our website. You also have the option to leave your contact information. Contains data filtering, however this portion is still needs some work.

## COVID-19 Statistics
-data scraped using rapid.api

-data is oriented into table

-CSS used to style table and update button, to gather most accurate data

## Home page
-describes our intent with the website

-contains css for better look

## Subscription
-user can input email, and output will be an email with covid data to that person


# Individual and Class lectures
Lesson 1 Notes: digital information
Bits - binary value that holds information
Byte - group of 8 binary values
Binary: puts a 0/1 placeholder is position to represent base 2 numbers
Hexadecimal: base 16 group of numbers, represents 256 numbers, goes from 0-9 and A-F
Lossless and lossy compression are two types of encoding methods in which there is data that is either not lost or lost
Classes: object oriented programming uses classes to create functions and objects

Lesson 2 Notes: the internet
Internet: allows computing devices to share data with each other without the use of secondary memories
Packet: small amount of data that includes a source and destination
IP address: Internet protocol address assigns a numerical value to each device on a network
Computer system: a group of computing devices working together for a joint purpose
Computer network: a group of interconnected devices that share data
Router: helps a packet find a path that travels from sender to receiver
Bandwidth: the speed in which a packet travels from sender to receiver
OSI model: from top down it goes application, presentation, session, transport, network, data link, physical

Lesson 3 Notes: the internet pt 2
World wide web: pages you see when you are connected on a device
Internet: Network of computers that the web will run on
Network interface card: a wireless or wired computer hardware component that a computer to a network 
MAC address unique identifier that is assigned to a network interface controller
DHCP: a protocol that either assigns either a public ip that can be accessed anywhere, or a private ip address that can only be accessed in one spot
Main protocols used: HTTP and HTTPS 
Narrow wide model: from top down it goes application, transport, internet, network access

Lesson 4 Notes (I was presenter this day): extracting information from data

4 things involved with data: collection, processing, bias are important to consider when taking and analyzing data
Cleaning: fixing inaccurate, invalid, incomplete, and duplicate data
Dirty data: this can be prevented by having certain requirements on the inputs
Metadata: data about data that can be used to organize, identify and sort them
Causation: when 2 events are correlated because one event causes another
Correlation: when 2 events are related to each other 

Lesson 5 notes:  using programs with data
Programs using data: spreadsheets, data filterers, and visuals can help process data
Visuals: trends and graphs are easier to read and interpret 
Sorting data: filtering and highlighting data can make sorting the data easier
Modifying data: using a function to apply to a table of data can make modifying the data easier

Lesson 6 notes: data abstraction
String: ordered sequence of characters
List: ordered sequence of elements
Element: an individual value in a list that is assigned to be variable
Index: a way to reference elements that starts at 1 for AP test
Data abstraction: it provides separation between abstract and concrete aspects of data
Complexity: data abstraction can make programs easier to run and manage

Lesson 7 notes: AP test requirements
Program code: submit 1 pdf file that contains all code, have comment by someone other than team
Requirements: lists, inputs, algorithms, procedures, outputs
Video: talk about all the aspects in the code, use captions instead of voice narration, convert to mp4, has to be under a minute
Written response: cannot be collaborative

Lesson 8 notes: lists
List: a way to store sets of data in one variable
Element: a value in a list assigned to a unique index, and is considered a variables
Index: numbers used for referencing the elements in a list, and starts at 1 on the AP exam
For loops: for loops can be run to do functions to the entire list
Append: adds element to end of list
Clear: clears list
Copy: returns copy of the list
Count: returns number of elements with specified value
Extend: adds elements of a list to the end of another list
Insert: adds element at a specified position
Pop: removes the element at a specified position
Remove: removes the item with the specified value
Reverse: reverses the order of the list
Sort: sorts the list

# P4-Wildcats Creators
Colin Tran, Ryan Moghaddas, Bryce Modugno, Gavin Theriault





