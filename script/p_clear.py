from mcpi.minecraft import Minecraft, mcpy
from mcpi.vec3 import Vec3
from util.coordinates import mc, RelativeCoordinates


@mcpy
def clearslope(playerName="xiaole", width=3, height=3, far=0):
    """
    以自己为中心，向面前清出一片斜坡
    如果斜坡前后距离 far 没有传入，那前后距离和高一样
    """
    if far == 0:
        far = height
    player = mc.getPlayer(playerName)
    offset = Vec3(-int(width / 2), 0, 0)
    rc = RelativeCoordinates(player, offset)
    slope = far / (height - 1)
    for level in range(1, height):
        rc.setBlocks(*(0, level, -1), *(width, level, int(-level * slope)), "空气")


@mcpy
def cr(*params):
    """
    clearslope 的缩写命令
    """
    clearslope(*params)


@mcpy
def clear(playerName="xiaole", width=3, height=3, far=3, blockname="空气"):
    """
    以自己为中心，用指定方块清除面前一个区域
    """
    player = mc.getPlayer(playerName)
    offset = Vec3(-int(width / 2), 0, 0)
    rc = RelativeCoordinates(player, offset)
    rc.setBlocks(*(0, 0, -1), *(width - 1, height - 1, -far), blockname)


@mcpy
def fill(*params):
    """
    clear 的别名
    """
    clear(*params)


# 单独运行的话，执行下面测试代码
if __name__ == "__main__":
    fill("xiaole", 3, 3, 3, "煤炭块")
