# Python 2020 Workshop

Creating an eLearn auto-login & content extractor with password manager using AES encryption

## Idea

The idea is to automate the login process & automatically enter into selected subject's 'Course Content' page while extracting announcement information from the day. This is assisted with a password manager as storing your password in plain text is a cybersecurity risk.

## Modules Required

- pycryptodomex
- hashlib (already installed)
- selenium
- webdriver_manager

## Getting Started

First, clone the repo to your desired directory & install the Python modules required to run the script

```bash
git clone https://github.com/easonchai/python2020-workshop.git
cd python2020-workshop

```

OPTIONAL: Then, create a venv (virtual env). This is to avoid your python modules from interfering with other projects

```bash
python -m venv .\env

```

Install all required modules
<br />
If you used a venv, make sure you activate it first.

```bash
.\env\Scripts\activate

(env) <-- you should see this next to your terminal!
```

IMPORTANT: Finally, install the modules

```bash
pip install -r requirements.txt
```

Now we can start coding our Python Web Scraper! If you would like to view the full example files, checkout the `full-example` branch!
