from typing import TypeVar
from urllib.parse import urlparse
import spotipy

T = TypeVar("T")


class Generator:
    def __init__(self, sp: spotipy.Spotify) -> None:
        self.sp = sp

    def generate(self, link: str) -> T:
        url = urlparse(link)
        if url.netloc != "open.spotify.com":
            return self.generate_error(
                "Link should start with https://open.spotify.com", "error_invalid_link"
            )
        path = list(filter(lambda x: x, url.path.split("/")))
        match path[0]:
            case "track":
                track = self.sp.track(path[1])
                return self.generate_track(track)
            case "album":
                album = self.sp.album(path[1])
                return self.generate_album(album)
            case "artist":
                artist = self.sp.artist(path[1])
                return self.generate_artist(artist)
        return self.generate_error(
            "We don't support this link type yet 😢", "error_unknown_link"
        )

    def generate_track(self, track: spotipy.Spotify) -> T:
        raise NotImplementedError

    def generate_album(self, album: spotipy.Spotify) -> T:
        raise NotImplementedError

    def generate_artist(self, artist: spotipy.Spotify) -> T:
        raise NotImplementedError

    def generate_error(self, message: str, id: str) -> T:
        raise NotImplementedError
