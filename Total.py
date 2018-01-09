import requests
from bs4 import BeautifulSoup


# Main

def get_num_and_title(start):
    while start < 1243:

        lead = "https://www.salvationist.org/"

        url = lead + "songbook.nsf/vw_us_nu?OpenView&Start=" + str(start) + "&Count=100"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for title in soup.findAll('tr', {'height': '35'}):
            for name in title.findAll('td'):
                print(name.string)
                numAndTitle = name.string
                file = open("TSA2015SB.txt", 'a')
                file.write(numAndTitle + "\n")
                for thistitle in title.findAll('a'):
                    href = thistitle.get('href')
            # file.write("\n")
            file.close()
            get_song(lead + href)

        start = start + 100


def get_song(url):

    source_code = requests.get(url)
    text = source_code.text
    soup = BeautifulSoup(text, "html.parser")

    file = open("TSA2015SB.txt", 'a')
    for song in soup.findAll('font', {'face': 'Times New'}):  # Song
        link = song.text
        if link != "":
            file.write(link + "\n")
        else:
            print("TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'")

    for extra in soup.findAll('i'):  # Category and Author
        file.write("\n" + extra.text)

    file.write("\n\n\n.......\n")
    file.close()


if __name__ == "__main__":
    get_num_and_title(1)



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
