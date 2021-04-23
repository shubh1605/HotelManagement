# Hotel Management System
## Technologies Used
HTML, CSS and Bootstrap were used for front-end. Django is used for storing data at the backend on its inbuilt database sqlite3.
## Commands to run it on your device
### Cloning the project
Go to the directory in the command line where you want to clone the project and run the command:
```
git clone https://github.com/shubh1605/HotelManagement.git
```

### Creating a virtual environment
```
pip install virtualenv
```
* Go to the directory in the command line where you want to create a virtual environment and run the command.
```
virtualenv <venv_name>
```
### Activating the environment
* For Mac: 
```
source mypython/bin/activate 
```
* For Windows: 
```
<venv_name>\Scripts\activate.bat
```
### Install the project dependencies:
Go to the directory in command line where you cloned the project and run the command: 
```
pip install -r requirements.txt
```
### Run it on the server
To run it on the server, your Virtual Environment should be activated and then run the command:
```
python manage.py runserver
```
Go to google and enter the url that came up in the command line.
## Features of the project
* Pre-booking of a room based n its availability.
* Check availability of room of any category based on checkin and checkout dates of all other guests.
* Checkin facility.
* Checkout Facility.
* Cancel a booking if a person has not checked-in.
