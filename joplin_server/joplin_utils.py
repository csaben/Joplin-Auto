from datetime import datetime, timedelta

from joplin_server import joplin_utils


def filter(note):
    # remove the leading zero from the month
    previous_day_title = note.lstrip("0")
    # remove the leading zero from the day
    previous_day_title = previous_day_title.replace("/0", "/")
    return previous_day_title


# Get the title for the previous day.
def backtrack_date(days=1):
    previous_day = datetime.now() - timedelta(days)
    previous_day_title = previous_day.strftime("%m/%d/%y")
    return previous_day_title


# Filter the notes to find the one with the title of the previous day.
# (don't need to filter)
def get_yesterday_note(previous_day_title, notes):
    for note in notes:
        if note.title == joplin_utils.filter(previous_day_title):
            yesterday_note = note.body
        else:
            yesterday_note = None
    # handle if there is no note for the previous day.
    ct = 2
    while not yesterday_note:
        print("yesterday note not found")
        previous_day_title = joplin_utils.backtrack_date(ct)
        print(previous_day_title)
        for note in notes:
            if note.title == joplin_utils.filter(previous_day_title):
                yesterday_note = note.body
        ct += 1

    return yesterday_note
