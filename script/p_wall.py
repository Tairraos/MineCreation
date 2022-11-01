from mcpi.minecraft import Minecraft, mcpy
from mcpi.vec3 import Vec3
from util.coordinates import mc, RelativeCoordinates


@mcpy
def wall(playerName="xiaole", length=5, height=5, type=1, blockname="錾制石砖"):
    """
    在自己前方堆墙
    /p wall 名字 长度 高度 类型 方块名
    类型是数字
        1 按站立位置计算固定高度的墙
        2 固定高度墙顶上奇数格添一个装饰块
        3 按地型高低计算的动态高度墙
    """
    player = mc.getPlayer(playerName)
    rc = RelativeCoordinates(player, Vec3(0, 0, -length))
    if type < 3:
        rc.setBlocks(0, 0, 0, 0, height - 1, length - 1, blockname)
        if type == 2:
            for z in range(0, length, 2):
                rc.setBlock(0, height, z, blockname)
    else:
        for z in range(length):
            bottom = rc.getHeight(0, z) - rc.basePos.y + 1
            top = bottom + height
            rc.setBlocks(0, bottom, z, 0, top, z, blockname)
            print(0, bottom, z, 0, top, z, blockname)


# 单独运行的话，执行下面测试代码
if __name__ == "__main__":
    wall("xiaole", 10, 2, 2)
