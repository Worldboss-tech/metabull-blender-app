
from . import retargeting, lipsync, emotions, attach
from ..camera_movement import camera_movement


def handle_actions(actors: dict, data: dict):
    # Attach objects to the armature
    attach.attach(actors, data)

    # Add animations to actors
    retargeting.automate(actors, data)

    # Add lip sync to the actors
    lipsync.add_lip_sync(actors, data)

    # Add emotions
    emotions.add_emotions(actors, data)

    # Add camera animations
    camera_movement.set_camera_movement(data)