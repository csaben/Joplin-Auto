# Joplin Server (Joplin-Auto)

## Purpose

Use a notebook directory within Joplin and have updated and new notes created each day. Support for
tracking todos across multiple days and graphing coming soon.

## Mailing (2 options)
[followed this repository](https://github.com/jeremyephron/simplegmail)
or by using Exchange 2016 (I prefer this, no re-authentication required)


## Setup

1. clone this directory
2. create a new conda env (normal python env works just fine too)
```
conda create --name your_env_name --file requirements.txt
```
3. inside this directory do:
```
python scripts/pypandocinstall.py
```
4. update your information inside of 'joplin_server/your_config.py'
5. make a cron job on linux:

```
crontab -e
```

in crontab buffer type the following:
```
unix time /bashlocation -i -c "conda activate or source your pip env your_env_name && python ~/locationOfThisProject/your_mailer.py" 2>~/yourLoggingDirectory/error.log
```

example of a job running at 3am 
```
0 3 * * * /bin/bash -i -c "conda activate tmp && python ~/workspace/joplin-server/daily-email.py" 2>~/workspace/joplin-server/error4.log
```

## Todo
- [ ] introduce excel sheet or living graph and upload/update to email or website
- [ ] synthesis module combining "interesting to me" and "to-do" + GPT + value statement prompt -> "suggested to-do"
