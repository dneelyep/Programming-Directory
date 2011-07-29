import getpass
import operator
import time
import pwd
import pygame

from datetime import datetime
from desktopcouch.records.server import CouchDatabase
from desktopcouch.records.record import Record

DARK_GRAY = (68, 47, 47)
LIGHT_GRAY = (200, 180, 180)
WHITE = (255, 255, 255)
SCORE_RECORD_TYPE = 'https://wiki.ubuntu.com/GamesIntegration/HighScore'

pygame.font.init()
font = pygame.font.Font(None, 24)
couchdb = CouchDatabase("python_name", create=True)

def get_user_fullname():
    """Return the name of the current user."""
    username = getpass.getuser()
    fullname = pwd.getpwnam(username).pw_gecos.split(",")[0]
    return fullname if len(fullname) > 0 else username

def add_dummy_scores():
    """Add some dummy scores to the database."""
    names = "Vince Noir|Naboo the Enigma|Bollo was Here|Bob Fossil|Howard Moon"
    level = 4
    for name in reversed(names.split("|")):
        save_score(level ** 2, level, name)
        level *= 2

def get_hiscores(top=10):
    """Return the sorted list of scores."""
    all_scores = couchdb.get_all_records(record_type=SCORE_RECORD_TYPE)
    if len(all_scores) == 0:
        add_dummy_scores()
        all_scores = couchdb.get_all_records(record_type=SCORE_RECORD_TYPE)
    sort_key = operator.itemgetter("score", "timestamp")
    sorted_scores = sorted(all_scores, key=sort_key, reverse=True)
    return sorted_scores[:top]

def save_score(score, level, player=get_user_fullname()):
    """Save the score in the couch database."""
    data = {
        "player": player,
        "level": level,
        "score": score,
        "timestamp": time.time(),
    }
    record = Record(data, record_type=SCORE_RECORD_TYPE)
    couchdb.put_record(record)

def hiscores_screen(screen_size, message="Press Enter to Start"):
    """A pygame surface with the hiscore board and start message."""
    screen = pygame.Surface(screen_size) # pylint: disable=E1121
    screen.fill(DARK_GRAY)
    screen_rect = screen.get_rect()
    centerx = screen_rect.centerx
    line_size = font.get_linesize()

    y = line_size
    msg = font.render("Highest Scores", 1, WHITE)
    msg_top = screen_rect.bottom - line_size
    screen.blit(msg, msg.get_rect(centerx=centerx, top=y))
    y += line_size * 2

    hiscores = get_hiscores(top=10)
    scoreboard_centerx = centerx * 0.83
    for score in hiscores:
        msg = font.render(str(score["score"]) + " - ", 1, LIGHT_GRAY)
        screen.blit(msg, msg.get_rect(right=scoreboard_centerx, top=y))
        msg = font.render(score["player"], 1, LIGHT_GRAY)
        screen.blit(msg, msg.get_rect(left=scoreboard_centerx, top=y))
        y += line_size

    msg = font.render(message, 1, WHITE)
    msg_bottom = screen_rect.bottom - line_size
    screen.blit(msg, msg.get_rect(centerx=centerx, bottom=msg_bottom))
    return screen
