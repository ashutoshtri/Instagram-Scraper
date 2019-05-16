# Instagram Media and Caption Scraper

The program scrapes media from public Instagram Pages and extracts the captions corresponding to the post, please use this appropriately and responsibly.

## Set Up
Step 1: Install Python from : 
`https://www.python.org/downloads/`

Step 2: Install pip by typing the following command in Terminal : 
`$ python get-pip.py`

## Installation

Step 1: Install Instagram Scraper:
`$ pip install instagram-scraper`

To Upgrade:
`$ pip install instagram-scraper --upgrade`

Be sure to cd the folder to a specified location and download other files in the same location.

## Usage

Program will result in a CSV file (openable in Excel/Numbers) which will seggregate the captions based on the respective photo.

( DO NOT CHANGE THE LOCATION, remember to download all files in the same location.)

Step 1: Download `InstagramScrappingData.py` (main file)

Step 2: To execute the file, open terminal and run : `python InstagramScrappingData.py <username to scrape>`

If user is private, you need an account that follows the user, then:

`python InstagramScrappingData.py <username to scrape> -u <approved follower username> -p <approved follower password>`

For more commands, please do check: 

https://github.com/rarcega/instagram-scraper (credits)

----------------
Executed files will be ready.

Do let me know if this works.
Cheers.
