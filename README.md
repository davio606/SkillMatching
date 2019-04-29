# Student Skill Matching v. 1.0.0

Contributors: David Yoon, Vismita Uppalli, Sri Jayakumar, Zijia Zeng, Geoff Hicks

This website was created for CS 3240 at the University of Virginia with the purpose of allowing UVA students to find specific study partners with certain skills and majors.
See working version at [http://student-skill-matching.herokuapp.com/]

## For Sherriff Only:
Go to [http://student-skill-matching.herokuapp.com/login/]. 

Username: Sherriff 

Password: helloworld!

/login/ was made specifically for the use of Professor Sherriff

After you login, you will be sent to the homepage that is only accessible for authenticated users, if you wish to look at the homepage for non-authenticated users (people that are not signed in), just click this [http://student-skill-matching.herokuapp.com/]. 

The profile tab is where you can edit your own profile. We also have a suggestion box page where users can submit a suggestion that goes to our master email (this master email is also used for the google calendars feature that we implemented in our calendars page). The email access is:

Email: studentskillmatching@gmail.com

Password: segfaultstrategists

If you would like to test the messaging feature, you can message yourself, as this has the same functionality as messaging someone else. 

## Install 

git clone https://github.com/UVA-CS3240-S19/project-102-segfault-strategists.git 

Make sure to pip install all requirements from requirements.txt

To start development server run command:
"python3 manage.py runserver"

The local development server will be running at:
http://127.0.0.1:8000/

## Features

### Advanced Search Features
Grasp allows user to search for potential study buddies in an advanced and efficient way. Find study buddies based on username, major, or skill.

### Built in Messaging
Grasp allows users to message others in a convenient manner. Users can compose a new message to anybody, view incoming messages, and view messages they have sent.

### Joint Calendar System
Grasp allows users to notify others of group events on a joint calendar. Simply type in the name of the event, a description, the date, and time.

### Suggestions
Grasp allows users to add suggestions to the website under the 'suggest' tab. For every suggestion made, an email is sent
to studentskillmatching@gmail.com with password: segfaultstrategists. 