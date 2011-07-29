#!/bin/sh

cd /tmp

rm -rf test-project

quickly create ubuntu-pygame test-project
# Creating bzr repository and committing
# Congrats, your new project is setup! cd /tmp/test-project/ to start hacking.
# Creating project directory test-project

cd test-project

bzr status

bzr ls -R
# .quickly
# AUTHORS
# bin/
# bin/test-project
# data/
# data/media/
# data/media/background.png
# data/media/blam.wav
# data/media/bullet.png
# data/media/bullet_explode_1.png
# data/media/bullet_explode_2.png
# data/media/bullet_explode_3.png
# data/media/bullet_explode_4.png
# data/media/enemy.png
# data/media/engine_hum.wav
# data/media/explosion.wav
# data/media/free_guy.wav
# data/media/game_over.png
# data/media/guy.png
# data/media/guy_explode_1.png
# data/media/guy_explode_2.png
# data/media/guy_explode_3.png
# data/media/guy_explode_4.png
# data/media/guy_explode_5.png
# data/media/guy_explode_6.png
# data/media/guy_explode_7.png
# data/media/homing_missle.png
# data/media/icon.png
# setup.py
# test-project.desktop.in
# test_project/
# test_project/__init__.py
# test_project/base_sprite.py
# test_project/bullet.py
# test_project/enemy.py
# test_project/game.py
# test_project/guy.py
# test_project/hiscores.py
# test_project/homingmissle.py
# test_project/test_projectconfig.py
