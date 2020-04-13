from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='dentoscrapper',
    version='0.1.3',
    description='Useful tools for scrapping textbook centre images',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Dennis Kamau',
    author_email='denniskamau3@gmail.com',
    keywords=['WebSrapper', 'Data Mining', 'Textbook centre','Web scrapping'],
    url='https://github.com/Denniskamau/TextbookcentreWebScrapper',
    download_url='https://pypi.org/project/dento-scrapper/'
)

install_requires = [
    'pysimplegui',
    'beautifulsoup4'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)