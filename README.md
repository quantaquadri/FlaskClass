# FlaskClass

Started Learning Flask In Class yesterday. To begin, you need to start the server from your terminal. Here is how to:

TO install Flask follow this:

- cd to the folder containing your server.py, welcome.html files
- switch to the virtual environment you have created in the folder you are in; hint------- source .env/bin/activate
- pip freeze just to confirm 
- export FLASK_APP=server.py
- export FLASK_DEBUG=1                      1 means true btw
- flask run

And the server starts. You can type http://127.0.0.1:5000 in your browser to feel it


TO INSTALL A VIRTUAL ENV

1. which python
2. sudo pip3 install virtualenv
3. mkdir <foldername>
4. now navigate to the folder you just created
5. virtualenv --version
6. virtualenv .env
7. TO ACTIVATE THE VIRTUAL ENV CREATE; source .env/bin/activate
8. to deactivate; type deactivate
