# To run the project
we will need to create to clone the project

` $ git clone git@github.com:AmroAly/python-challenge-two.git `

then we will need to create an env

`cd python-challenge-two && virtualenv env`

then activate our env

` $ source env/bin/activate`

then install our dependencies

` $ pip install -r requirements.txt` 

let's make our migrarions and migrate

` $ manage.py makemigrations `

` $ manage.py migrate`

lastly let's run our server on port 8000

` $ manage.py runserver`