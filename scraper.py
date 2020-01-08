import datetime
from itertools import dropwhile, takewhile

from instaloader import Instaloader, Profile

loader = Instaloader()

PROFILE = input("Enter the username of the profile you would like to scan: ")

posts = Profile.from_username(loader.context, PROFILE).get_posts()

since = input("Enter the date of where you'd like to start (mm/dd/yyyy): ")
since_dates = since.split('/')

until = input("Enter the date of where you'd like to end (mm/dd/yyyy): ")
until_dates = until.split('/')

SINCE = datetime.datetime(int(since_dates[2]), int(since_dates[0]), int(since_dates[1]))
UNTIL = datetime.datetime(int(until_dates[2]), int(until_dates[0]), int(until_dates[1]))

for post in dropwhile(lambda p: p.date > UNTIL, takewhile(lambda p: p.date > SINCE, posts)):
    print(post.date)
    loader.download_post(post, PROFILE)

class Scraper():

    def __init__(self, profile):
        self.profile = profile

    def get_post_data(self, begin, end):
        begin = datetime.datetime(int(since_dates[2]), int(since_dates[0]), int(since_dates[1]))
