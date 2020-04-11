# Import the required liblaries
import os
import urllib.request
import urllib.request
from bs4 import BeautifulSoup

# Set the url of the page you want to scrap for data
urlpage = 'https://textbookcentre.com/catalogue/category/text-books/secondary-school/?page=7'
page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')
producet_list = soup.find('div',class_="prod-list-view")
items = producet_list.find('section')
book_list = items.find('ol',class_="product-list row")
book_data = book_list.findAll('li',class_='col-xs-6 col-md-3')
print('INFO: Number of results', len(book_data))

# Create directory to store the images
path = "/home/dennis/Desktop/books"
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)
    
for book in book_data:
    try:
        product = book.find('div',class_="product")
        url = product.find('a')
        full_url = url.get('href')
        page = urllib.request.urlopen('https://textbookcentre.com'+full_url)
        soup = BeautifulSoup(page, 'html.parser')
        data = soup.find('article',class_='product_page')
        image = data.find('div',id='product-images')
        image = image.find('a')
        image_url = image.get('href')
        title_data = data.find('div',class_='col-sm-6 product_main')
        title = title_data.find('h1')
        fullpath = os.path.join(path,title.text) 
        #Save the book
        urllib.request.urlretrieve('https://textbookcentre.com'+image_url, "{}/{}.jpg".format(path,title.text))
        print('INFO: saved {}'.format(title.text))
    except Exception as e:
        print('ERROR:',e)