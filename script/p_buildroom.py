from mcpi.minecraft import Minecraft, mcpy
from mcpi.vec3 import Vec3
from util.coordinates import mc, RelativeCoordinates


@mcpy
def buildroom(playerName="xiaole", innerWidth=3, innerLength=0):
    """
    以自己为中心造一个空玻璃房. buildroom(玩家名字, 宽左右, 长前后)
    如果长没有传入，那长宽相等
    """
    if innerLength == 0:
        innerLength = innerWidth

    player = mc.getPlayer(playerName)

    # 起点x1,y1（0,0）距离player的偏移
    # 墙加屋檐要占2格厚度，造完后自己在屋子正中间，那0,0点偏移为一半宽度+2
    offset = Vec3(-int(innerWidth / 2 + 2), 0, -int(innerLength / 2 + 2))

    rc = RelativeCoordinates(player, offset)

    # 终点x2,y2的坐标
    x2 = innerWidth + 3  # 房子x2等于内部宽度+4-1，x坐标从0开始所以要-1
    y2 = innerLength + 3  # y2也一样

    # 清空位置，5层高
    rc.setBlocks(*[0, 0, 0], *[x2, 5, y2], "空气")

    # -1层铺地板
    rc.setBlocks(*[1, -1, 1], *[x2 - 1, -1, y2 - 1], "白桦木板")

    # 搭4根柱子
    rc.setBlocks(*[1, 0, 1], *[1, 3, 1], "白桦原木")
    rc.setBlocks(*[x2 - 1, 0, 1], *[x2 - 1, 3, 1], "白桦原木")
    rc.setBlocks(*[1, 0, y2 - 1], *[1, 3, y2 - 1], "白桦原木")
    rc.setBlocks(*[x2 - 1, 0, y2 - 1], *[x2 - 1, 3, y2 - 1], "白桦原木")

    # 4面玻璃墙
    rc.setBlocks(*[2, 0, 1], *[x2 - 2, 2, 1], "玻璃")
    rc.setBlocks(*[x2 - 1, 0, 2], *[x2 - 1, 2, y2 - 2], "玻璃")
    rc.setBlocks(*[2, 0, y2 - 1], *[x2 - 2, 2, y2 - 1], "玻璃")
    rc.setBlocks(*[1, 0, 2], *[1, 2, y2 - 2], "玻璃")

    # 屋檐
    rc.setBlocks(*[1, 4, 1], *[x2 - 1, 4, 1], "白桦木楼梯", 3)
    rc.setBlocks(*[x2 - 1, 4, 2], *[x2 - 1, 4, y2 - 1], "白桦木楼梯", 0)
    rc.setBlocks(*[1, 4, y2 - 1], *[x2 - 2, 4, y2 - 1], "白桦木楼梯", 1)
    rc.setBlocks(*[1, 4, 2], *[1, 4, y2 - 2], "白桦木楼梯", 2)
    rc.setBlocks(*[0, 3, 0], *[x2, 3, 0], "白桦木楼梯", 3)
    rc.setBlocks(*[x2, 3, 1], *[x2, 3, y2], "白桦木楼梯", 0)
    rc.setBlocks(*[0, 3, y2], *[x2 - 1, 3, y2], "白桦木楼梯", 1)
    rc.setBlocks(*[0, 3, 1], *[0, 3, y2 - 1], "白桦木楼梯", 2)

    # 内檐
    rc.setBlocks(*[2, 3, 1], *[x2 - 2, 3, 1], "白桦木板")
    rc.setBlocks(*[x2 - 1, 3, 2], *[x2 - 1, 3, y2 - 2], "白桦木板")
    rc.setBlocks(*[2, 3, y2 - 1], *[x2 - 2, 3, y2 - 1], "白桦木板")
    rc.setBlocks(*[1, 3, 2], *[1, 3, y2 - 2], "白桦木板")
    rc.setBlocks(*[2, 4, 2], *[x2 - 2, 4, 2], "白桦木板")
    rc.setBlocks(*[x2 - 2, 4, 2], *[x2 - 2, 4, y2 - 2], "白桦木板")
    rc.setBlocks(*[2, 4, y2 - 2], *[x2 - 2, 4, y2 - 2], "白桦木板")
    rc.setBlocks(*[2, 4, 2], *[2, 4, y2 - 2], "白桦木板")

    # 屋顶
    rc.setBlocks(*[3, 4, 3], *[x2 - 3, 4, y2 - 3], "玻璃")

    # 光源
    rc.setBlock(*[3, 5, 3], "灯笼")
    rc.setBlock(*[3, 5, y2 - 3], "灯笼")
    rc.setBlock(*[x2 - 3, 5, 3], "灯笼")
    rc.setBlock(*[x2 - 3, 5, y2 - 3], "灯笼")


@mcpy
def br(*params):
    """
    buildroom 的缩写命令
    """
    buildroom(*params)


# 单独运行的话，执行下面测试代码
if __name__ == "__main__":
    buildroom("xiaole", 3)
