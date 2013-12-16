zabbix-twilio
=============
Just a little wrapper for the TwilioRestClient.

Requirements
===
 + twilio
 + getopts
 + yaml
 + sys

Installation
===
Download the zip from github and place:

    cp zabbix-twilio.py /etc/zabbix/alert.d/
    cp config.yml.sample /etc/zabbix/alert.d/config.yml

Configuration
===
API Credentials
The TwilioRestClient needs your Twilio credentials.

 + account_number:
 + account_token:
 + from_number


Usage
===
zabbix-twilio.py -n <phonenumber> -m <message>
