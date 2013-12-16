#!/usr/bin/python

__author__ = 'monkee'
from twilio.rest import TwilioRestClient
import yaml, sys, getopt


def main(argv):
    phonenumber = ''
    message = ''

    try:
      opts, args = getopt.getopt(argv,"h:n:m:",["phonenumber=","message="])
    except getopt.GetoptError:
      print 'Error: zabbix-twilio.py -n <phonenumber> -m <message>'
      sys.exit(2)

    for opt, arg in opts:
          if opt == '-h':
             print 'Usage: zabbix-twilio.py -n <phonenumber> -m <message>'
             sys.exit(2)
          elif opt in ("-n", "--phonenumber"):
             phonenumber = arg
          elif opt in ("-m", "--message"):
             message = arg

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
                                     body=message)
    except BaseException, emsg:
         print('Cannot send message: ' + str(emsg))
         sys.exit(2)

    sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])