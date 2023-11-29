## Check you python version 
``` bash
$ python3 --version

> Python 3.11.12
``` 

Python 3.11.12 - this is a dev version

## Create venv and 
``` bash
python3 -m venv ~/.virtualenvs/ydownload
```

## activate and install requirements
```bash
source ~/.virtualenvs/ydownload/bin/activate
pip install -r requirements.txt
```
## To load file just run
```
python app.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
## Add this alias to your ~/.zshrc or ~/.bashrc or similar...
```
alias yd='~/.virtualenvs/ydownload/bin/python3 <PATH TO FILE>/app.py'
```
