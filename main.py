from bs4 import BeautifulSoup

with open("scrapper.html", encoding="utf8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

#print(soup)

#print(soup.prettify())

#print(soup.find_all("p"))

#print(soup(tag.get_text()))
git -v
#print(soup(tag.get("class")))

print(soup.select_one("p"))

print(soup.select("p"))
