# Weather Telegram bot

Hello this is bot for Telegram messenger that can tell you the weather of any city.
It deployed on Heroku and it's working even right now! You can find it by this ID: Tenkipybot or just use direct link https://t.me/Tenkipybot


# How it works?
1.  Install Python, as well as Telebot and Pyowm on your system
2.  Download this repo (you can use "Download Zip" button for the sake of speed)
3.  Open "telbot.py" for edit (or create your own if you want)
4.  Find BotFather in Telegram by this link https://t.me/BotFather.
5. Send command "/newbot"
6. Follow BotFather's simple steps to create your own bot with the name you want.
7. Then this bot will give you Token, that you have to copy&paste instead of my token in the line #9 of "telbot.py"
8.  Run "telbot.py" within Terminal and wait few seconds
9.  Done! Open your telegram bot and try it out! :)



# How to install Telebot & Pyowm?

## Telebot
This API is tested with Python 3.6-3.10 and Pypy 3. There are two ways to install the library:

-   Installation using pip (a Python package manager):
```
	$ pip install pyTelegramBotAPI
```

-   Installation from source (requires git):

```
	$ git clone https://github.com/eternnoir/pyTelegramBotAPI.git
	$ cd pyTelegramBotAPI
	$ python setup.py install
```
or:

```
$ pip install git+https://github.com/eternnoir/pyTelegramBotAPI.git

```

It is generally recommended to use the first option.

_While the API is production-ready, it is still under development and it has regular updates, do not forget to update it regularly by calling_

```
pip install pytelegrambotapi --upgrade
```

## PyOWM
-  Install with  `pip`  for your ease:
```
	$ pip install pyowm
```
There are alternatives:  _setuptools_,  _Windows installers_  and common Linux package managers such as  _Yaourt (Arch Linux)_  _YaST/Zypper (OpenSuse)_  (please refer to the documentation for more detail)

-  Eager to fetch the very latest updates to PyOWM? Install the development trunk (which might be unstable). Eg on Linux:
```
	$ git clone https://github.com/csparpa/pyowm.git
	$ cd pyowm && git checkout develop
	$ pip install -r requirements.txt && python setup.py install
```
