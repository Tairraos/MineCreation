from mcpi.minecraft import Minecraft, mcpy
from mcpi.vec3 import Vec3
from util.coordinates import mc, RelativeCoordinates


@mcpy
def pos(playerName="xiaole", x=None, z=None):
    """
    查看坐标，或者安全传送。只需要给XZ坐标，传送目标Y轴会在最高一个非空气的方块上方。不会把玩家卡在石头里。
    """
    player = mc.getPlayer(playerName)

    if player:  # player存在的话
        facing = player.getFacing()
        pos = player.getTilePos()
        facingInfo = ["北,向前Z减小", "东,向前X增加", "南,向前Z增加", "西,向前X减小"][facing]
        if x is None:
            mc.postToChat("当前坐标为: x={0} z={1} 朝向{2}".format(pos.x, pos.z, facingInfo))
        else:
            y = mc.getHeight(x, z) + 1
            player.setTilePos(x, y, z)
            mc.postToChat("已经瞬移到 x={0}, z={1}".format(x, z))


# 单独运行的话，执行下面测试代码
if __name__ == "__main__":
    pos("xiaole")
