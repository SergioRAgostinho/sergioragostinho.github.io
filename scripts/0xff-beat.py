#!/usr/bin/env python3

"""
0xff-beat.py: A script for fetching automatically all episodes from mixcloud
and create the appropriate files in the source build tree.

Warning: At the moment the folder to create the files is hard coded
"""

__author__ = "Sérgio Agostinho"
__copyright__ = "Copyright 2018"
__credits__ = ["Sérgio Agostinho"]
__version__ = "1.0.0"
__maintainer__ = "Sérgio Agostinho"
__email__ = "sergio(dot)r(dot)agostinho(at)gmail(dot)com"


import os.path
import urllib.request
import json
import re
from slugify import slugify

def fetch_json_data(url):
    with urllib.request.urlopen(url) as req:
        if req.getcode() != 200:
            print("Error: Request returned code " + r.getcode())
            return None
        data = json.loads(req.read().decode())
        return data

def create_episode_file(episode, folder):

    # Assemble full name
    date = episode['created_time'].split('T')[0]
    filename = folder + '/' + date + '-' + slugify(episode['name']) + ".md"
    print("Creating episode '" + episode['name'] + "' in '" + filename + "'")
    with open(filename, "w") as out:

        # Write front matter
        out.write("---\n")
        out.write('title: "' + episode['name'] + '"\n')

        # Date
        date = episode['created_time'].split('T')[0]
        out.write("date: " + date + "\n")

        # tags
        out.write("tags: [")
        for tag in episode['tags']:
            if tag != episode['tags'][0]:
                out.write(", ")
            out.write(slugify(tag['name']))

        out.write("]\n")

        # Header image
        out.write('header:\n  teaser: "' + episode['pictures']['320wx320h'] + '"\n')

        # Close Front Matter
        out.write("---\n")

        # Fetch description and parse urls properly
        desc = fetch_json_data("https://api.mixcloud.com" + episode['key'])['description']
        urls = re.findall("(?P<url>https?://[^\s]+)", desc)
        for url in urls:
            desc = desc.replace(url, "[" + url + "](" + url + ")")

        out.write("\n" + desc + "\n")

        # Write iframe with player
        out.write('\n<iframe width="100%" height="120" src="'
                  'https://www.mixcloud.com/widget/iframe/?'
                  'hide_cover=1&light=1&feed=%2F0xff-beat%2F' + episode['slug'] +
                  '%2F" frameborder="0" ></iframe>\n')


# Pull content from website go through the episodes
data = fetch_json_data("https://api.mixcloud.com/0xff-beat/cloudcasts/?limit=100")
episodes = data['data']
folder = "/home/sergio/Development/website/_off-beat"

for ep in episodes:
    # Create the name for checking the file
    date = ep['created_time'].split('T')[0]
    file_name = folder + '/' + date + '-' + slugify(ep['name']) + ".md"

    # if it doesn't exist create it
    if not os.path.exists(file_name):
        create_episode_file(ep, folder)
