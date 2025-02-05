# Changed the growth speed of the fire to be dependent on the score.

from designer import *
from random import randint

World = {'plane': DesignerObject,
         'plane speed': int,
         'drops': [DesignerObject],
         'fires': [DesignerObject],
         'score': int,
         'counter': DesignerObject}

def create_world() -> World:
    return {'plane': create_plane(),
            'plane speed': PLANE_SPEED,
            'drops': [],
            'fires': [],
            'score': 0,
            'counter': text('black', '', 40, 400, 45)}

# make a plane
def create_plane() -> DesignerObject:
    plane = image("plane.png")
    plane['scale'] = .30
    plane['y'] = 150
    return plane

# make plane move
PLANE_SPEED = 5

def move_plane(world: World):
    world['plane']['x'] += world['plane speed']

# Helper functions
def head_left(world: World):
    world['plane speed'] = -PLANE_SPEED
    world['plane']['flip_x'] = True

def head_right(world: World):
    world['plane speed'] = PLANE_SPEED
    world['plane']['flip_x'] = False

# bounce plane
def bounce_plane(world: World):
    if world['plane']['x'] > get_width():
        head_left(world)
    elif world['plane']['x'] < 0:
        head_right(world)

# control plane
def flip_plane(world: World, key: str):
    if key == 'left':
        head_left(world)
    elif key == 'right':
        head_right(world)

# droplet 
def create_water_drop() -> DesignerObject:
    return circle("blue", 12)

# move droplet
def move_below(bottom: DesignerObject, top: DesignerObject):
    bottom['y'] = top['y'] + bottom['height']/2
    bottom['x'] = top['x']

# create droplets
def drop_water(world: World, key: str):
    if key == 'space':
        new_drop = create_water_drop()
        move_below(new_drop, world['plane'])
        world['drops'].append(new_drop)

# drop the droplets
WATER_DROP_SPEED = 5

def make_water_fall(world):
    for drop in world['drops']:
        drop['y'] += WATER_DROP_SPEED

# remove drops
def destroy_waters_on_landing(world):
    kept = []
    for drop in world['drops']:
        if drop['y'] < get_height():
            kept.append(drop)
    world['drops'] = kept

# fire
def create_fire() -> DesignerObject:
    fire = image('fire1.png')
    fire['scale_x'] = .1
    fire['scale_y'] = .1
    fire['anchor'] = 'midbottom'
    fire['x'] = randint(0, get_width())
    fire['y'] = get_height()
    return fire

# grow fire
def grow_fire(world: World):
    for fire in world['fires']:
        fire['scale_x'] += 0.0015 + (world['score'] * 0.00002)
        fire['scale_y'] += 0.0015 + (world['score'] * 0.00002)
        
# make random fires
def make_fires(world: World):
    not_too_many_fires = len(world['fires']) < 10
    random_chance = randint(0, 9) == 1
    if not_too_many_fires and random_chance:
        world['fires'].append(create_fire())

# pause on big fire
def there_are_big_fires(world) -> bool:
    any_big_fires_so_far = False
    for fire in world['fires']:
        any_big_fires_so_far = fire['scale_x'] >= 1 or False
    return any_big_fires_so_far
    
# update counter
def update_counter(world):
    world['counter']['text'] = str(world['score'])
    
# collision detection
def collide_water_fire(world):
    destroyed_fires = []
    destroyed_drops = []
    # Compare every drop to every fire
    for drop in world['drops']:
        for fire in world['fires']:
            # Check if there are any collisions between each pair
            if colliding(drop, fire):
                # Remember to remove this drop and fire
                destroyed_drops.append(drop)
                destroyed_fires.append(fire)
                # And increase our score accordingly
                world['score'] += 1
    # Remove any fires/drops that were identified as colliding
    world['drops'] = filter_from(world['drops'], destroyed_drops)
    world['fires'] = filter_from(world['fires'], destroyed_fires)

def filter_from(old_list: list, elements_to_not_keep: list) -> list:
    new_values = []
    for item in old_list:
        if item not in elements_to_not_keep:
            new_values.append(item)
    return new_values

# end print
def print_score(world):
    print("Your score was", world['score'])

def flash_game_over(world):
    world['counter']['text'] = "GAME OVER!"


when('starting', create_world)
when('updating', move_plane)
when('updating', bounce_plane)
when('typing', flip_plane)
when('typing', drop_water)
when('updating', make_water_fall)
when('updating', destroy_waters_on_landing)
when('updating', grow_fire)
when('updating', make_fires)
when('updating', update_counter)
when('updating', collide_water_fire)
#when(there_are_big_fires, pause)
when(there_are_big_fires, print_score, flash_game_over, pause)
start()