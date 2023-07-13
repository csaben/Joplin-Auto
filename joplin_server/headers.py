from joplin_server import note_utils


class HeaderNode:
    """HeaderNode class to hold header information"""

    def __init__(self, header: str, df):
        self.name: str = header
        # tomorrow = self.df[self.df["text"].str.contains(f"\({self.tomorrow}\)")]
        self.header = df[df["text"].str.contains(f"\({self.name}\)")]
        self.df = df
        self.start_idx, self.end_idx = (
            note_utils.get_index(self.name, self.df),
            None,
        )
        self.next = None
        self._value = None
        self.completed, self.total = None, None

    def _update_indices(self):
        self.index: int = note_utils.get_index(self.name, self.df)
        self.start_index: int = self.index
        self.end_index: int = self._end()
        self._value = self.df.iloc[self.start_index : self.end_index]

    def _end(self):
        """Get the end index"""
        if self.next:
            return self.next.start_idx
        else:
            return len(self.df.index)

    def update_start_end_indices(self):
        """Get the start and end indices of a header"""
        self._update_indices()
        self.local_stats = self.completed, self.total = self._get_local_stats()
        return self.start_index, self.end_index

    def _get_local_stats(self):
        """Get the local stats of a header"""
        return note_utils.get_stats(self._value)

    @property
    def value(self):
        # abuse remaining dataframe functionality
        # 1) find any floating todos
        floating = self.df[self.df["text"].str.contains(f"\({self.name}\)")]
        self._values = self._value._append(floating)
        # 2) remove duplicates
        self._value = self._value.drop_duplicates()

        # convert df values to list and return it
        self._value = "\n".join(self._value["text"].tolist())
        return self._value


class HeaderList:
    """List of header objects

    e.g.
    headers = HeaderList(df)
    headers.get_header("tomorrow").value
    """

    def __init__(self, df):
        self.head = None
        self.df = df
        self._build_list()

    def _build_list(self):
        """Build the list of headers"""
        from joplin_server.config import headers

        for header, cls in headers.items():
            self.append(header, cls)

    def append(self, header: str, cls: callable):
        """Append a header to the list"""
        new_node = cls(header, self.df)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """Print the list of headers"""
        temp = self.head
        while temp:
            print(temp.name)
            temp = temp.next

    def get_header(self, header: str):
        """Get the header object"""
        temp = self.head
        while temp:
            if temp.name == header:
                return temp
            temp = temp.next
        return None

    def update_indices(self):
        temp = self.head
        while temp:
            temp.update_start_end_indices()
            temp._get_local_stats()
            temp = temp.next
