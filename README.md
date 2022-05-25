# How to update app on Heroku
heroku container:push web
heroku container:release web

# Reminders
1) Add new dependecies to requierements.txt

# Error
»   Error: Missing required flag:
 »     -a, --app APP  app to run command against
 »   See more help with --help

# Solution
1- Initialise with git: git init

2- Get the app name: heroku apps

3- Add remote:

heroku git:remote -a your_app_name