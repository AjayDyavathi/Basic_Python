class CPU:

    def __init__(self, memory, ram, gen, cat, gpu):
        self.memory = memory
        self.ram = ram
        self.gen = gen
        self.cat = cat
        self.gpu = gpu


    def info(self):
        print('RAM is',self.ram)
        print('Storage is', self.memory)
        print('It has ',self.gen,' generation',self.cat,' processor')
        print('with ',self.gpu, ' graphics memory')

myDream = CPU('4 TB','32 GB',8,'i9','6 GB')
myDream.info()
