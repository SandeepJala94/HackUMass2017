from bs4 import BeautifulSoup

url = r"C:\Users\Sandeep\Desktop\Hack UMass 2017\twitter-trump.html"
page = open(url)
soup = BeautifulSoup(page.read())

#soup = BeautifulSoup(open("C:\Users\Sandeep\Desktop\Hack UMass 2017\twitter-trump.html"), "html.parser")
    
print(soup.prettify())