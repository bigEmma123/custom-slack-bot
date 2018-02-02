import os
import time
import re

from slackclient import SlackClient


#Instantiate
token=os.environ.get('SLACK_BOT_TOKEN')
slack_client=SlackClient(token)


#bot id
botId=None

if slack_client.rtm_connect(with_team_state=False):
    botId=slack_client.api_call("auth.test")
    print(botId['user']+" with id "+botId['user_id']+" is running smoothly")
    botId=botId['user_id']

    print(slack_client.rtm_read())
    while True:
        slack_client.rtm_read()
        time.sleep(0.4)

else:print("Well there was an error so hmmmm  yh")

print(token)
