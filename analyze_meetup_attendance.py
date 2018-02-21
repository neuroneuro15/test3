import requests
import pandas as pd


url = 'https://api.meetup.com/SuperPythonTalks/events?&status=past'
r = requests.get(url)

df = pd.DataFrame(r.json())
df = df[['name', 'local_date', 'yes_rsvp_count']]