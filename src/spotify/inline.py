from typing import Any
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

from spotify.generator import Generator


class InlineGenerator(Generator):
    def generate_track(self, track: Any) -> list[InlineQueryResultArticle]:
        title = track["name"]
        description = ", ".join(map(lambda x: x["name"], track["artists"]))
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
        return [
            InlineQueryResultArticle(
                id=track["id"],
                title=title,
                description=description,
                input_message_content=InputTextMessageContent(
                    message_text=target_message
                ),
                thumbnail_url=image_url,
            )
        ]

    def generate_album(self, album: Any) -> list[InlineQueryResultArticle]:
        title = album["name"]
        description = ", ".join(map(lambda x: x["name"], album["artists"]))
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
        return [
            InlineQueryResultArticle(
                id=album["id"],
                title=title,
                description=description,
                input_message_content=InputTextMessageContent(
                    message_text=target_message
                ),
                thumbnail_url=image_url,
            )
        ]

    def generate_artist(self, artist: Any) -> list[InlineQueryResultArticle]:
        title = artist["name"]
        image_url = artist["images"][0]["url"]
        return [
            InlineQueryResultArticle(
                id=artist["id"],
                title=title,
                description=title,
                input_message_content=InputTextMessageContent(
                    message_text=f"""
        <a href="{image_url}">&#8204;</a><a href="{artist["external_urls"]["spotify"]}">{title}</a>

{artist["external_urls"]["spotify"]}
        """
                ),
                thumbnail_url=image_url,
            )
        ]
