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

## Add this alias to your ~/.zshrc or ~/.bashrc or similar...
```
alias yd='~/.virtualenvs/ydownlad/bin/python3 <PATH TO FILE>/app.py'
```