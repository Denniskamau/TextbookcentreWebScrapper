
import PySimpleGUI as sg
import random
from .bookscrapper import BookScrapper


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
                bookScrapper = BookScrapper()
                
                data = bookScrapper.initializeScapping(values[0])
                sg.Print('Starting sraping this may take some time depending on your Network')
                
                counter = bookScrapper.startScrapping(data[0],data[1])
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
    
    
    
scrapper = DentoScrapper()
scrapper.initialization()