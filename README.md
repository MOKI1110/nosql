
# nosql

Sample Blog...

# setup

python -m venv myenv
myenv\scripts\activate  source env/bin/activate
pip install django==3.2
pip install djongo
pip install pymongo==3.12.1
django-admin startproject <projectname>
cd <projectname>
django-admin startapp <appname>
python -m ensurepip --upgrade
python -m pip install setuptools
python manage.py migrate
python manage.py runserver
