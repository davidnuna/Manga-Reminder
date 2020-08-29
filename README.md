# Manga-Reminder
Simple python application that announces the user through a facebook message when a new chapter from his list of mangas is released.

# Setting up the files
In order to have a valid script, you need to create a facebook account and send a friend request to your personal account (and obviously accept it).
After doing that,  replace the lines in the file "info.txt" with:
- the username of the newly created facebook account ( can be found in the general settings )
- the password of the newly created facebook account
- the name that people can find your personal account by
Finally, in the "mangas.txt" file enter in a CSV format the name of the manga, the future chapter to be released and the website where the chapter should be visible in the future. Do this, on each line, for every manga you want to be checked.

# Installation and Usage:
Clone the repository:
```
git clone https://github.com/neutralove/Manga-Reminder.git
```
Install beautifulsoup4
```
pip install beautifulsoup4
```
Install lxml
```
pip install lxml
```
Install fbchat
```
pip install fbchat
```
