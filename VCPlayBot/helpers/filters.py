from typing import List
from typing import Union

from pyrogram import filters

from VCPlayBot.config import COMMAND_PREFIXES

other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
