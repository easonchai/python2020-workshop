# 🐍 Python 2020 Workshop

Creating an eLearn auto-login & content extractor with password manager using AES encryption

## 💡 Idea

The idea is to automate the login process & automatically enter into selected subject's 'Course Content' page while extracting announcement information from the day. This is assisted with a password manager as storing your password in plain text is a cybersecurity risk.

## 🗺️ Getting Started

First, clone the repo to your desired directory

```bash
git clone https://github.com/easonchai/python2020-workshop.git
cd python2020-workshop

```

Then, create a [venv](https://docs.python.org/3/library/venv.html) (virtual environment) within the directory. A virtual environment is a Python environment that is isolated (contained) by itself. All packages installed will not interfere with other Python projects on your computer. This is really handy if you create a bunch of Python projects! Otherwise, you might run into some unknown issues!

```bash
python -m venv .\env

```

**IMPORTANT: Activate your venv first!**
<br />

```
.\env\Scripts\activate

(env) <-- you should see this next to your terminal!
```

Next, install all required modules. This command basically reads through the requirements.txt file and installs all the required modules so you have an exact copy of my files to follow along the workshop!

```bash
pip install -r requirements.txt
```

Now we can start coding our Python Web Scraper! If you would like to view the full example files, checkout the [full-example](https://github.com/easonchai/python2020-workshop/tree/full-example) branch!

## File Structure

Now, we can definitely program everything in one file, but that will get really messy and complicated. The best way is to split up groups of functions into separate files. For example, the encryption should be in its own Python file, while the scraper should be in another. That makes sense right?<br /><br />
I've structured the project to use five(5) different files:

| File          | Function                                                                                          |
| ------------- | ------------------------------------------------------------------------------------------------- |
| main.py       | Main entry point (we will only interact with this file!)                                          |
| encryption.py | Handle password encryption/decryption                                                             |
| scraper.py    | Handle eLearn scraping using selenium                                                             |
| setup.py      | Setup the config.ini                                                                              |
| boot.ps1      | This is not a Python file, but can be used with Powershell as a script to run on Windows Startup! |

Feel free to start fresh if you do not want to use these files!
