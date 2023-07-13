class TemplateBuilder:
    def __init__(self, note, config):
        self.note = note
        self.template = None
        self.config = config
        self._build(note)

    def update(self):
        """TODO:
        specific sections should each have an update function to be accessed in send.py
        or
        different styles of templates should be available
        """
        pass

    def _build(self, note):
        self.template = f"""
today todos

{note.headers.get_header("today todos").value}

***

tomorrow todos

{note.headers.get_header("tomorrow todos").value}

***

everyday todos

{self.config.everyday}

***

work todos

{note.headers.get_header("work todos").value}

***

personal todos

{note.headers.get_header("personal todos").value}

***

misc todos

{note.headers.get_header("misc todos").value}

"""
