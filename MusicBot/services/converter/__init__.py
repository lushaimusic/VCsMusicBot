from os import listdir, mkdir

if "raw_files" not in listdir():
    mkdir("raw_files")

from MusicBot.services.converter.converter import convert
