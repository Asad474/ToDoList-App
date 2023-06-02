#   ToDoList App



## Setup

The first thing to do is to clone the repository:

```bash
$ git clone https://github.com/Asad474/ToDoList-App.git
$ cd ToDoList-App
```

Create a virtual environment to install its dependencies and activate

```bash
$ python -m venv env(or any virtual environment name)
$ source env/scripts/activate
```

For running this project on local server, go to settings.py file in ToDoList folder and set

```bash 
DEBUG = True
```

Install the required packages from requirements.txt with the following command

```bash 
$ pip install -r requirements.txt
```


Running the app 

```bash 
python manage.py runserver
```