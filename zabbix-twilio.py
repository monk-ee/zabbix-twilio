#!/usr/bin/python

__author__ = 'monkee'
from twilio.rest import TwilioRestClient
import yaml, sys, getopt


def main(argv):
    phonenumber = ''
    subject = ''
    message = ''

    try:
        phonenumber = argv[1]
        subject = argv[2]
        message = argv[3]
    except BaseException, emsg:
        print('Usage: zabbix-twilio.py <phonenumber> <subject> <message>: ' + str(emsg))
        sys.exit(2)

    #get configuration
    try:
        configStr = open('config.yml','r')
        config = yaml.load(configStr)
    except (OSError, IOError), emsg:
        print('Cannot find or parse config file: ' + str(emsg))
        sys.exit(2)

    try:
        client = TwilioRestClient(config['account_number'], config['account_token'])
        cm = client.messages.create(to=phonenumber, from_=config['from_number'],
                                     body=subject + ': ' +message)
    except BaseException, emsg:
         print('Cannot send message: ' + str(emsg))
         sys.exit(2)

    sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])