# redink
1. This is a project for printing documents
2. Build from Django andd integrate with Razorpay for payment 
3. This project has a package named Poetry for managing packages and virtual environment 
4. To install packages required for this project use the command "poetry install" 
5. This will create a folder "venv" for virtual env , all the project will be install in this file
6. After installing packages run command "poetry shell"  to activate virtual env
7. then run "python manage.py makemigrations","python manage.py migrate" and python manage.py runserver" all one after another to start backend server 


#End Points 
1. file/upload (to upload file ) --only for local 
2. admin/ (for admin to access backend , admin must create superuser by running command "python manage.py "createsuperuser" and fill the credentials ) --for admin only 
3. success/ (for payment)-- no need to access automatic redirect

