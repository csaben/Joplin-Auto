from joplin_server import custom_headers

password = ""
MAILBOX = ""
SERVER = ""

# parent id of the notebook that you store your todos in
PARENT_ID = ""

# token if using gmail
token = ""

everyday = """
- [ ] daily problem solving
    - [ ] leetcode problem
- [ ] daily workout
    - [ ] go for a run
"""

headers = {
    "today todos": custom_headers.today,
    "tomorrow todos": custom_headers.tomorrow,
    "everyday todos": custom_headers.everyday,
    "work todos": custom_headers.work,
    "personal todos": custom_headers.personal,
    "misc todos": custom_headers.misc,
}
