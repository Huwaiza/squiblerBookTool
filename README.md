Setup Project


Clone the project using following command

    git clone git@github.com:Huwaiza/squiblerBookTool.git

Make sure you have python 3 installed in your system


Open terminal and run command

    python3 --version

If there is not python3 version in your system, please visit https://www.python.org/downloads/


Check if you have pip in you OS

    pip --version or python3 -m pip --version

If it says no module named pip please visit https://pip.pypa.io/en/stable/installation/#get-pip-py

Create Virtual Environment

    python -m venv {{virtual_env}}

Activate Environment

    source {{virtual_env}}/bin/activate
    
Install Required Dependencies

    pip install -r requirements.txt
 
Run following command to migrate django models to database

    python manage.py makemigrations
    python manage.py migrate
    
Run following command to create superuser   

    python manage.py createsuperuser

After creating super user login to url
127.0.0.1/admin
after signing in hit the url 127.0.0.1/docs where you will see every API used in system,
you can interact with them and can also use them via postman


