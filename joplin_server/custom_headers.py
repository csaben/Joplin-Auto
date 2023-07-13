from joplin_server import note_utils
from joplin_server.headers import HeaderNode


class today(HeaderNode):
    def __init__(self, header: str, df):
        super().__init__(header, df)
        pass


class tomorrow(HeaderNode):
    def __init__(self, header: str, df):
        super().__init__(header, df)
        pass


class everyday(HeaderNode):
    def __init__(self, header: str, df):
        super().__init__(header, df)
        pass


class work(HeaderNode):
    def __init__(self, header: str, df):
        super().__init__(header, df)
        pass


class personal(HeaderNode):
    def __init__(self, header: str, df):
        super().__init__(header, df)
        pass


class misc(HeaderNode):
    def __init__(self, header: str, df):
        super().__init__(header, df)

    @property
    def value(self):
        # abuse remaining dataframe functionality
        # 1) find any floating todos
        floating = self.df[self.df["text"].str.contains(f"\({self.name}\)")]
        self._values = self._value._append(floating)

        # misc specific: any todos above 'today todos' should be added
        # to the misc todos section
        # 2) get the index of 'today todos'
        idx = note_utils.get_index("today todos", self.df)
        above = self.df.iloc[:idx]

        self._value = self._value._append(above)
        # 3) remove duplicates
        self._value = self._value.drop_duplicates()

        # convert df values to list and return it
        self._value = "\n".join(self._value["text"].tolist())
        return self._value
