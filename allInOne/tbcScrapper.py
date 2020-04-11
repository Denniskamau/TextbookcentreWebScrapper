#!/usr/bin/env python
import os
import random
import urllib.request
import urllib.request
import PySimpleGUI as sg
from bs4 import BeautifulSoup




class DentoScrapper():  
    def initialization(self):
        sg.theme('DarkAmber')# Add a touch of color
        # All the stuff inside your window.
        layout = [  [sg.Text('Welcome to Textbook centre scraper')],
                    [sg.Text('Enter the URL to scrap for data'), sg.InputText()],
                    [sg.Button('Start'), sg.Button('Cancel')] ]

        # Create the Window
        window = sg.Window('Dento Scrapper', layout)
        
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event in (None, 'Cancel'):	# if user closes window or clicks cancel
                break
            if values[0] is not None:
                print('You entered ', values[0])
                
                sg.Print('Loading books from:',str(values[0]))
                
                
                data = self.initializeScapping(values[0])
                sg.Print('Starting sraping this may take some time depending on your Network')
                
                counter = self.startScrapping(data[0],data[1])
                print('counter',counter)
                if counter == data[0]:
                    sg.Print('Number of books found:',str(data[0]))
                    sg.Print('Finished scrapping data from:',str(values[0]))
                
        window.close()


    def progress(self,items,data):
        print('INFO: Loader started')
        textList = ["loading..", "fetching data..", "Scrapping.."]
        progressDur = 100000
        layout = [[sg.Text(textList[0], key="progtext")],
                  [sg.ProgressBar(progressDur, orientation='h', size=(20, 20), key='progbar')],
                  [sg.Cancel()]]
        
        
        # create the Window
        window = sg.Window('Dentos scrapper', layout)
        
        # loop that would normally do something useful
        for i in range(progressDur):
            # check to see if the cancel button was clicked and exit loop if clicked
            event, values = window.Read(timeout=0)
            if event == 'Cancel' or event is None:
                break
                # update bar with loop value +1 so that bar eventually reaches the maximum
            bookScrapper.startScrapping(data)
            if i ==10000:
                window.Element('progtext').Update("Starting..")
            if i == progressDur * .2:
                window.Element('progtext').Update(textList[random.randrange(len(textList))])
            if i == progressDur * .3:
                window.Element('progtext').Update(textList[random.randrange(len(textList))])
            if i == progressDur * .4:
                window.Element('progtext').Update(textList[random.randrange(len(textList))])
            if i == progressDur * .5:
                window.Element('progtext').Update(textList[random.randrange(len(textList))])
            if i == progressDur * .6:
                window.Element('progtext').Update(textList[random.randrange(len(textList))])
            if i == progressDur * .7:
                window.Element('progtext').Update(textList[random.randrange(len(textList))])
            if i == progressDur * .8:
                window.Element('progtext').Update(textList[random.randrange(len(textList))])
            window.Element('progbar').UpdateBar(i + 1)
        # done with loop... need to destroy the window as it's still open
        window.Close()
        
        
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
        current_directory = os.getcwd()
        print('curr',current_directory)
        path = os.path.join(current_directory,r"books")
        print('path',path)
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
    
if __name__ == '__main__':
    scrapper = DentoScrapper()
    scrapper.initialization()