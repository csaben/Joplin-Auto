# Joplin Local Server

## Mailing 
[followed this repository](https://github.com/jeremyephron/simplegmail)


## todo's
- introduce excel sheet or living graph and upload/update to email or website
- synthesis module combining "interesting to me" and "to-do" + GPT + value statement prompt -> "suggested to-do"

## basic setup
make a cron job on linux:

```
crontab -e
```

insert:
```
0 3 * * * /bin/bash -i -c "conda activate tmp && python ~/workspace/joplin-server/daily-email.py" 2>~/workspace/joplin-server/error4.log
```
