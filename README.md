# TODO App using Flask and SQL Alchemy
A simple TODO app using Flask and SQL Alchemy for demonstrating the standard structure

To run in dev mode, first create the database
```bash
$ python
>>> from todoapp import db
>>> db.create_all()
```

then, set the flask environment variables and run the app
```bash
$ export FLASK_APP=todoapp
$ export FLASK_ENV=development
$ flask run
```

On windows using powershell
```bash
> $env:FLASK_APP="todoapp"
> $env:FLASK_ENV="development"
> flask run
```

You'll see the output as
```bash
 * Serving Flask app "todoapp"
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
