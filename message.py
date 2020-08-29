import fbchat

class UserFB(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.client = None

	def loginFB(self):
		self.client = fbchat.Client(self.username, self.password)

	def sendFBMessage(self, message, otherUser):
		receiver = self.client.searchForUsers(otherUser)[0]
		sent = self.client.sendMessage(message, thread_id = receiver.uid)

def read_FB_file():
    with open("info.txt", "r") as file:
        lines_in_file = file.readlines()
        username = lines_in_file[0]
        password = lines_in_file[1]
        receiverFB = lines_in_file[2]
        return [username, password, receiverFB]

