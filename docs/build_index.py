#!/usr/bin/env python

import glob
import os

entry = '      <li><a href="examples/%s">%s</a></li>'

with open("index.html") as f:
    data = f.read()

start = data.find("\n", data.find('<ul id="examples">'))
end = data.rfind("\n", 0, data.find('</ul>', start))

os.chdir("examples")
data = data[:start+1] + "\n".join(entry % (filename, os.path.splitext(filename)[0]) for filename in sorted(glob.glob("*.html"))) + data[end:]
os.chdir("..")

with open("index.html", "w") as f:
    f.write(data)

