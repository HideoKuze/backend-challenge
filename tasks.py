#simple tasks to inform user when Db has been updated instead of having to run requests
#test
from celery import task, Celery
import datetime
from datetime import timedelta
import time
from datetime import date
import sqlite3


app = Celery('tasks', broker='amqp://guest@localhost//')

# --- bug here, tasks won't execute periodically, but work when run manually ---
CELERYBEAT_SCHEDULE = {
    'add-every-5-sec': {
        'task': 'tasks.show',
        'schedule': timedelta(seconds=5),
    },
}
# ------------------------------------------------------------------------------

CELERY_TIMEZONE = 'UTC'

#return a list of messages that were created at the current date
@app.task
def show():
	today = datetime.date.today()
	conn = sqlite3.connect('db.sqlite3')
	c = conn.cursor()
	c.execute("SELECT * FROM convoapp_inputinfo WHERE date_without_time = '%s'" % today)
	result = c.fetchall()
	return result
