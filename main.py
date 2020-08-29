from domain import *
from message import *

from bs4 import BeautifulSoup
import requests
import time

if __name__ == "__main__":
    mangas = read_file()

    infos = read_FB_file()
    receiverName = infos[2]
    senderFB = UserFB(infos[0], infos[1])
    senderFB.loginFB()

    while True:
        for manga in mangas:
            url = manga.website
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")

            if str(soup).find("Chapter {}".format(manga.chapter)) == -1:
                continue
            else:
                message = str("Chapter " + str(manga.chapter) + " of " + manga.name + " is live <3")
                senderFB.sendFBMessage(message, receiverName)
                manga.chapter += 1

        update_file(mangas)
        time.sleep(1800) # sleep 30 minutes
