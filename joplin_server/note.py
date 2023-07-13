import datetime

import joplin_utils
import pandas as pd

from joplin_server import note_utils
from joplin_server.headers import HeaderList


class Note:
    def __init__(self, note=None):
        self.note = note
        if note:
            # remove all *** and replace with ""
            note = note.replace("* * *", "")
            # convert to dataframe and meaningfully store tabs
            df = pd.DataFrame(note.split("\n"), columns=["text"])
            # remove the empty rows
            self.df = df[df["text"] != ""]
            self.df = df

        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        self.day_of_week = datetime.date.today().strftime("%A")
        tomorrow = joplin_utils.filter(tomorrow.strftime("%m/%d/%Y"))
        self.tomorrow = tomorrow
        self.completed = 0
        self.total = 0
        self.backup_df = None
        self.daily_completed = 0
        self.daily_total = 0

        # TODO: implement these
        # self.diff_tags = {"easy": 0, "medium": 0, "hard": 0}

    @property
    def headers(self):
        """usage:
        note = Note()
        note.headers.get_header("today todos").value
        """
        # get secton indices
        header_list = HeaderList(self.df)
        # update indices
        header_list.update_indices()
        self._collect_attribs()
        return header_list

    def _collect_attribs(self):
        self.completed, self.total = note_utils.get_stats(self.df)
        self.daily_completed, self.daily_total = self.completed, self.total
        self.backup_df = note_utils.get_backup_df(self.df)
        # TODO: fix
        # self.daily_completed, self.daily_total = self.headers.get_header(
        #     "daily todos"
        # ).local_stats


# make a test
def test():
    import warnings

    from joppy.api import Api

    import joplin_server.config as config
    import joplin_server.joplin_utils as joplin_utils

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

    # this call should work

    assert (
        note.headers.get_header("today todos").value is not None
    ), "today todos header not found"
