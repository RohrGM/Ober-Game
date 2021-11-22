from util.Animation import Animation
from util.Vector2 import Vector2


class AnimationData:
    ANIMATIONS = {
        "player_0": {
            "arms_idle": {
                "speed": 7,
                "position": Vector2(0, 0),
                "frames": 3,
                "size": Vector2(32, 19),
                "loop": True
            },
            "arms_run": {
                "speed": 5,
                "position": Vector2(96, 0),
                "frames": 4,
                "size": Vector2(32, 19),
                "loop": True
            },
            "arms_shoot": {
                "speed": 2,
                "position": Vector2(0, 32),
                "frames": 3,
                "size": Vector2(32, 19),
                "loop": False
            },
            "arms_reload": {
                "speed": 4,
                "position": Vector2(0, 64),
                "frames": 8,
                "size": Vector2(32, 19),
                "loop": False
            },
            "arms_special": {
                "speed": 4,
                "position": Vector2(0, 96),
                "frames": 7,
                "size": Vector2(32, 32),
                "loop": False
            },
            "legs_idle": {
                "speed": 7,
                "position": Vector2(0, 19),
                "frames": 3,
                "size": Vector2(32, 13),
                "loop": True
            },
            "legs_run": {
                "speed": 5,
                "position": Vector2(96, 19),
                "frames": 4,
                "size": Vector2(32, 13),
                "loop": True
            }
        },
        "player_1": {
            "arms_idle": {
                "speed": 7,
                "position": Vector2(0, 192),
                "frames": 3,
                "size": Vector2(32, 20),
                "loop": True
            },
            "arms_run": {
                "speed": 5,
                "position": Vector2(96, 192),
                "frames": 4,
                "size": Vector2(32, 20),
                "loop": True
            },
            "arms_shoot": {
                "speed": 1,
                "position": Vector2(0, 224),
                "frames": 3,
                "size": Vector2(32, 20),
                "loop": False
            },
            "arms_reload": {
                "speed": 5,
                "position": Vector2(96, 224),
                "frames": 5,
                "size": Vector2(32, 20),
                "loop": False
            },
            "arms_special": {
                "speed": 4,
                "position": Vector2(0, 96),
                "frames": 7,
                "size": Vector2(32, 32),
                "loop": False
            },
            "legs_idle": {
                "speed": 7,
                "position": Vector2(0, 19),
                "frames": 3,
                "size": Vector2(32, 13),
                "loop": True
            },
            "legs_run": {
                "speed": 5,
                "position": Vector2(96, 19),
                "frames": 4,
                "size": Vector2(32, 13),
                "loop": True
            }
        },
        "zombie_1": {
            "run": {
                "speed": 5,
                "position": Vector2(0, 128),
                "frames": 4,
                "size": Vector2(32, 32),
                "loop": True
            },
            "attack": {
                "speed": 5,
                "position": Vector2(128, 128),
                "frames": 4,
                "size": Vector2(32, 32),
                "loop": True
            },
            "dead": {
                "speed": 3,
                "position": Vector2(0, 160),
                "frames": 5,
                "size": Vector2(32, 32),
                "loop": False
            }
        }
    }

    @staticmethod
    def get_anim_list(character: str, list_name: list, agent: object) -> dict:
        animations = {}
        for name in list_name:
            current_dict = AnimationData.ANIMATIONS[character][name]
            animations[name] = Animation(
                speed=current_dict["speed"],
                position=current_dict["position"],
                frames=current_dict["frames"],
                size=current_dict["size"],
                loop=current_dict["loop"],
                agent=agent
            )
        return animations
