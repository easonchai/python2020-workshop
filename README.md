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

Modify the subjects.txt to fit your needs, follwing the format below. Make sure there are no spaces between the comma!
<br />

`CODE1011,CODE2302,SMTG2310`

Last but not least, run `main.py` to create the configuration file

```Powershell
.\main.py
```

This will initially create a config.ini file, which holds all your login info. Then, run main.py again to start the actual program!
