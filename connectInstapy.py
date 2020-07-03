from instapy import InstaPy

# Connect & Login
session = InstaPy(username="usr", password="pwd")
session.login()

# Unfollow 400 accounts who dont follow back at random, sleep 10 min
session.unfollow_users(amount=100, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
