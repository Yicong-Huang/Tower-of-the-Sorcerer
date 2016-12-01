from PIL.ImageTk import PhotoImage

from collections import namedtuple


Enhancement=namedtuple('Enhancement','name image kind value')
Mob= namedtuple('Mob', 'name image hp attack defense gold')
Character= namedtuple('Character', 'name image')
Protagonist= namedtuple('Protagonist', 'name image hp attack defense gold')
Build = namedtuple('Build', 'name image')
Collection = namedtuple('Collection', 'name image')
Hallow = namedtuple('Hallow', 'name image')
Trigger = namedtuple('Trigger', 'name obj image case')
#lib={}

lib= {
    'background':Build('background',None),
    'hidden_wall':Build('hidden_wall',None),
    'wall':Build('wall','src/item/build/wall.png'),
    'hidden_door':Build('hidden_door','src/item/build/wall.png'),
    'shop_mid':Build('shop_mid',('src/item/build/shop_mid.png','src/item/build/shop_mid2.png',)),
    'shop_left':Build('shop_left','src/item/build/shop_left.png'),
    'shop_right':Build('shop_right','src/item/build/shop_right.png'),
    'yellow_door':Build('yellow_door','src/item/build/yellow_door.png'),
    'special_door':Build('special_door','src/item/build/special_door.png'),
    'upstairs':Build('upstairs','src/item/build/upstairs.png'),
    'downstairs':Build('downstairs','src/item/build/downstairs.png'),
    'blue_door':Build('blue_door','src/item/build/blue_door.png'),
    'red_door':Build('red_door','src/item/build/red_door.png'),
    'iron_door':Build('iron_door','src/item/build/iron_door.png'),
    'lava':Build('lava',('src/item/build/lava.png',)),
    
    'yellow_key':Collection('yellow_key','src/item/collection/yellow_key.png'),
    'red_key':Collection('red_key','src/item/collection/red_key.png'),
    'blue_key':Collection('blue_key','src/item/collection/blue_key.png'),
    
    'transmit':Hallow('transmit','src/item/hallow/transmit.png'),
    'cross':Hallow('cross','src/item/hallow/cross.png'),
    'pickaxe':Hallow('pickaxe','src/item/hallow/pickaxe.png'),
    
    'red_blood':Enhancement('red_blood','src/item/enhancement/red_blood.png','hp',50),
    'blue_blood':Enhancement('blue_blood','src/item/enhancement/blue_blood.png','hp',200),
    'red_gem':Enhancement('red_gem','src/item/enhancement/red_gem.png','attack',1),
    'blue_gem':Enhancement('blue_gem','src/item/enhancement/blue_gem.png','defense',1),
    'sword1':Enhancement('sword1','src/item/enhancement/sword1.png','attack',10),
    'sword2':Enhancement('sword2','src/item/enhancement/sword2.png','attack',20),
    'sword3':Enhancement('sword3','src/item/enhancement/sword3.png','attack',40),
    'sword4':Enhancement('sword4','src/item/enhancement/sword4.png','attack',50),
    'shield1':Enhancement('sheild1','src/item/enhancement/shield1.png','defense',10),
    'shield2':Enhancement('sheild2','src/item/enhancement/shield2.png','defense',20),
    'shield3':Enhancement('sheild3','src/item/enhancement/shield3.png','defense',40),
    'shield4':Enhancement('sheild4','src/item/enhancement/shield4.png','defense',50),
    
    'bat':Mob('bat',('src/character/mob/bat.png',),35,38,3,3),
    'skeleton':Mob('skeleton',('src/character/mob/skeleton.png',),50,42,6,6),
    'blue_wizard':Mob('blue_wizard',('src/character/mob/blue_wizard.png',), 60,32,8,5),
    'skeleton_soldier':Mob('skeleton_soldier',('src/character/mob/skeleton_soldier.png',),  55,52,12,8),
    'skeleton_captain':Mob('skeleton_captain',('src/character/mob/skeleton_captain.png',), 100,65,15,30),
    'green_slime':Mob('green_slime',('src/character/mob/green_slime.png',),35,18,1,1),
    'red_slime':Mob('red_slime',('src/character/mob/red_slime.png',), 45,20,2,2),
    'mid_soldier':Mob('mid_soldier',('src/character/mob/mid_soldier.png',),100,180,110,50),
    'pri_soldier':Mob('pri_soldier',('src/character/mob/pri_soldier.png',), 50,48,22,12),
    'big_bat':Mob('big_bat',('src/character/mob/big_bat.png',),60,100,8,12),
    'big_slime':Mob('big_slime',('src/character/mob/big_slime.png',),130,60,3,8),
    'red_wizard':Mob('red_wizard',('src/character/mob/red_wizard.png',),100,95,30,18),
    'vampire':Mob('vampire',('src/character/mob/vampire.png',),444,199,66,144),
    'zombie':Mob('zombie',('src/character/mob/zombie.png',),100,95,30,18),
    'rock':Mob('rock',('src/character/mob/rock.png',),20,100,67,28),
    'zombie_soldier':Mob('zombie_soldier',('src/character/mob/zombie_soldier.png',),100,95,30,18),
    'ghost_soldier':Mob('ghost_soldier',('src/character/mob/ghost_soldier.png',),220,180,30,35),
    'slime_man':Mob('slime_man',('src/character/mob/slime_man.png',),320,140,20,30),
    'golden':Mob('golden',('src/character/mob/golden.png',),120,150,50,100),
    'knight':Mob('knight',('src/character/mob/knight.png',),160,230,105,65),
    'swords_man':Mob('swords_man',('src/character/mob/swords_man.png',),100,680,50,55),
    'soldier':Mob('soldier',('src/character/mob/soldier.png',),210,200,65,45),
    'pri_witch':Mob('pri_witch',('src/character/mob/pri_witch.png',),220,370,110,80),
    'pro_witch':Mob('pro_witch',('src/character/mob/pro_witch.png',),200,380,130,90),
    'vampire_bat':Mob('vampire_bat',('src/character/mob/vampire_bat.png',),200,390,90,50),
    'squid':Mob('squid',('src/character/mob/squid.png',),1200,180,20,100),
    'great_magic':Mob('great_magic',('src/character/mob/great_magic.png',),4500,560,310,1000),
    'dragon':Mob('dragon',('src/character/mob/dragon.png',),1500,600,250,800),
    
    'trigger':Trigger('trigger','background',None,1),
    'yellow_door_trigger':Trigger('yellow_door_trigger','yellow_door',None,2),
    'green_slime_trigger':Trigger('green_slime_trigger','green_slime',None,2),
    'red_slime_trigger':Trigger('red_slime_trigger','red_slime',None,2),
    'big_slime_trigger':Trigger('big_slime_trigger','big_slime',None,2),
    'skeleton_trigger':Trigger('skeleton_trigger','skeleton',None,2),
    'skeleton_soldier_trigger':Trigger('skeleton_soldier_trigger','skeleton_soldier',None,2),
    'skeleton_captain_trigger':Trigger('skeleton_captain_trigger','skeleton_captain',None,3),
    'red_wizard_trigger':Trigger('red_wizard_trigger','red_wizard',None,1),
    'mid_soldier_trigger':Trigger('mid_soldier_trigger','mid_soldier',None,2),
    'pri_soldier_trigger':Trigger('pri_soldier_trigger','pri_soldier',None,1),
    'pri_soldier_trigger2':Trigger('pri_soldier_trigger2','pri_soldier',None,2),
    'zombie_trigger':Trigger('zombie_trigger','zombie',None,3),
    'zombie_soldier_trigger':Trigger('zombie_soldier_trigger','zombie_soldier',None,4),
    'vampire_trigger':Trigger('vampire_trigger','vampire',None,2),
    'ghost_soldier_trigger':Trigger('ghost_soldier_trigger','ghost_soldier',None,2),
    'soldier_trigger':Trigger('soldier_trigger','soldier',None,2),
    'knight_trigger':Trigger('knight_trigger','knight',None,2),
    'bat_trigger':Trigger('bat_trigger','bat',None,2),
    'swords_man_trigger':Trigger('swords_man_trigger','swords_man',None,2),
    'squid_trigger':Trigger('squid_trigger','squid',None,2),
     
     
     
     
     
     'thief':Character('thief',('src/character/thief.png',)),
     'merchant':Character('merchant',('src/character/merchant.png',)),
     'sage':Character('sage',('src/character/sage.png',)),
     'protagonist':Protagonist('protagonist','src/character/protagonist.png',4000,200,200,0)
     
     
     
     
     
     
     }

def set_image(name):
    global lib      
    if 'trigger' in name :
        image= lib[lib[name].obj].image
        if isinstance(image,tuple) and isinstance(image[0],str):
            set_image(lib[name].obj)
            image=lib[lib[name].obj].image
        lib[name]=lib[name]._replace(image=image)
    else:
        image=lib[name].image
    if isinstance(image,str):
        print(name,image)
        lib[name]=lib[name]._replace(image=PhotoImage(file=image))
    elif isinstance(image,tuple) and isinstance(image[0],str): 
        file=image[0]
        print('111111',file)
        lib[name]=lib[name]._replace(image=(PhotoImage(file=file),PhotoImage(file=file[:-4]+'2.png')))
   