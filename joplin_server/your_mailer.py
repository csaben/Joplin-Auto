import warnings
from datetime import datetime

import pypandoc
from exchangelib import Account, Credentials, HTMLBody, Mailbox, Message
from joppy.api import Api

import joplin_server.config as config
import joplin_server.joplin_utils as joplin_utils
from joplin_server.build import TemplateBuilder
from joplin_server.note import Note

YOUR_EMAIL = config.SERVER
YOUR_RECIPIENT = config.MAILBOX

warnings.filterwarnings("ignore")

# Create a new Api instance.
api = Api(token=config.token)

# Obtain the notes via joplin API.
notes = api.get_all_notes(fields="id,title,body")


previous_day_title = joplin_utils.backtrack_date()

yesterday_note = joplin_utils.get_yesterday_note(
    previous_day_title=previous_day_title, notes=notes
)
note = Note(yesterday_note)

# Fill in template with the note object.
configurableTemplate = TemplateBuilder(note=note, config=config)

# TODO: move logic into main()

# send yourself an email with the template.
html = pypandoc.convert_text(configurableTemplate.template, "html", format="md")
percent = (note.completed / (note.total + 0.1)) * 100
frac = f"{note.completed}/{note.total}"
# offset to prevent division by zero error.
percent = (note.daily_completed / (note.daily_total + 1)) * 100
frac = f"{note.daily_completed}/{note.daily_total}"


api.add_note(
    parent_id=config.PARENT_ID,
    title=joplin_utils.filter(datetime.now().strftime("%m/%d/%y")),
    body=configurableTemplate.template,
    is_todo=True,
)

credentials = Credentials(f"{YOUR_EMAIL}", config.password)
account = Account(f"{YOUR_EMAIL}", credentials=credentials, autodiscover=True)

m = Message(
    account=account,
    subject=f"Yesterday Progress | {percent:.2f}% | {frac}",
    body=HTMLBody(html),
    to_recipients=[
        Mailbox(email_address=f"{YOUR_RECIPIENT}"),
    ],
)
m.send()
