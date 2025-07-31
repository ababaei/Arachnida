# Spider & Scorpion

Spider is a tool to automatically extract information from the web. More precisely images.

Scorpion is a tool to analyze these files and read there metadata. 

## Installation

Use the package manager to install beautifulsoup4 if needed.

```bash
pip install beautifulsoup4
```

## Usage

```bash
# show help
python3 spider.py --help

# recursively downloads the images in a URL received as a parameter.
python3 spider.py -r URL

# indicates the maximum depth level of the recursive download. If not indicated, it will be 5.
python3 spider.py -r -l [N] URL

#indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used.
python3 spider.py -r -p [PATH] URL
```

## Test case
```bash
python3 -m http.server 5500
```

## Warning

This project is only for educational purpose. This exercise is from the school 42 cybersecurity basic training project.