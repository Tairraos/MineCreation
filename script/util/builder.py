from mcpi.minecraft import Minecraft, mcpy
from mcpi.vec3 import Vec3

# 建立mc连接对象
mc = Minecraft.create()

# 给定两点, 返回范围内的坐标集
def area(x1, y1, x2, y2):
    return [[x, y] for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]


# X,Y List构成的阵列
def dots(xn, yn):
    return [[x, y] for x in xn for y in yn]


# X,Y List构成的阵列
def dotsxr(xn, yn):
    return [
        [x, y]
        for x in filter((lambda n: not n in xn), range(min(xn), max(xn)))
        for y in yn
    ]


def dotsyr(xn, yn):
    return [
        [x, y]
        for x in xn
        for y in filter((lambda n: not n in yn), range(min(yn), max(yn)))
    ]


# 用建筑数据层层建造
def build(buildData, levelUp=1):
    dir = buildData[0].get("dir")
    base = buildData[0].get("base").clone()
    offset = buildData[0].get("offset").clone()
    fix = buildData[0].get("fixMethod")

    for line in buildData[1:]:
        items = line if type(line[0]) == list else [line]
        for item in items:
            matrial = item[0].split(":")[0]
            matrialData = (
                (int(item[0].split(":")[1]) + dir - 1) % 4 if ":" in item[0] else ""
            )
            for place in item[1:]:
                mc.setBlock(*(base + fix(Vec3(*place) + offset)), matrial, matrialData)
        offset.z += levelUp


# 方向校准类, 把观察坐标转换成MC坐标
# 观察坐标定义为在空中俯瞰地面, 左右为X轴, 向右增大；上下为Y轴, 向下增大。Y轴增大的方向为朝向, 东, 南, 西, 北。
class DIRECTION:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    FIX = [
        lambda o: Vec3(o.x, o.z, o.y),  # 朝北, dx = -X, dz = Y
        lambda o: Vec3(-o.y, o.z, o.x),  # 朝东, dx = -Y, dz = X
        lambda o: Vec3(-o.x, o.z, -o.y),  # 朝南, dx = X, dz = -Y
        lambda o: Vec3(o.y, o.z, -o.x),  # 朝西, dx = Y, dz = -X
    ]
