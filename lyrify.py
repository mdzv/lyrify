import requests

def GetLyrics(artist, title):
    artist = artist.strip().lower()
    title = title.strip().lower()
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("lyrics", None)
    return None

if __name__ == "__main__":
    program = True
    while program:
        artist = input("Enter artist name: ")
        title = input("Enter song title: ")
        
        lyrics = GetLyrics(artist, title)
        
        if lyrics:
            print("\n Lyrics \n")
            print(lyrics)
            program = False 
        else:
            print(f"\nLyrics cannot be found for: {artist} - {title}")
            retry = input("Do you want to try again? (y/n): ").strip().lower()
            if retry == "n":
                print("Exiting program.")
                program = False 
