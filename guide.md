## 环境搭建指南

### 原理
- 使用 Java 版 Minecraft 连入自架的 SpiGot 服务器。
- 在多人模式下，数台电脑都可以加入建造同一个世界。
- [JuicyRaspberryPie](https://github.com/wensheng/JuicyRaspberryPie) 插件用 SpiGot API 的接口实现了一个 Command Server。
- 在服务器上写 Python，就能在每一台连入该 SpiGot 的 MineCraft 上使用指令执行它，创造和改变世界。
- 所有玩家用移动指令移动到同一区域，一起建造。（当然也可以自己躲在角落造自己的）

### 编译 SpiGot
- [SpiGot](https://github.com/SpigotMC/Spigot) 因为版权限制，Github 站点已关闭。
- 从 [SpiGot 团队的 Jenkins](https://hub.spigotmc.org/jenkins/job/BuildTools/) 下载最新的 `buildTool.jar`。
- 用 Java 17 执行命令：`java -jar BuildTools.jar --rev 版本`。
- 几分钟后打包完成，留下 `SpiGot-版本.jar`，其它都可以删除。
- 参考 [Wiki](https://www.spigotmc.org/wiki/spigot-installation/) 写一个启动 bat 或 sh 运行服务器。 
- Build 中使用的版本参数为你使用的 Java 版 Minecraft 的版本号。

### 编译 JuicyRaspberryPie
- 下载 [JuicyRaspberryPie](https://github.com/wensheng/JuicyRaspberryPie) 整个项目到 SpiGot 服务器。
- 解包，进入项目根文件夹执行命令 `mvn clean package`。
- 几分钟后打包完成，把 `JuicyRaspberryPie-版本.jar` 放入 SpiGot 的 Plugins 文件夹，其它删除。
- 重新启动 SpiGot 插件就会起作用。

### Minecraft 连入
- 运行和 SpiGot 版本相同的 Java版 Minecraft
- 选择多人游戏，添加服务器，填入 `xxx.xxx.xxx.xxx:25565`
- 十多秒后，服务器状态显示在 Minecraft 内，点击服务器图标连接进入游戏。
- `xxx.xxx.xxx.xxx` 指 SpiGot服务器电脑所在的 IP 地址。
- Minecraft 和 Spigot 需要在同一网络环境才能连入服务器。

### Python
- 以下操作在 SpiGot 服务器主机上。
- 准备好 Python 3.9，下载本项目并解包，进入项目文件夹。
- 执行命令启动 Command Server `python3 cmdsvr/pycmdsvr.py`
- 用 Python 控制 Minecraft 要用到的 API 都定义在 `mcpi/minecraft.py` 里。
- API 参数需要使用到方块名字在[我的世界物品表](我的世界物品表)文件夹。
- 写在 `pplugins` 下的 Python 程序，在重启 Command Server 后，可以在 Minecraft 里使用 `/p 函数名 参数 参数 ...` 执行。
- 也可以直接在项目根文件夹写 Python 程序，直接用 `python3 文件名` 执行，玩家可以立刻 Minecraft 里观察到变化。
