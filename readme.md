# Clone the project
```
git clone https://github.com/Rohitbhandari007/myhome.git
```

# Create a virtual environment

```
virtualenv env
```

Linux/MacOS:
```
source env/bin/activate
``` 
Windows: 
```
cd env\Scripts\activate
``` 

# Install the requirements
```
pip install -r requrements.txt
```
# Run the sever and apply migrations
```
python manage.py migrate
python mange.py runserver
```

# Run redis on a docker container 
To enable layers for multiple instances to communicate with each other
```
sudo docker run --rm -p 6379:6379 redis:7
```