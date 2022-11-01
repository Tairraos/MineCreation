from mcpi.minecraft import Minecraft, mcpy
from mcpi.vec3 import Vec3
from util.namelib import ID, NAME

# 建立mc连接对象
mc = Minecraft.create()

# 定义一套相对坐标系
# 相对坐标：原点0,0在player的offset位置处 / X坐标左向右增加 / Y坐标从前向后增加 / player脸朝向定义为0
# 世界坐标：原点0,0为种子生成起始位置 / X坐标从西向东增加 / Z轴坐标从北向南增加 / 北定义为方向0
class RelativeCoordinates:
    def __init__(self, player, offset=Vec3(0, 0, 0)):
        self.player = player
        self.basePos = player.getTilePos()  # 获得玩家位置
        self.facing = player.getFacing()  # 玩家脸的朝向数据

        self.offset = offset
        # 根据脸的朝向修正坐标
        fixBundle = [
            lambda o: Vec3(o.x, o.y, o.z),  # 朝北, dx =  X, dz =  Z
            lambda o: Vec3(-o.z, o.y, o.x),  # 朝东, dx = -Z, dz =  X
            lambda o: Vec3(-o.x, o.y, -o.z),  # 朝南, dx = -X, dz = -Z
            lambda o: Vec3(o.z, o.y, -o.x),  # 朝西, dx =  Z, dz = -X
        ]
        self.absFix = fixBundle[self.facing]
        self.rcFix = fixBundle[(4 - self.facing) % 4]

    # 把相对坐标换算成绝对坐标
    def toAbsPos(self, x, y, z):
        return self.basePos + self.absFix(Vec3(x, y, z) + self.offset)

    # 换算绝对方向
    def toAbsDir(self, dir):
        return (dir + self.facing - 1) % 4

    # 换算相对坐标
    def toRcPos(self, x, y, z):
        return self.rcFix(Vec3(x, y, z) - self.basePos - self.offset)

    # 换算相对方向
    def toRcDir(self, dir):
        return (dir + 5 - self.facing) % 4

    # 更新基准坐标为玩家当前坐标和朝向
    def updatePos():
        self.basePos = self.player.getTilePos()  # 获得玩家位置
        self.facing = self.player.getFacing()  # 玩家脸的朝向数据

    # 重新设置原点坐标基准，以距离self.basePos offset的坐标为0，0
    def setOffset(self, offset=Vec3(0, 0, 0)):
        self.offset = offset

    def setBlock(self, x, y, z, blockname, dir=0):
        mc.setBlock(*self.toAbsPos(x, y, z), ID(blockname), self.toAbsDir(dir))

    def setBlocks(self, x1, y1, z1, x2, y2, z2, blockname, dir=0):
        mc.setBlocks(*self.toAbsPos(x1, y1, z1), *self.toAbsPos(x2, y2, z2), ID(blockname), self.toAbsDir(dir))

    def getBlockWithData(self, x, y, z):
        return mc.getBlockWithData(*self.toAbsPos(x, y, z))

    def getBlock(self, x, y, z):
        return mc.getBlock(*self.toAbsPos(x, y, z))

    def getBlocks(self, x1, y1, z1, x2, y2, z2):
        return mc.getBlocks(*self.toAbsPos(x1, y1, z1), *self.toAbsPos(x2, y2, z2))

    def spawnEntity(self, x, y, z, blockname, dir=0):
        mc.spawnEntity(*self.toAbsPos(x, y, z), ID(blockname), dir)

    # 用方块填充区域，区域为距离 self.basePos 多少个方块以内的某层(y)
    def setAreaBlocks(self, d, y, blockname, dir=0):
        mc.setBlocks(*self.toAbsPos(-d, y, -d), *self.toAbsPos(d, y, d), ID(blockname), self.toAbsDir(dir))

    def getAreaBlocks(self, d, y):
        return mc.getBlocks(*self.toAbsPos(-d, y, -d), *self.toAbsPos(d, y, d))

    def getHeight(self, x, z):
        (ax, ay, az) = self.toAbsPos(x, 50, z)
        return mc.getHeight(ax, az)
