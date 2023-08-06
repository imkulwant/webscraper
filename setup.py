from setuptools import setup, find_packages

setup(
    name='web_scraper',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'web_scraper = web_scraper.main:main',
        ],
    },
    author='Kulwant Singh',
    author_email='singh.kulwant@gmx.com',
    description='A generic web scraping project in Python',
    url='https://github.com/imkulwant/web-scraper',
    license='MIT',
)
