from mcpi.minecraft import Minecraft, mcpy
from mcpi.vec3 import Vec3
from util.builder import *
import time


playerName = "xiaole"

# 建立mc连接对象
mc = Minecraft.create()
player = mc.getPlayer(playerName)
# 玩家坐标
basePos = mc.player.getTilePos()
offsetPos = Vec3(-18, -24, -2)

# 玩家脸的方向
(px, py, pz) = mc.player.getDirection()
if abs(px) > abs(pz):
    if px > 0:
        direction = DIRECTION.EAST
    else:
        direction = DIRECTION.WEST
else:
    if pz > 0:
        direction = DIRECTION.SOUTH
    else:
        direction = DIRECTION.NORTH


# 定义建筑起始点, 就是参考点和设计点X:0,Y:0的关系。参考点通常是玩家站立的位置。
config = {"player": "xiaole", "offset": offsetPos}
# 数据层, List, 每个元素为一层。自下向上建
levelData = [
    ["prismarine", *area(0, 1, 0, 17), *area(1, 0, 28, 18), *area(29, 1, 29, 17)],  # level 0
    [  # level 1
        ["prismarine", *area(0, 1, 0, 17), *area(1, 0, 28, 0), *area(1, 18, 28, 18), *area(17, 19, 20, 23), *area(29, 1, 29, 17)],
        ["polished_diorite", *area(2, 2, 27, 16)],
        ["grass_block", *area(1, 1, 28, 1), *area(1, 17, 28, 17), *area(1, 2, 1, 16), *area(28, 2, 28, 16), *area(13, 12, 27, 16)],
        ["polished_diorite", *area(22, 16, 27, 16), *area(18, 13, 19, 13), *area(18, 15, 19, 15), *area(21, 12, 21, 16)],
        ["water", *area(3, 3, 7, 15), *area(8, 12, 11, 15)],
    ],
    [  # level 2
        ["flowering_azalea", *dotsxr([1, 5, 9, 13, 17, 18, 19, 20, 24, 28], [1, 17]), *dotsyr([1, 28], [1, 5, 9, 13, 17]), *area(18, 1, 19, 1)],
        ["stripped_oak_log", *dots([1, 5, 9, 13, 17, 20, 24, 28], [1, 17]), *dots([1, 28], [5, 9, 13])],
        ["rose_bush", *area(22, 12, 26, 15)],
        ["acacia_fence", [14, 14]],
        ["quartz_slab", [14, 13], [14, 15]],
        ["smooth_quartz_stairs:2", [15, 13], [15, 15]],
        ["glass_pane", *area(9, 10, 15, 10), *area(22, 10, 26, 10), *area(15, 8, 17, 8), *area(20, 8, 22, 8)],
        ["tinted_glass", [9, 10], [15, 10], [22, 10], [26, 10]],
        ["gray_concrete", *area(9, 3, 26, 3), *area(9, 4, 9, 9), *area(15, 6, 15, 9), *area(22, 6, 22, 9), *area(26, 4, 26, 9), [17, 8], [20, 8]],
        ["acacia_fence", [17, 11], [20, 11]],
        ["smooth_quartz_stairs:1", [25, 7]],
        ["smooth_quartz", *area(25, 4, 25, 6)],
    ],
    [  # level 3
        ["black_stained_glass_pane", *area(28, 2, 28, 16), *area(1, 2, 1, 16), *area(1, 17, 17, 17), *area(20, 17, 28, 17), *area(1, 1, 28, 1)],
        ["stripped_oak_log", *dots([1, 5, 9, 13, 17, 20, 24, 28], [1, 17]), *dots([1, 28], [5, 9, 13])],
        ["orange_carpet", [14, 14]],
        ["glass_pane", *area(9, 10, 15, 10), *area(22, 10, 26, 10), *area(15, 8, 17, 8), *area(20, 8, 22, 8)],
        ["tinted_glass", [9, 10], [15, 10], [22, 10], [26, 10]],
        ["gray_concrete", *area(9, 3, 26, 3), *area(9, 4, 9, 9), *area(15, 6, 15, 9), *area(22, 6, 22, 9), *area(26, 4, 26, 9), [17, 8], [20, 8]],
        ["acacia_fence", [17, 11], [20, 11]],
        ["smooth_quartz_stairs:1", [25, 6]],
        ["smooth_quartz", *area(25, 4, 25, 5)],
    ],
    [  # level 4
        ["glass_pane", *area(9, 10, 15, 10), *area(22, 10, 26, 10), *area(15, 8, 17, 8), *area(20, 8, 22, 8)],
        ["tinted_glass", [9, 10], [15, 10], [22, 10], [26, 10]],
        ["gray_concrete", *area(9, 3, 26, 3), *area(9, 4, 9, 9), *area(15, 6, 15, 9), *area(22, 6, 22, 9), *area(26, 4, 26, 9), [17, 8], [20, 8]],
        ["acacia_fence", [17, 11], [20, 11]],
        ["smooth_quartz_stairs:1", [25, 5]],
        ["smooth_quartz", [25, 4]],
    ],
    [  # level 5
        ["glass_pane", *area(9, 10, 15, 10), *area(22, 10, 26, 10), *area(15, 8, 17, 8), *area(20, 8, 22, 8)],
        ["tinted_glass", [9, 10], [15, 10], [22, 10], [26, 10]],
        ["gray_concrete", *area(9, 3, 26, 3), *area(9, 4, 9, 9), *area(15, 4, 22, 8), *area(26, 4, 26, 9), [15, 9], [22, 9]],
        ["acacia_trapdoor:3", *area(17, 9, 20, 11)],
        ["smooth_quartz_stairs:1", [25, 4]],
    ],
    [  # level 6
        ["white_concrete", *area(8, 2, 16, 11), *area(21, 2, 27, 11), *area(17, 2, 20, 8), *area(13, -2, 22, 1)],
        ["smooth_quartz_stairs:1", [25, 3]],
        ["air", *area(25, 4, 25, 9)],
    ],
    [  # level 7
        ["glass_pane", *area(8, 11, 16, 11), *area(21, 11, 27, 11), *area(16, 8, 21, 8), *area(8, 2, 13, 2), *area(22, 2, 27, 2)],
        ["glass_pane", *area(13, -1, 13, 1), *area(13, -2, 22, -2), *area(22, -1, 22, 1)],
        ["white_concrete", *area(8, 2, 8, 11), *area(27, 2, 27, 11), *area(16, 8, 16, 11), *area(21, 8, 21, 11)],
        ["smooth_quartz_stairs:1", [15, 10]],
        ["smooth_quartz", *area(15, 8, 15, 9)],
    ],
    [  # level 8
        ["glass_pane", *area(8, 11, 16, 11), *area(21, 11, 27, 11), *area(16, 8, 21, 8), *area(8, 2, 13, 2), *area(22, 2, 27, 2)],
        ["white_concrete", *area(8, 2, 8, 11), *area(27, 2, 27, 11), *area(16, 8, 16, 11), *area(21, 8, 21, 11)],
        ["smooth_quartz_stairs:1", [15, 9]],
        ["smooth_quartz", [15, 8]],
    ],
    [  # level 9
        ["glass_pane", *area(8, 11, 16, 11), *area(21, 11, 27, 11), *area(16, 8, 21, 8), *area(8, 2, 13, 2), *area(22, 2, 27, 2)],
        ["white_concrete", *area(8, 2, 8, 11), *area(27, 2, 27, 11), *area(16, 8, 16, 11), *area(21, 8, 21, 11)],
        ["smooth_quartz_stairs:1", [15, 8]],
    ],
    [  # level 10
        ["white_concrete", *area(8, 2, 16, 11), *area(21, 2, 27, 11), *area(17, 2, 20, 8)],
        ["smooth_quartz_stairs:1", [15, 7]],
        ["air", *area(15, 8, 15, 10)],
    ],
    [  # level 11
        ["orange_concrete", *area(12, 2, 23, 10)],
        ["smooth_red_sandstone_stairs:1", [15, 6]],
        ["air", *area(15, 7, 15, 9)],
    ],
    [  # level 12
        ["glass_pane", *area(12, 2, 23, 2), *area(12, 10, 23, 10)],
        ["orange_concrete", *area(12, 2, 12, 10), *area(23, 2, 23, 10)],
    ],
    [  # level 13
        ["glass_pane", *area(12, 2, 23, 2), *area(12, 10, 23, 10)],
        ["orange_concrete", *area(12, 2, 12, 10), *area(23, 2, 23, 10)],
    ],
    [  # level 14
        ["glass_pane", *area(12, 2, 23, 2), *area(12, 10, 23, 10)],
        ["orange_concrete", *area(12, 2, 12, 10), *area(23, 2, 23, 10)],
    ],
    ["orange_concrete", *area(12, 2, 23, 10)],  # level 15
]

singlyData = [
    config,
]
# mc.setBlocks(*(base + dir(Vec3(8, -2, 2) + offset)), *(base + dir(Vec3(27, 11, 16) + offset)), "air")
time.sleep(0.5)

build(config, levelData)
