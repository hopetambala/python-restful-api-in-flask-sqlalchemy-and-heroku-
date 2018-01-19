# MicroRestful API
Here's a MicroRestful API to store a directory of people's first and last names. 

*Runs on https://flask-microrestful.herokuapp.com/*

## To Run the Application
$ python run.py

## To Develop the Application
### Step 1:
Setup Environment

```python
$ virtualenv our_app
$ cd our_app
$ source bin/activate
``` 
* '$ deactivate' once you're in environment if you want to leave*

```python
$ pip install flask
$ pip install flask-sqlalchemy
```

### Step 2:
Develop and Run Application
Project Structure

the_project/
	my_app/
	    - __init__.py
	    baseline/
	        - __init__.py
	        - models.py
	        - views.py
	- run.py
```python
$ python run.py
```

### Step 3: 
Test Methods and Develop Resful API with Postman

*create requirements.txt*
*microdatabases/*
```python
$ pip freeze > requirements.txt
```
### Step 4:
Deploy to Heroku
*Remember to be in virtualenv when installing*

```python
$ source bin/activate
$ pip install flask gunicorn
```
Create your app in Heroku
Then
```python
$ heroku login
$ cd the_project
$ git init
$ heroku git:remote -a name-of-heroku-app
```
Push the app to heroku!
```python
$ git add .
$ commit -am "our project commit!"
$ git push heroku master
```

### Step 5 and beyond:
Expand Application features and create web/mobile front-end
*Future*

##Tools
Python 2.7
Sublime Text 2
Flask
Postman for API Development

