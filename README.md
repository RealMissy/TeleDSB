# TeleDSB

DSB mobile bot for telegram

### Prerequisites

You will need python 2.7.x on your computer.

```
https://www.python.org/downloads/
```


Get your telegram bot token after you created a new bot with /newbot or just use the command /token if you already created a bot.

```
https://telegram.me/botfather
```

### Installing

1)
Install the latest version of <a href="https://github.com/nickoala/telepot">telepot</a>
```
$ pip install telepot
$ pip install telepot --upgrade  # UPGRADE
```
more detail: <a href="https://github.com/nickoala/telepot">the project-website</a>

2)
Install the latest version of <a href="https://github.com/jarrekk/imgkit">IMGKit</a> and wkhtmltopdf
```
pip install imgkit
```
For Debian/ Ubuntu:
```
sudo apt-get install wkhtmltopdf
```
For MacOS:
```
brew install wkhtmltopdf
```

Download our last stable release and run it in two seperate command lines.

```
python TeleDSB.py <<YOUR-BOT-TOKEN>>
python getTimetables.py <<YOUR-DSB-LOGIN>> <<YOUR-DSB-PASSWORD>>
```

## Authors

RealMissy

JayCeM

## License

This project is licensed GNU General Public License 3

## Acknowledgments

* Big thanks to TheNoim for for providing a great DSB mobile API
* nickoala wrote the telepot libary, which is absolutely handy
* jarrek provided the html to .png convertation libary
