import requests
import sys

mainurl = sys.argv[1]
url = mainurl
getlen = len(mainurl)
thingy = getlen - 4
dummy, dummy2, extension = mainurl.split(".", maxsplit=3)
print(extension)
print(url)
r = requests.get(url, allow_redirects=True)
print("Saving as 'Download'")
saver = "download" + "." + extension
print(saver)
open(saver, 'wb').write(r.content)