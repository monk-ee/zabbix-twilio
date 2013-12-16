#!/usr/bin/python

__author__ = 'monkee'
from twilio.rest import TwilioRestClient
from datetime import date
import yaml, sys,logging


def main(argv):
    phonenumber = ''
    subject = ''
    message = ''
    timestamp = str(date.today())

    #get configuration
    try:
        configStr = open('config.yml','r')
        config = yaml.load(configStr)
    except (OSError, IOError), emsg:
        print('Cannot find or parse config file: ' + str(emsg))
        sys.exit(2)

    #logging for debug really you can set to logging.INFO to chill it out
    logging.basicConfig(filename=config['logfile'],level=logging.DEBUG)

    try:
        phonenumber = argv[1]
        subject = argv[2]
        message = argv[3]
    except BaseException, emsg:
        logging.warning(timestamp + ': Missing Arguments: ' + str(emsg) + ' : '+str(argv))
        sys.exit(2)



    try:
        client = TwilioRestClient(config['account_number'], config['account_token'])
        cm = client.messages.create(to=phonenumber, from_=config['from_number'],
                                     body=subject + ': ' +message)
        logging.debug(timestamp + ': ' + phonenumber + ' / ' + subject + ' / ' + message + ': ' + str(cm))
    except BaseException, emsg:
         logging.warning(timestamp + ': Cannot send message: ' + str(emsg))
         sys.exit(2)

    sys.exit()

if __name__ == "__main__":
   main(sys.argv)