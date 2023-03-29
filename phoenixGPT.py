from objectionpy import preset, enums, assets, objection
from objectionpy.frames import *

scene = objection.Scene()

def frameWithCharacterPose(characterChosen, whatTheySay, pose, bubbleChosen):
    scene.frames.append(Frame(
    char = FrameCharacter(
        character=characterChosen,
        poseSubstr=pose
    ),
    text = whatTheySay,
    bubble = bubbleChosen
))

# PASTE THE CHATGPT OUTPUT UNDER HERE 








with open('./scene.objection', 'w') as f:
    f.write(scene.makeObjectionFile(scene.compile()))
