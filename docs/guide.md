### bug board

- categorization headers for things within "todays todos" should be allowed and then subsequently removed at EOD
- logs should go into log dir with new file name
- pypandoc installation should be documented in readme
- repeat tag for things that you completed but need to be re-added tomorrow but are forever
- storing task/goal specific files full of their todos and having a scraping call that on a specific day or flag provided in the tomorrow todos will populate your today todos differently (dynamic template)
- building in default text such as (```weekend (saturday)```) as a config enum to access in template build step. 

new philosophy: 
* Note should handle collecting main header content 
* Config should store text defaults and editable day to day conditional todos
* send.py should not be building and sending, build should happen in a separate file (this way standalone build testing can be done)
* a build module should use parsed previous day (so things within default text should have their own gathering fn) and then we should re-assemble the template with line to line precision of default text, main headers, and config configurable daily todos
