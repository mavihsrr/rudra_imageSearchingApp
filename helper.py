import requests
import re
http_pattern="^(http|https)://"
def download_images(urls):
    for index,url in enumerate(urls):
        result = re.match(http_pattern, url)
        if result:
            r = requests.get(url, allow_redirects=True)
            open(f'/Users/arya/Desktop/test/scrapper/tmp/image{index}.png', 'wb').write(r.content)