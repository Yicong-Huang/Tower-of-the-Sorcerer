'''The LIB contains all info about Items and Characters used in the game'''
from collections import namedtuple
import inspect

from PIL.ImageTk import PhotoImage

Enhancement = namedtuple('Enhancement', 'name image kind value')
Mob = namedtuple('Mob', 'name image hp attack defense gold')
Character = namedtuple('Character', 'name image')
Protagonist = namedtuple('Protagonist', 'name image hp attack defense gold')
Build = namedtuple('Build', 'name image')
Collection = namedtuple('Collection', 'name image')
Hallow = namedtuple('Hallow', 'name image')
Trigger = namedtuple('Trigger', 'name case')


LIB = {
    'background':Build('background', None),
    'hidden_wall':Build('hidden_wall', None),

    'wall':Build('wall', 1),
    'hidden_door':Build('wall', 1),
    'shop_mid':Build('shop_mid', 2),
    'shop_left':Build('shop_left', 1),
    'shop_right':Build('shop_right', 1),
    'yellow_door':Build('yellow_door', 1),
    'special_door':Build('special_door', 1),
    'upstairs':Build('upstairs', 1),
    'downstairs':Build('downstairs', 1),
    'blue_door':Build('blue_door', 1),
    'red_door':Build('red_door', 1),
    'iron_door':Build('iron_door', 1),
    'lava':Build('lava', 2),

    'yellow_key':Collection('yellow_key', 1),
    'red_key':Collection('red_key', 1),
    'blue_key':Collection('blue_key', 1),

    'transmit':Hallow('transmit', 1),
    'cross':Hallow('cross', 1),
    'pickaxe':Hallow('pickaxe', 1),
    'st_water':Hallow('st_water', 1),
    'lucky_coin':Hallow('lucky_coin', 1),
    'transmit_down':Hallow('transmit_down', 1),
    'info_book':Hallow('info_book', 1),
    'ice':Hallow('ice', 1),
    'earthquake':Hallow('earthquake', 1),
    'key':Hallow('key', 1),
    'boom':Hallow('boom', 1),
    'fly_down':Hallow('fly_down', 1),
    'fly_up':Hallow('fly_up', 1),
    'fly_oppo':Hallow('fly_oppo', 1),
    'dragon_dagger':Hallow('dragon_dagger', 1),

    'red_blood':Enhancement('red_blood', 1, 'hp', 50),
    'blue_blood':Enhancement('blue_blood', 1, 'hp', 200),
    'red_gem':Enhancement('red_gem', 1, 'attack', 1),
    'blue_gem':Enhancement('blue_gem', 1, 'defense', 1),
    'sword1':Enhancement('sword1', 1, 'attack', 10),
    'sword2':Enhancement('sword2', 1, 'attack', 20),
    'sword3':Enhancement('sword3', 1, 'attack', 40),
    'sword4':Enhancement('sword4', 1, 'attack', 50),
    'sword5':Enhancement('sword5', 1, 'attack', 100),
    'shield1':Enhancement('shield1', 1, 'defense', 10),
    'shield2':Enhancement('shield2', 1, 'defense', 20),
    'shield3':Enhancement('shield3', 1, 'defense', 40),
    'shield4':Enhancement('shield4', 1, 'defense', 50),
    'shield5':Enhancement('shield5', 1, 'defense', 100),

    'bat':Mob('bat', 2, 35, 38, 3, 3),
    'skeleton':Mob('skeleton', 2, 50, 42, 6, 6),
    'blue_wizard':Mob('blue_wizard', 2, 60, 32, 8, 5),
    'skeleton_soldier':Mob('skeleton_soldier', 2, 55, 52, 12, 8),
    'skeleton_captain':Mob('skeleton_captain', 2, 100, 65, 15, 30),
    'green_slime':Mob('green_slime', 2, 35, 18, 1, 1),
    'red_slime':Mob('red_slime', 2, 45, 20, 2, 2),
    'mid_soldier':Mob('mid_soldier', 2, 100, 180, 110, 50),
    'pri_soldier':Mob('pri_soldier', 2, 50, 48, 22, 12),
    'big_bat':Mob('big_bat', 2, 60, 100, 8, 12),
    'big_slime':Mob('big_slime', 2, 130, 60, 3, 8),
    'red_wizard':Mob('red_wizard', 2, 100, 95, 30, 18),
    'vampire':Mob('vampire', 2, 444, 199, 66, 144),
    'zombie':Mob('zombie', 2, 260, 85, 5, 22),
    'rock':Mob('rock', 2, 20, 100, 67, 28),
    'zombie_soldier':Mob('zombie_soldier', 2, 320, 120, 15, 30),
    'ghost_soldier':Mob('ghost_soldier', 2, 220, 180, 30, 35),
    'slime_man':Mob('slime_man', 2, 320, 140, 20, 30),
    'slime_king':Mob('slime_king', 2, 360, 310, 20, 40),
    'vampire_bat':Mob('vampire_bat', 2, 200, 390, 90, 50),
    'soldier':Mob('soldier', 2, 210, 200, 65, 45),
    'swords_man':Mob('swords_man', 2, 100, 680, 50, 55),
    'knight':Mob('knight', 2, 160, 230, 105, 65),
    'pri_witch':Mob('pri_witch', 2, 220, 370, 110, 80),
    'pro_witch':Mob('pro_witch', 2, 200, 380, 130, 90),
    'golden':Mob('golden', 2, 120, 150, 50, 100),
    'magic_guard':Mob('magic_guard', 2, 230, 450, 100, 100),
    'dark_knight':Mob('dark_knight', 2, 180, 430, 210, 120),
    'pro_soldier':Mob('pro_soldier', 2, 180, 460, 360, 200),
    'squid':Mob('squid', 2, 1200, 180, 20, 100),
    'great_magic':Mob('great_magic', 2, 4500, 560, 310, 1000),
    'dragon':Mob('dragon', 2, 1500, 600, 250, 800),
    'fake_lord1':Mob('lord', 2, 8000, 5000, 1000, 500),
    'fake_lord2':Mob('lord', 2, 800, 500, 100, 500),

    'background_trigger':Trigger('background_trigger', 1),
    'yellow_door_trigger':Trigger('yellow_door_trigger', 2),
    'green_slime_trigger':Trigger('green_slime_trigger', 2),
    'red_slime_trigger':Trigger('red_slime_trigger', 2),
    'big_slime_trigger':Trigger('big_slime_trigger', 2),
    'skeleton_trigger':Trigger('skeleton_trigger', 2),
    'skeleton_soldier_trigger':Trigger('skeleton_soldier_trigger', 2),
    'skeleton_captain_trigger':Trigger('skeleton_captain_trigger', 3),
    'red_wizard_trigger':Trigger('red_wizard_trigger', 1),
    'mid_soldier_trigger':Trigger('mid_soldier_trigger', 2),
    'pri_soldier_trigger':Trigger('pri_soldier_trigger', 1),
    'pri_soldier_trigger2':Trigger('pri_soldier_trigger', 2),
    'zombie_trigger':Trigger('zombie_trigger', 3),
    'zombie_soldier_trigger':Trigger('zombie_soldier_trigger', 4),
    'vampire_trigger':Trigger('vampire_trigger', 2),
    'ghost_soldier_trigger':Trigger('ghost_soldier_trigger', 2),
    'soldier_trigger':Trigger('soldier_trigger', 2),
    'knight_trigger':Trigger('knight_trigger', 2),
    'bat_trigger':Trigger('bat_trigger', 2),
    'swords_man_trigger':Trigger('swords_man_trigger', 2),
    'squid_trigger':Trigger('squid_trigger', 2),
    'dragon_trigger':Trigger('dragon_trigger', 1),
    'pro_witch_trigger':Trigger('pro_witch_trigger', 3),
    'pro_witch_trigger2':Trigger('pro_witch_trigger', 2),
    'magic_guard_trigger':Trigger('magic_guard_trigger', 4),
    'dark_knight_trigger':Trigger('dark_knight_trigger', 2),
    'fake_lord2_trigger':Trigger('fake_lord2_trigger', 5),
    'pro_soldier_trigger':Trigger('pro_soldier_trigger', 1),
    'golden_trigger':Trigger('golden_trigger', 2),

    'thief':Character('thief', 2),
    'merchant':Character('merchant', 2),
    'sage':Character('sage', 2),
    'protagonist':Protagonist('protagonist', 1, 4000, 10000, 10, 10000)

    }

def set_image(item):
    "Sets the image with the path created by Obj's class and stores the image"
    global LIB
    image = LIB[item.get_value('name')].image
    name = LIB[item.get_value('name')].name
    file = '/'.join(['src']+[cls.__name__ for cls in inspect.getmro(item.__class__)]
                    [::-1][3:]+[name+'.png'])
    if image == 1:
        LIB[item.get_value('name')] = LIB[item.get_value('name')]._replace(
            image=PhotoImage(file=file))
    elif image == 2:
        LIB[item.get_value('name')] = LIB[item.get_value('name')]._replace(
            image=(PhotoImage(file=file), PhotoImage(file=file[:-4]+'2.png')))
    elif isinstance(image, str):
        LIB[item.get_value('name')] = LIB[item.get_value('name')]._replace(
            image=LIB[image].image)
