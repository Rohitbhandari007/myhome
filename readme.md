# ABOUT PROJECT

This project is built to control the lights of rooms. The technologies used are:
- Django (backend)
- Django Channels
- SQLite3 Database
- Vanilla JavaScript

# Project Setup 
- Clone the project
```
git clone https://github.com/Rohitbhandari007/myhome.git
```

 - Create a virtual environment

Linux/MacOS:
```
virtualenv env
source env/bin/activate
``` 
Windows: 
```
cd env\Scripts\activate
``` 

- Install the requirements
```
pip install -r requrements.txt
```

- Run redis on a docker container 
Make sure you have docker installed in your system
To enable layers for multiple instances to communicate with each other
```
sudo docker run --rm -p 6379:6379 redis:7
```

-  Run the migrations and start the server
```
python manage.py migrate
python mange.py runserver
```

