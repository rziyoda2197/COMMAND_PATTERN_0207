from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def on(self):
        print("Light ON")

    def off(self):
        print("Light OFF")


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


class Remote:
    def __init__(self):
        self.history = []

    def press(self, cmd):
        cmd.execute()
        self.history.append(cmd)


light = Light()
remote = Remote()

remote.press(LightOnCommand(light))
remote.press(LightOffCommand(light))
