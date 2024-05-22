from RGBMatrixDriver import RGBMatrixOptions, RGBMatrixArguments
import collections
import argparse
import os
import debug
import datetime
from tzlocal import get_localzone

# get local timezone
local_tz = get_localzone()

def get_file(path):
  dir = os.path.dirname(__file__)
  return os.path.join(dir, path)

def center_text(text_width,center_pos):
  return abs(center_pos - (text_width / 2))

def split_string(string, num_chars):
  return [(string[i:i + num_chars]).strip() for i in range(0, len(string), num_chars)]

def args():
  sb_parser = RGBMatrixArguments()
  sb_parser.add_argument("--fav-team", action="store", help="ID of the team to fallow. (Default:8 (Montreal Canadien)) Change the default in the config.json", type=int)

  return sb_parser.parse_args()

def deep_update(source, overrides):
    """Update a nested dictionary or similar mapping.
    Modify ``source`` in place.
    """
    for key, value in list(overrides.items()):
        if isinstance(value, collections.Mapping) and value:
            returned = deep_update(source.get(key, {}), value)
            source[key] = returned
        else:
            source[key] = overrides[key]
    return source

def convert_time(utc_dt):

  local_dt = datetime.datetime.strptime(utc_dt, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc).astimezone(local_tz)
  return local_tz.normalize(local_dt)  # .normalize might be unnecessary

def getsize(font, text):
    return font.font.getsize(text)[0][0]
