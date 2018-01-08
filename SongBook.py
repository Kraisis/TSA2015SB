import requests
from bs4 import BeautifulSoup


def thishere(start):
    # Best so far
    while start < 1243:

        lead = "https://www.salvationist.org/"

        url = lead + "songbook.nsf/vw_us_nu?OpenView&Start=" + str(start) + "&Count=100"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        # # LINK
        # for title in soup.findAll('tr', {'height': '35'}):
        #     for thistitle in title.findAll('a'):
        #         href = thistitle.get('href')
        #         # print(lead + href)
        #
        # # NUMBER
        # for title in soup.findAll('tr', {'height': '35'}):
        #     for number in title.findAll('b'):
        #         # print(number.string)
        #         pass

        # NUMBER, TITLE, AND LINK

        for title in soup.findAll('tr', {'height': '35'}):
            for name in title.findAll('td'):
                print(name.string)
                numAndTitle = name.string
                file = open("TSA Songbook 2015.txt", 'a')
                file.write(numAndTitle + "\n")
                for thistitle in title.findAll('a'):
                    href = thistitle.get('href')
            file.write("\n")
            file.close()
            getfile(lead + href)

        start = start + 100


def getfile(url):

    source_code = requests.get(url)
    text = source_code.text
    soup = BeautifulSoup(text, "html.parser")

    file = open("TSA Songbook 2015.txt", 'a')
    for song in soup.findAll('font', {'face': 'Times New'}):
        print(song.string)
        link = song.string
        file.write(link + "\n")
    for extra in soup.findAll('i'):
        print(extra.text)
        file.write("\n" + extra.text)
        file.write("\n.......\n\n")
    file.close()


if __name__ == "__main__":
    # getfile("https://www.salvationist.org/songbook.nsf/vw_us_nu/B60E743744327B9A80256C870032D9D2?OpenDocument")
    thishere(1)











# def getNumber():
#     url = "https://www.salvationist.org/songbook.nsf/vw_us_nu?OpenView&Start=1&Count=100"
#     source_code = requests.get(url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text, "html.parser")
#
#     for title in soup.findAll('td', {'width': '35'}):
#         print(title.string)
#
#
# def getNumAndTitle(start):
#     # Best so far
#     while start < 1243:
#
#         url = "https://www.salvationist.org/songbook.nsf/vw_us_nu?OpenView&Start=" + str(start) + "&Count=100"
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, "html.parser")
#
#         for title in soup.findAll('tr', {'height': '35'}):
#             for newtitle in title.findAll('td'):
#                 # f = open('songs.txt', 'a')
#                 # f.write(newtitle.string[0:50] + "\n")
#                 print(newtitle.string)
#                 # print(title)
#         start = start + 100
#

# def link(start):
#     while start < 1243:
#         lead = "https://www.salvationist.org"
#         url = lead + "/songbook.nsf/vw_us_nu?OpenView&Start=" + str(start) + "&Count=100"
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, "html.parser")
#
#         for link in soup.findAll('a'):
#             href = link.get("href")
#             if "Document" in href:
#                 if len(lead + href) is 96:
#                     load = lead + href
#                     print(load)
#                     break
#         start += 100
#
#
#
# def last(start):
#     while start < 1243:
#         print("INNNNNN")
#         lead = "https://www.salvationist.org"
#         url = lead + "/songbook.nsf/vw_us_nu?OpenView&Start=" + str(start) + "&Count=100"
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, "html.parser")
#
#         for title in soup.findAll('tr', {'height': '35'}):
#             for newtitle in title.findAll('td'):
#                 # f = open('songs.txt', 'a')
#                 # f.write(newtitle.string[0:50] + "\n")
#                 print(newtitle.string)
#                 for booklink in soup.findAll('a'):
#                     href = booklink.get("href")
#                     if "Document" in href:
#                         thislink = lead + href
#                         if len(thislink) is 96:
#                             print(thislink)
#                             # break
#                             # break
#         start = start + 100
#
