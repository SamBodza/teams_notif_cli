try:
    import pymsteams
except Exception as e:
    print(f'Install pymsteams using the commmand: "pip install pymsteams"')
    print(e)

from config import colours


def send_teams_notif(url, Title, msg, colour):
    # You must create the connectorcard object with the Microsoft Webhook URL
    myTeamsMessage = pymsteams.connectorcard(url)

    # add Title to Card
    myTeamsMessage.title(Title)

    # Add text to the message.
    myTeamsMessage.text(msg)

    # add colour to card
    myTeamsMessage.color(colour)

    # send the message.
    myTeamsMessage.send()


def send_error_msg(url, msg):
    send_teams_notif(url, 'ERROR', msg, colours['red'])


def send_succ_msg(url, msg):
    send_teams_notif(url, 'SUCCESS', msg, colours['green'])
