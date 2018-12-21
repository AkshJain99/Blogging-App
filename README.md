# Mysite
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### A Project In Django (Python 3.x)
_A simple blogging platform for the modern Time._

#### This web application generates a simple but capable blog using Django. The platform allows authors to create text posts using a dedicated admin portal, and allows logged in users to post comments through a simple comment form.

_Create a beautiful and powerful blog in under 4mb!_

### [| Example Website >>>](https://mighty-reaches-82829.herokuapp.com/)

### Installation Process

* clone the repository at your preferred directory:
```
git clone https://github.com/AkshJain99/mysite.git

```

* create database 
```
sudo apt-get update
sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
sudo mysql_install_db
sudo mysql_secure_installation
mysql -u root -p
CREATE DATABASE project CHARACTER SET UTF8;
CREATE USER projectuser@localhost IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON project.* TO myprojectuser@localhost;
FLUSH PRIVILEGES;
exit
```
* enter the repository cloned.
```
cd mysite
```
* activate the virtual environment in the directory
```
pip --version
pip install virtualenv
virtualenv .
source bin/activate
```
* install mysqlclient
```
pip install django mysqlclient
```
* start the project
```
django-admin.py startproject myproject .
```
* install all the tools mentioned in requirements.txt
```
pip install -r requirements.txt
```
* migrate the created database
```
python3 manage.py makemigrations
python3 manage.py migrate
```
* create superuser
```
python manage.py createsuperuser
```
* run the server
```
python manage.py runserver
```
work on the localhost you just created.

### FAQ
___
  **Q.** What can it do? <br>
  **A.** Create simple yet beautiful text based blog posts with important features such as commenting and user credential generation.

  **Q.** Who is it for? <br>
  **A.** Anyone looking for a simple but capable solution for a text only blog such as quotes or philosophy.

  **Q.** What is in store for the future? <br>
  **A.** The sky is the limit!

## Requirements
___
  * `Python 3.xx`
  * `dj-database-url 0.5.0`
  * `Django 1.10.8`
  * `gunicorn 19.9.0`
  * `psycopg2 2.7.4`
  * `psycopg2-binary 2.7.4`
  * `python-decouple 3.1`
  * `whitenoise 4.0`

### Features To Be Improved And Implemented
___
See the issues for more about the ongoing developments
https://github.com/AkshJain99/mysite/issues
### Communtiy Gitter Channel
___

To get started, the first step is to meet the community. We use gitter to communicate, and there the helpful community will guide you. Gitter is an instant messaging service used by developers and users of GitHub. Gitter uses chatrooms, where developers can join in and can talk about a particular topic. Here is our gitter room link

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/Akshjain99/Lobby)


> _A Selected Ongoing Project for Kharagpur Winter Of Code-2018 (KWOC-2018) by IIT Kharagpur KOSS_
