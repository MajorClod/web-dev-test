# web-dev-test

This test includes a simple Python Django API for development purposes.  You do not need to know any python or django to complete this test.

## Setup

The following instructions are for a Windows based environment.  Linux or Mac instructions will be similar but may use different commands.  Google is your friend :)

- Install Python 3.8 64-bit on your computer and ensure python.exe is available from your command line
- Install Python virtual environments using pip install virtualenv
- Check out this repository to a folder
- In that folder, create a new virtual environment using the command virtualenv venv
  - This will create a sub folder called venv with a python virtual environment inside 
- Mount the virtual environment using venv\scripts\activate (windows only)
- With your virtual environment mounted, install the project dependencies using pip install -r requirements.txt
- After installation, try running the project using python manage.py runserver
- Navigate to http://localhost:8000 and you should see Welcome to index.html inside your browser
- You're now setup and ready for the test
- PS: There is an API endpoint for accounts - see if you can find it
