# Smart Home Light System
This project is built to control the lights of rooms. The technologies used are:
- Python 3.8.10
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

- Load the data in database using fixures
```
python manage.py loaddata all_fixtures.json
```

- Navigate to  http://127.0.0.1:8000/

    Now you can see the homes and navigate to each of them.


----
----
Additionally , after the setup is complete, to add and remove data ( homes/rooms/lights ) we can use django's admin panel 
- First we have to create a super user
```
python manage.py createsuperuser
```
- Navigate to : http://127.0.0.1:8000/admin/
- Log in with the superuser credentials
- You can see now do the basic curd of the entities using the panel
