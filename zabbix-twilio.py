__author__ = 'monkee'

#!/usr/bin/python2.7
from twilio.rest import TwilioRestClient
import yaml, sys, getopt


def main(argv):
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["phonenumber=","message="])
    except getopt.GetoptError:
      print 'zabbix-twilio.py -n <phonenumber> -m <message>'
      sys.exit(2)

    for opt, arg in opts:
          if opt == '-h':
             print 'zabbix-twilio.py -n <phonenumber> -m <message>'
             sys.exit()
          elif opt in ("-n", "--phonenumber"):
             phonenumber = arg
          elif opt in ("-m", "--message"):
             message = arg

    #get configuration
    try:
        configStr = open('config.yml','r')
        config = yaml.load(configStr)
    except BaseException, emsg:
        print('Cannot find or parse config file: ' + emsg)
        sys.exit(2)

    try:
        client = TwilioRestClient(config['account_number'], config['account_token'])
        client.messages.create(to=phonenumber, from_=config['from_number'],
                                     body=message)
        sys.exit()
    except BaseException, emsg:
         print('Cannot send message: ' + emsg)
         sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])