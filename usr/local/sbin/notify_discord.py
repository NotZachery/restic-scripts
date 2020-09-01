#!/usr/bin/env python3
import requests, sys, json, subprocess

if __name__ == "__main__":
        somedata = subprocess.getoutput("systemctl status %s" % sys.argv[1])
        data = {'content': "[ <@&ROLEID> ] \nThere was a failure running the following systemd unit ```%s```" % somedata}
        requests.post("https://discordapp.com/api/webhooks/xxxxxx", json=data)

