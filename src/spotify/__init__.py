from .text import TextGenerator
from .inline import InlineGenerator
from spotipy.oauth2 import SpotifyClientCredentials
from os import getenv
import spotipy

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager,
    proxies={"https": getenv("PROXY_URL")},
)

text_generator = TextGenerator(sp)
inline_generator = InlineGenerator(sp)

generate_text = text_generator.generate
generate_inline = inline_generator.generate

__all__ = ["generate_text", "generate_inline"]
