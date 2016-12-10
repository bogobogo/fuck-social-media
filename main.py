import logging
from google.appengine.api import mail
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/mail', methods=['GET'])
def hello():
	if request.method == 'POST':
		ms = "דבר איתי כשאתה בבית".decode('utf-8')
	                ## if it isnt send mail to the mail and 
	    mail.send_mail(sender='Your daily tweets! <noreply@fuck-social-media.appspotmail.com>',
	           to="bogo elad <bogomolnyelad@gmail.com>",
	           subject="You were invited to join a notebook!",
	           body="""Dear NIV:

	            works just need to add hebrew support
	            I am free to talk now
	            daw
	            The legati Team
	            """,
	            html="<head> <meta charset='utf-8' /> </head><h3>" + ms + " </h3>") 


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500