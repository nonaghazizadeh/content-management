# Content-Management

## How to start
1. install vue/cli for front project
```
npm install -g @vue/cli
```
2. install python >= 3.8 with following [guide](https://www.python.org/downloads/) for back project
3. clone the project with following command
```
git clone git@github.com:youngbizman/Content-Management.git
```
4. go to `/back` and run following commands for creating virtualenv, active it, install requirments and run backend project
```
virtualenv venv
source venv/bin/activate
pip install -r requirments file
python manage.py migrate
python manage.py runserver
```
5. go to `/front/content-management` and run following commands for install packages, create nodemodules, package-lock.json and run frontend project
```
npm cache clean -f
rm -rf node-modules package-lock.json
npm run serve
```




