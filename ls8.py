import sys
from cpu import *
# new instance on=f class CPU
cpu = CPU()

cpu.load(sys.argv[1])
cpu.run()