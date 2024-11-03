from Spotify_Music.core.bot import Spotify
from Spotify_Music.core.dir import dirr
from Spotify_Music.core.git import git
from Spotify_Music.core.userbot import Userbot
from Spotify_Music.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()
# Bot Client
app = Spotify()

# Assistant Client
userbot = Userbot()

from .platforms import PlaTForms

Platform = PlaTForms()
HELPABLE = {}
