# Python 2020 Workshop

Creating an eLearn auto-login & content extractor with password manager using AES encryption

## Idea

The idea is to automate the login process & automatically enter into selected subject's 'Course Content' page while extracting announcement information from the day. This is assisted with a password manager as storing your password in plain text is a cybersecurity risk.

## Modules Required

- pycryptodomex
- hashlib (already installed)
- selenium
- webdriver_manager

## File Structure

main -> entry point
setup -> creates config.ini
encryption -> handles encryption/decryption
scraper -> handles scraping

## Getting Started

First, clone the repo to your desired directory & install the Python modules required to follow the workshop

```
git clone https://github.com/easonchai/python2020-workshop.git
pip install selenium webdriver_manager pycryptodomex
```
