# pyportal-soundcloud
Python code for PyPortal - queries soundcloud for number of followers and number of listens to tracks.

Soundcloud does not make this easy. Their api does not accept new application registrations.
However, you can get the information if you're willing to work to find your IDs.

It first checks a user page, to get the follower count.
The it checks the number of listens for three separate tracks.

You have to manually enter the track IDs into the secrets file along with your user and client id.
I couldn't easly find a way to automatically get track IDs for a user.
I may look into this at a later date.

To get user, client and track IDs, I had to inspect the source of the respective pages.
The json data is usually present at the bottom.


