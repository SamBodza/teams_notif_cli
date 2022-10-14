import argparse
from utility import send_teams_notif, send_error_msg,  send_succ_msg

parser = argparse.ArgumentParser()
parser.add_argument("webhook", type=str, help="the webhook url to your teams channel connector")
parser.add_argument("-s", "--successMessage", type=str, help="text to send with a success message")
parser.add_argument("-e", "--errorMessage", type=str, help="text to send with an error message")
parser.add_argument("-c", "--customMessage", type=str, help="send a custom message in the format "
                                                            "title;message;hex-colour")
args = parser.parse_args()

url = args.webhook
if args.successMessage:
    send_succ_msg(url, args.susuccessMessage)
elif args.errorMessage:
    send_error_msg(url, args.errorMessage)
elif args.customMessage:
    values = args.customMessage.split(';')
    send_teams_notif(url, values[0], values[1], values[2])
