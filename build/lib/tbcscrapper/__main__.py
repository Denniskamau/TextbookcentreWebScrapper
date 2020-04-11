# from bookscrapper import BookScrapper
from .textbookcentreGUI import DentoScrapper

def main():

    scrapper  = DentoScrapper()
    scrapper.initialization()

if __name__ == "__main__":
    main()