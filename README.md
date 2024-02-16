# scratch-livestats

## Installation
Run the following command in your command prompt/shell to install `scratchattach` :
```cmd
pip install -U scratchattach
```

## Download & Configuration
Download the file [here](https://raw.githubusercontent.com/Artcas2/scratch-livestats/main/live-stats.py).

Configuration : 
*You can get your session id from your browser's cookies. [More information](https://github.com/Artcas2/scratch-livestats/#get-your-session-id)*
```python
session = scratch3.Session("sessionid", username="your_username") # replace sessionid with your scratch session id and your_username with your username
project_id = "your_project_id" # replace your_project_id with your project id
cloud = session.connect_cloud(project_id)
user = scratch3.get_user("your_username") # replace your_username with your username
project = session.connect_project(project_id)
```

**You can also log in with username/password like this:**
```python
session = scratch3.login("your_username", "your_password") # replace your_username with your username and your_password with your password
```

# Get your session id

This section explains how to get your Scratch session id from your browser cookies.

1. Open scratch.mit.edu in your browser
2. Click the 🔒 icon in the URL bar, then click "Cookies"
3. Then find a cookie called `scratchsessionid` (in the "scratch.mit.edu" » "Cookies" folder). The content of this cookie is your Scratch session id

![](https://scratch3-assets.1tim.repl.co/template/cookies.png)
