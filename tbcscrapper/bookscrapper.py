# Import the required liblaries
import os
import random
import urllib.request
import urllib.request
import PySimpleGUI as sg
from bs4 import BeautifulSoup





class BookScrapper():
    def initializeScapping(self,url):
        # Set the url of the page you want to scrap for data
        urlpage = url
        page = urllib.request.urlopen(urlpage)
        soup = BeautifulSoup(page, 'html.parser')
        producet_list = soup.find('div',class_="prod-list-view")
        items = producet_list.find('section')
        book_list = items.find('ol',class_="product-list row")
        book_data = book_list.findAll('li',class_='col-xs-6 col-md-3')
        number_of_books = len(book_data)
        print('INFO: Number of results', number_of_books)
        return number_of_books,book_data
        # self.startScrapping(book_data)
        
    def startScrapping(self,items,book_data,):
        print('INFO: scrapping started')
        path = "/home/dennis/Desktop/books"
        self.createDirectory(path)
        counter = 1
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
                if counter == items:
                    print('INFO: finished')
                    return counter
                else:
                    print('INFO: saved {} {}'.format(title.text,counter))
                    counter +=1
            except Exception as e:
                print('ERROR:',e)
                
    def createDirectory(self,path):
        # Create directory to store the images
        try:
            os.mkdir(path)
        except Exception as e:
            print ("Creation of the directory failed",e )
        else:
            print ("Successfully created the directory %s " % path)