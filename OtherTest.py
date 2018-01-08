import requests
from bs4 import BeautifulSoup


def thishere(start):
    # Gets Tunes and Meter
    while start < 1243:
        url = "https://www.salvationist.org/songbook.nsf/vw_us_nu/269FAF55D0C9B1AE8025668E00338104?OpenDocument"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for tunes in soup.findAll('td', {'width': '510'}):
            print(tunes.text + "\n")

        start = start + 100000


def get_num_and_title(start):
    while start < 1243:

        lead = "https://www.salvationist.org/"

        url ="https://www.salvationist.org/songbook.nsf/vw_us_nu/366556C70DAADF0880256689005C8FDD?OpenDocument"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for title in soup.findAll('tr', {'height': '35'}):
            for name in title.findAll('td'):
                print(name.string)
                numAndTitle = name.string
                file = open("TSA Songbook 2015.txt", 'a')
                file.write(numAndTitle + "\n")
                for thistitle in title.findAll('a'):
                    href = thistitle.get('href')
                    print(href)
            # file.write("\n")
            file.close()
            get_song(lead + href)

        start = start + 100000


def get_song(url):

    source_code = requests.get(url)
    text = source_code.text
    soup = BeautifulSoup(text, "html.parser")

    file = open("TSA Songbook 2015.txt", 'a')
    for song in soup.findAll('td', {'id': 'mainContent'}):  # Song
        for right in song.findAll('p'):
            before = right.text[:-220]
            print(before.replace("Add to Powerpoint Creator \n\n\n", ""))
            break

    # for extra in soup.findAll('i'):  # Category and Author
    #     file.write("\n" + extra.text)
    #     # print(extra.text)
    # for tunes in soup.findAll('td', {'width': '510'}):  # Tune(s) and the Meter
    #     file.write("\n\n" + tunes.text)


if __name__ == "__main__":
    get_song("https://www.salvationist.org/songbook.nsf/vw_us_nu/B3148EE98408522080256689005C8F64?OpenDocument")
