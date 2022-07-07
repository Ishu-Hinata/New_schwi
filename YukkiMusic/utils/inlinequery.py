from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause Stream",
            description=f"Pause the current playout on group call.",
            thumb_url="https://telegra.ph/file/98b875508c50b684fa242.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume Stream",
            description=f"Resume the ongoing playout on group call.",
            thumb_url="https://telegra.ph/file/b1f023be3bd5bdb8b7b5b.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Mute Stream",
            description=f"Mute the ongoing playout on group call.",
            thumb_url="https://telegra.ph/file/8637f7e38cd0dbd0014e5.jpg",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="Unmute Stream",
            description=f"Unmute the ongoing playout on group call.",
            thumb_url="https://telegra.ph/file/295c6d8204146ce43bce4.jpg",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="Skip Stream",
            description=f"Skip to next track. | For Specific track number: /skip [number] ",
            thumb_url="https://telegra.ph/file/10f954f184ee655f07a7b.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End Stream",
            description="Stop the ongoing playout on group call.",
            thumb_url="https://telegra.ph/file/6dba63e1ad35ea526fa68.jpg",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="Shuffle Stream",
            description="Shuffle the queued tracks list.",
            thumb_url="https://telegra.ph/file/5cfd543a3e49aae4dadc4.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Seek Stream",
            description="Seek the ongoing stream to a specific duration.",
            thumb_url="https://telegra.ph/file/a42d7b017db10c21a6525.jpg",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="Loop Stream",
            description="Loop the current playing music. | Usage: /loop [enable|disable]",
            thumb_url="https://telegra.ph/file/f3d3b249e7e66dbd95638.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
