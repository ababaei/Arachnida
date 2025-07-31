import argparse
from urllib.parse import urljoin, urlparse
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import os

visited = []
maxdepth = 0
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

def is_image_valid(url):
    return url.lower().endswith(IMAGE_EXTENSIONS)

def dl_images(img_url, folder):
    try:
        response = requests.get(img_url, stream=True)

        if response.status_code == 200: #requete OK
            filename = os.path.basename(urlparse(img_url).path)
            filepath = os.path.join(folder, filename)
            urlretrieve(img_url, filepath)
            print(f"Downloaded: {img_url}")
        else:
            print(f"Failed to download: {img_url}")
    except Exception as e:
        print(f"Error downloading {img_url}: {e}")

def crawl(url, folder, depth):
    if depth == maxdepth or url in visited:
        return
    
    visited.append(url)

    print("____________________________________")
    print(f"crawling: {url} (current depth {depth})")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        #DL LES IMAGES
        for img in soup.find_all("img"):
            img_url = img.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                if is_image_valid(img_url):
                    dl_images(img_url, folder)

        #CONTINUER A CRAWL LES LIENS
        for link in soup.find_all("a"):
            href = link.get("href")
            if href:
                new_url = urljoin(url, href)
                crawl(new_url, folder, depth + 1)

    except Exception as e:
        print(f"failed to crawl {url}: {e}")    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Starting URL")
    parser.add_argument("-r", action="store_true", help="Enable recursive download")
    parser.add_argument("-l", type=int, default=5, help="Max recursion depth (default 5)")
    parser.add_argument("-p", default="./data", help="Download path (default ./data)")

    args = parser.parse_args()

    os.makedirs(args.p, exist_ok=True)

    print(args.l)


    if args.r:
        maxdepth = args.l + 1 
        crawl(args.url, args.p, 1)
    else:
        maxdepth = 2