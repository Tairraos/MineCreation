# Tairraos 简化并翻译了 Command Server 代码
# 原代码由 wenshengwang 编写
# BSD License
"""这是一个TCP服务。侦听本地主机端口4731提供服务。
服务启动时，会扫描 "p_" 开头的python文件将它们作为模块加载。
这些模块里，如果在 docstring 里用 "_mcpy " 描述的方法，或用 "@mcpy" 修饰符修饰的方法，会被注册为命令。
当服务从游戏里收到一个命令时，如果收到的命令是注册命令，对应的程序就会被执行。
"""

import os
import sys
import glob
import socketserver
import threading
import types
import importlib
import time

HOST = "localhost"
PORT = 4731

plugin_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, plugin_dir)

KEEP_RUNNING = True
exit_signal = threading.Event()


def keep_running():
    return KEEP_RUNNING


def register_commands():
    global mc_functions
    mc_functions = {}
    pp_files = glob.glob(os.path.join(plugin_dir, ".", "p_*.py"))
    # import all files and put minecraft function into the mc_functions dict
    for pp_file in pp_files:
        basename = os.path.basename(pp_file)
        if basename != "__init__.py":
            try:
                name = "" + basename[:-3]
                if name in sys.modules:
                    module = importlib.reload(sys.modules[name])
                else:
                    module = importlib.import_module(name)
                for item in dir(module):
                    if isinstance(module.__dict__[item], types.FunctionType):
                        docs = module.__dict__[item].__doc__
                        if docs and docs.startswith("_mcpy"):
                            print("注册命令:", module.__dict__[item].__name__)
                            mc_functions[item] = module.__dict__[item]
            except (NameError, ImportError) as e:
                print(e)


class MyTCPHandler(socketserver.BaseRequestHandler):
    def parseArg(self, arg):
        # 把全数字的arg变成数值型，方便p命令里的数字参数使用
        test = str(arg)
        if test.isdigit():
            return int(test)
        try:
            return float(test)
        except ValueError:
            pass
        return arg

    def handle(self):
        global KEEP_RUNNING
        self.data = self.request.recv(1024)
        # firt 2 bytes are length info, from Java's writeUTF
        args = self.data[2:].decode("utf-8").split()
        cmd = args[0]
        pargs = list(map(lambda s:self.parseArg(s), args[1:]))
        if cmd == "list":
            s = "可用的命令: %s" % (" ".join(list(mc_functions.keys())))
            self.request.sendall(s.encode("utf-8"))
        elif cmd == "help":
            s = 'JuicyRaspberryPie: 把你的 Python 程序放在 pplugins 文件夹下就可以使用, "/p 命令" 来调用程序里的方法, "/p list" 可以查看所有支持的命令。'
            self.request.sendall(s.encode("utf-8"))
        elif cmd == "update":
            register_commands()
            s = "发现命令: " + " ".join(mc_functions)
            self.request.sendall(s.encode("utf-8"))
        elif cmd == "shutdownserver":
            print("命令服务收到关闭命令，正在关闭。")
            KEEP_RUNNING = False
            self.request.sendall("命令服务收到关闭命令，正在关闭".encode("utf-8"))
        elif cmd in mc_functions:
            threading.Thread(target=mc_functions[cmd], args=tuple(pargs)).start()
            self.request.sendall("ok".encode("utf-8"))
        else:
            self.request.sendall(("未知的命令: %s" % args).encode("utf-8"))


register_commands()

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    print("命令服务在此接口提供服务： %s:%d." % (HOST, PORT))
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.socket.settimeout(1)

    def server_serve():
        while keep_running():
            server.handle_request()

    thread = threading.Thread(target=server_serve)
    thread.daemon = True
    try:
        thread.start()
        while keep_running():
            time.sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        print("结束中……")
        KEEP_RUNNING = False

    thread.join()
