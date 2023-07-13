def get_index(header, df):
    """Get the index of the header in the dataframe"""
    return df[df["text"].str.contains(header, case=False)].index[0]


def get_completed_todos(df):
    """Get the number of completed todos"""
    return df[df["text"].str.contains("- \[x\]")]


def get_incomplete_todos(df):
    """Get the number of incomplete todos"""
    return df[df["text"].str.contains("- \[ \]")]


def filter_todo_by_substring(df, substring):
    """Filter the dataframe by a substring"""
    return df[df["text"].str.contains(substring)]


def get_backup_df(df):
    """Get the backup dataframe"""
    new_df = df.copy()
    new_df.index = range(len(new_df.index))

    # return df.copy() with updated index
    return new_df


def get_stats(df):
    """Get the stats of the dataframe"""
    completed = len(get_completed_todos(df))
    total = len(get_incomplete_todos(df)) + completed
    return completed, total
