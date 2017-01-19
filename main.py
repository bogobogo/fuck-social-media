#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from google.appengine.api import mail
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import feedparser
import datetime
from time import mktime, sleep

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/mail', methods=['GET'])
def send_mail():
	if request.method == 'GET':
		following = ['paulg', 'NadavEyalDesk','browniefed','RavivDrucker','sama', 'rabovitz', 'jasonfried', 'naval', 'realDonaldTrump', 'nntaleb', 'tul', 'dhh', 'shapiro',
					 'cpojer', 'chamath', 'patrickc', 'collision', 'gilamran', 'intelligibabble', 'grabbou', 'ccheever', 'guyeldar', 'ilyasu', 'DanielPink', 'OpenAI',
					 'waitbutwhy', 'ScottHYoung', 'bencasnocha', 'koltal', 'paultoo', 'Harjeet', 'yuris', 'ilikevests', 'getexponent', 'WixEng', 'amirtibon', 'notbrent', 'olivercameron', 'elonmusk', 'amsterdamski2']
		emaildata = []
		for name in following:
			sleep(0.3)
			page = feedparser.parse('http://twitrss.me/twitter_user_to_rss/?user=' + name)
			if page.bozo:
				logging.info('problem with name' + name)
				logging.info(page)		
			else:
				username = page['feed']['title'].split()[-1]
				for i in page.entries:
					emaildata.append({ 'username' : username, 'tweet' : i.title, 'date': i.published_parsed})
				
			
		emaildata.sort(key=lambda item:item['date'], reverse=True)
		yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
		dataFiltered = [i for i in emaildata if datetime.datetime.fromtimestamp(mktime(i['date'])) > yesterday]
		logging.info(dataFiltered)

		logging.info('1')
        ms = render_template('tweets_email.html', emaildata = dataFiltered)
        mail.send_mail(sender='Your daily elad tweets! <noreply@fuck-social-media.appspotmail.com>',
               to="bogo elad <bogomolnyelad@gmail.com>",
               subject = "Here is what people you care about shared",
	           body="""you should
	           use an email client that can render html dude
               """,
              html="<head> <meta charset='utf-8' /> </head>" + ms ) 
        
        return 'Hello World!'



@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500