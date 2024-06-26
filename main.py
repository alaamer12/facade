# Subsystem classes
class CPU:
    def freeze(self):
        pass

    def jump(self, position):
        pass

    def execute(self):
        pass

class Memory:
    def load(self, position, data):
        pass

class HardDrive:
    def read(self, lba, size):
        pass

# Facade
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load(0, self.hard_drive.read(0, 1024))
        self.cpu.jump(10)
        self.cpu.execute()

# Client code
def main():
    computer_facade = ComputerFacade()
    computer_facade.start()

if __name__ == "__main__":
    main()
