import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = str(input("which year do you want to travel to? write the date in the format yyyy-mm-dd:")).strip()
year = date.split("-")[0]

url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")

billboard_top_100_h3 = soup.select("li ul li h3")
billboard_top_100 = [song.get_text() for song in billboard_top_100_h3]
for song in billboard_top_100:
    updated_song = song.strip()
    index = billboard_top_100.index(song)
    billboard_top_100[index] = updated_song



sp_username = "Munachimso Arubaleze"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="a48677ff6e0e4cfc8cede13a5481e1da",
        client_secret="d45ecdf23bc94c70bd41b2dfe77dfaa8",
        show_dialog=True,
        cache_path="token.txt",
        username=sp_username,
    )
)
user_id = sp.current_user()["id"]
params= {
    "q": f"track:{billboard_top_100[0]} year:{year}",
    "type": "album",

}
song_uris = []
playlist = sp.user_playlist_create(user=user_id, public=False, name=f"{date} Billboards top 100",
                                   description="A playlist containing"
                                               "the top 100 songs from the date "
                                               "specified on the playlist title")

for song in billboard_top_100:
    list_of_songs = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = list_of_songs["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in spotify. Skipped")
    else:
        sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)




