init python:

    class MoerinnState:
        def __init__(self):
            self.met = False
            self.name = "???"

            self.heart = 0
            self.anger = 0
            self.sadism = 0
            self.tease = False

            self.check = 0
            self.caught = False

            self.passive_aggression = False

    class PlayerState:
        def __init__ (self):

            self.health = 100
            self.sanity = 100
            self.drugged = 0
            self.bonding = 0

            self.pov = {
                "meek": 0,
                "happy": 0,
                "blunt": 0,
                "rude": 0,
                "quiet": 0,
                "loud": 0
            }

            self.give_name = False
            self.tas = False
            self.cosconreply = False
            self.aah = False
            self.friend_reply = False
            self.wdyewk = False
            self.dddres = False
            self.yelling_diag = False
            self.lie_meter = 0
            self.corrans = 0
            self.idk = 0
    
    class WorldState:
        def __init__ (self):
            self.check_drawers = False
            self.check_floors = False
            self.check_plant = False
            self.check_boxes = False
            self.check_curtains = False

            self.butterfly = False
            self.pink_card = False
            self.scene_finished = False
            self.dont_eat = False
            self.pretend_eat = False

    moerinn = MoerinnState()
    player = PlayerState()
    world = WorldState()