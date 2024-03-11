# Clone the project

git clone https://


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
