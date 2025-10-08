from typing import Any

from spotify.generator import Generator


class TextGenerator(Generator):
    def generate_track(self, track: Any) -> str:
        title = track["name"]
        image_url = track["album"]["images"][0]["url"]

        artists_with_urls = ", ".join(
            map(
                lambda x: f"<a href='{x['external_urls']['spotify']}'>{x['name']}</a>",
                track["artists"],
            )
        )

        target_message = f"""
        <a href="{image_url}">&#8204;</a><a href="{track["external_urls"]["spotify"]}">{title}</a> – {artists_with_urls}

    {track["external_urls"]["spotify"]}
        """
        return target_message

    def generate_album(self, album: Any) -> str:
        title = album["name"]
        artists_with_urls = ", ".join(
            map(
                lambda x: f"<a href='{x['external_urls']['spotify']}'>{x['name']}</a>",
                album["artists"],
            )
        )
        image_url = album["images"][0]["url"]
        target_message = f"""
        <a href="{image_url}">&#8204;</a><a href="{album["external_urls"]["spotify"]}">{title}</a> – {artists_with_urls}

    {album["external_urls"]["spotify"]}
        """
        return target_message

    def generate_artist(self, artist: Any) -> str:
        title = artist["name"]
        image_url = artist["images"][0]["url"]
        return f"""
        <a href="{image_url}">&#8204;</a><a href="{artist["external_urls"]["spotify"]}">{title}</a>

    {artist["external_urls"]["spotify"]}
        """
