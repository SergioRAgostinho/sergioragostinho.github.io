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


import sys
import os.path
import urllib.request
import json
import re
import unicodedata

def slugify(string):
    tmp = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore');
    tmp = str(re.sub(r'[^\w\s-]', '', tmp.decode()).strip().lower())
    return re.sub(r'[-\s]+', '-', tmp)

def fetch_json_data(url):
    with urllib.request.urlopen(url) as req:
        if req.getcode() != 200:
            print("Error: Request returned code " + r.getcode())
            return None
        data = json.loads(req.read().decode())
        return data

def generate_file_content(episode):
    # Initialize empty string
    content = ''

    # Write front matter
    content += "---\n"
    content += 'title: "' + episode['name'] + '"\n'

    # Date
    date = episode['created_time'].split('T')[0]
    content += "date: " + date + "\n"

    # tags
    content += "tags: ["
    for tag in episode['tags']:
        if tag != episode['tags'][0]:
            content += ", "
        content += slugify(tag['name'])

    content += "]\n"

    # Header image
    content += 'header:\n  teaser: "' + episode['pictures']['320wx320h'] + '"\n'

    # Close Front Matter
    content += "---\n"

    # Fetch description and parse urls properly
    desc = fetch_json_data("https://api.mixcloud.com" + episode['key'])['description']
    urls = re.findall("(?P<url>https?://[^\s]+)", desc)
    for url in urls:
        desc = desc.replace(url, "[" + url + "](" + url + ")")

    content += "\n" + desc + "\n"

    # Write iframe with player
    content += '\n<iframe width="100%" height="120" src="' \
               'https://www.mixcloud.com/widget/iframe/?' \
               'hide_cover=1&light=1&feed=%2F0xff-beat%2F' + episode['slug'] + \
               '%2F" frameborder="0" ></iframe>\n'

    return content;

def is_content_equal(filename, content):
    with open(filename, "r") as file:
        return str(file.read()) == content

# Pull content from website go through the episodes
data = fetch_json_data("https://api.mixcloud.com/0xff-beat/cloudcasts/?limit=100")
# data = fetch_json_data("https://api.mixcloud.com/0xff-beat/cloudcasts/?limit=6")
episodes = data['data']
script_path, _ = os.path.split(os.path.abspath(sys.argv[0]))
folder = script_path + '/../_off-beat'

# Iterate through all episodes to check if any needs to be updated
for i, ep in enumerate(episodes):

    # Fetch post content
    content = generate_file_content(ep)

    # Assemble full name
    date = ep['created_time'].split('T')[0]
    filename = folder + '/' + date + '-' + slugify(ep['name']) + ".md"

    # Check if file needs to be written
    exists = os.path.exists(filename)
    if exists:
        different = not is_content_equal(filename, content)


    if not exists:
        print("Creating episode '" + ep['name'] + "' in '" + filename + "'")
    elif different:
        print("Updating episode '" + ep['name'] + "' in '" + filename + "'")

    sys.stdout.write("\r%d%% - " % (i*100/len(episodes)))
    sys.stdout.flush()

    if not exists or different:
        with open(filename, 'w') as out:
            out.write(content)

# Force new line
print('')
