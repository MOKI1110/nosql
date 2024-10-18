
# nosql

Sample Blog...

# setup

python -m venv myenv
myenv\scripts\activate      git=> source env/bin/activate
pip install django==3.2
pip install djongo
pip install pymongo==3.12.1
pip install --upgrade setuptools
django-admin startproject <projectname>
cd <projectname>
django-admin startapp <appname>
python manage.py migrate
python manage.py runserver
