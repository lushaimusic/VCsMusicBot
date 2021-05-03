# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from os import path
import asyncio

from helpers.errors import FFmpegReturnCodeError


async def convert(file_path: str) -> str:
    out = path.basename(file_path)
    out = out.split(".")
    out[-1] = "raw"
    out = ".".join(out)
    out = path.basename(out)
    out = path.join("raw_files", out)

    if path.isfile(out):
        return out
    try:
        proc = await asyncio.create_subprocess_shell(
            f"ffmpeg -y -i {file_path} -f s16le -ac 1 -ar 48000 -acodec pcm_s16le {out}",
            asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        await proc.communicate()

        if proc.returncode != 0:
            raise FFmpegReturnCodeError("FFmpeg did not return 0")

        return out
    except:
        raise FFmpegReturnCodeError("FFmpeg did not return 0")
