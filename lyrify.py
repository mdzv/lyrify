import requests

def GetLyrics(artist, title):
    artist = artist.strip().lower()
    title = title.strip().lower()
    
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("lyrics", "Lyrics not found.")
    else:
        return "Error: Cannot find the lyrics."
    
    
if __name__ == "__main__":
    artist = input("Enter artist name: ")
    title = input("Enter song title: ")
    
    lyrics = GetLyrics(artist, title)
    print("\n Lyrics \n")
    print(lyrics)
