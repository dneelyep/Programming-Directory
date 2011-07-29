
__python_name_data_directory__ = '../data/'


import os

class project_path_not_found(Exception):
    pass

def getdatapath():
    """Retrieve project_name data path

    This path is by default <project_name_lib_path>/../data/ in trunk
    and /usr/share/project_name in an installed version but this path
    is specified at installation time.
    """

    # get pathname absolute or relative
    if __python_name_data_directory__.startswith('/'):
        pathname = __python_name_data_directory__
    else:
        pathname = os.path.dirname(__file__) + '/' + __python_name_data_directory__

    abs_data_path = os.path.abspath(pathname)
    if os.path.exists(abs_data_path):
        return abs_data_path
    else:
        raise project_path_not_found

#screen dimensions
screen_width = 800
screen_height = 480

hiscores_size = (620, 300)

#images
image_path = os.path.join(getdatapath(), "media/")

background_image = image_path + "background.png"
game_over_background = image_path + "game_over.png"

guy_img = image_path + "guy.png"
guy_bullet = image_path + "bullet.png"
bullet_explode_stage = image_path + "bullet_explode_"
guy_explode_stage = image_path + "guy_explode_"
enemy_explode_stage = image_path + "guy_explode_"
enemy_image = image_path + "enemy.png"
homing_missle_image = image_path + "homing_missle.png"

default_bullet = image_path + "bullet.png"

#sounds
sound_path = os.path.join(getdatapath(), "media/")

guy_eng = sound_path + "engine_hum.wav"
guy_explode = sound_path + "explosion.wav"
guy_shoot_sound = sound_path + "blam.wav"
guy_bullet_explode = sound_path + "explosion.wav"
free_guy_sound = sound_path + "free_guy.wav"

enemy_explode_sound = sound_path + "explosion.wav"
