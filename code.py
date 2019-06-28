"""
This example will access the Souncloud API.
It will first get the number of listeners for a user.
It will then get the number of listens for three separate tracks.

"""
import time
import board
from adafruit_pyportal import PyPortal

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

CAPTION = "soundcloud.com/your_user_uri"

# pylint: disable=line-too-long

# The uri of the user account to obtain the followers.
MAIN_DATA_SOURCE = "http://api.soundcloud.com/users/"+secrets['soundcloud_user_id']+"?client_id="+secrets['soundcloud_client_id']

# This is the uri of the tracks to display. I've kept them separate for now, for simplicity.
LAST_TRACK_DATA_SOURCE = "http://api.soundcloud.com/tracks/"+secrets['soundcloud_track_id_last']+"?client_id="+secrets['soundcloud_client_id']
SECOND_TRACK_DATA_SOURCE = "http://api.soundcloud.com/tracks/"+secrets['soundcloud_track_id_second']+"?client_id="+secrets['soundcloud_client_id']
THIRD_TRACK_DATA_SOURCE = "http://api.soundcloud.com/tracks/"+secrets['soundcloud_track_id_third']+"?client_id="+secrets['soundcloud_client_id']

# The json locations where the data is stored
FOLLOWERS_DUMMY = ["first_name"]        # This doesn't really matter. It expects two peices of information
FOLLOWERS_COUNT = ["followers_count"]
PLAYBACK_TITLE = ["title"]
PLAYBACK_COUNT = ["playback_count"]
# pylint: enable=line-too-long

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
main_json_path=(FOLLOWERS_DUMMY, FOLLOWERS_COUNT)
track_json_path=(PLAYBACK_TITLE, PLAYBACK_COUNT)

pyportal = PyPortal(url=MAIN_DATA_SOURCE,
                    json_path=main_json_path,
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/background.bmp",
                    text_font=cwd+"/fonts/Collegiate-50.bdf",
                    text_position=((15, 129),(60, 180)),
                    text_color=(0x000000, 0x000000),
                    caption_text=CAPTION,
                    caption_font=cwd+"/fonts/Collegiate-24.bdf",
                    caption_position=(10, 220),
                    caption_color=0x000000)


# track the last value so we can play a sound when it updates
last_follower = 0

while True:
    # Followers:
    # A limitation of the PyPortal object is it must have an equal number of
    # text objects and json fields. So in this case, get some dummy information,
    # then replace the text with the word followers after. It's a bit ugly.
    # Alternatively, do this outside of a pyportal object manually.
    try:
        pyportal._json_path = main_json_path
        dummy, followers = pyportal.fetch(MAIN_DATA_SOURCE)
        pyportal.set_text("Followers:", index=0)
        followers = int(followers)
        print("followers:", followers)
        if last_follower < followers:  # another follower
            print("New Follower!")
            pyportal.play_file(cwd+"/coin.wav")
        last_follower = followers
    except RuntimeError as e:
        print("Some error occured, retrying! -", e)
    except ValueError as e:
        print("Value error occured, retrying! -", e)
    except:
        print("An unknown error occured, retrying!")

    time.sleep(30)

    # Tracks
    # This is done one at a time for readability.
    # Could easily be done in a loop.
    # Update the uri and the json path.
    # All the required data is updated automatically,
    # so no need to update the text.
    try:
        pyportal._json_path = track_json_path
        title, listeners = pyportal.fetch(LAST_TRACK_DATA_SOURCE)
        listeners = int(listeners)
        print("title:", title)
        print("listeners:", listeners)
    except RuntimeError as e:
        print("Some error occured, retrying! -", e)
    except ValueError as e:
        print("Value error occured, retrying! -", e)
    except:
        print("An unknown error occured, retrying!")

    time.sleep(30)

    try:
        pyportal._json_path = track_json_path
        title, listeners = pyportal.fetch(SECOND_TRACK_DATA_SOURCE)
        listeners = int(listeners)
        print("title:", title)
        print("listeners:", listeners)
    except RuntimeError as e:
        print("Some error occured, retrying! -", e)
    except ValueError as e:
        print("Value error occured, retrying! -", e)
    except:
        print("An unknown error occured, retrying!")

    time.sleep(30)

    try:
        pyportal._json_path = track_json_path
        title, listeners = pyportal.fetch(THIRD_TRACK_DATA_SOURCE)
        listeners = int(listeners)
        print("title:", title)
        print("listeners:", listeners)
    except RuntimeError as e:
        print("Some error occured, retrying! -", e)
    except ValueError as e:
        print("Value error occured, retrying! -", e)
    except:
        print("An unknown error occured, retrying!")

    time.sleep(30)

