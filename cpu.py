import sys
import time


HLT = 0b00000001
PRN = 0b01000111
LDI = 0b10000010
ADD = 0b10100000
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RET = 0b00010001
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110

pointer = 7

class CPU:

    def __init__(self):
        self.ram = [0] * 26
        self.reg = [0] * 8
        self.running = True
        self.pc = 0
        self.f1 = 0b00000000 #CMP flag
        self.branchtable = {}
        self.branchtable[HLT] = self.handle_HLT
        self.branchtable[PRN] = self.handle_PRN
        self.branchtable[LDI] = self.handle_LDI
        self.branchtable[ADD] = self.handle_ADD
        self.branchtable[MUL] = self.handle_MUL
        self.branchtable[PUSH] = self.handle_PUSH
        self.branchtable[POP] = self.handle_POP
        self.branchtable[CALL] = self.handle_CALL
        self.branchtable[RET] = self.handle_RET
        self.branchtable[JEQ] = self.handle_JEQ
        self.branchtable[JNE] = self.handle_JNE
        self.branchtable[JMP] = self.handle_JMP
        self.branchtable[CMP] = self.handle_CMP
        self.reg[pointer] = 0xf4


    #set up memory address register
    def ram_read(self, MAR):
        return self.ram[MAR]

    #set up memeory address register and memory data register
    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR
    
    def HLT_Handle(self, _x, _y):
        self.running = False

    #set up print to print a register value
    def PRN_Handle(self, x, _):
        print(self.reg[x])
        self.pc += 3

    # set up a register to an actual value
    def LDI_Handle(self, x, y):
        self.reg[x] = y
        self.pc += 3

    def MUL_Handle(self, x, y):
        self.alu('mul', x, y)
        self.pc += 3

    def ADD_Handle(self, x, y):
        self.alu('add', x, y)
        self.pc += 3

    def PUSH_Handle(self, x, _):
        # push decrease sp
        self.reg[pointer] -= 1
        # code the value to the slot
        reg_v = self.reg[x]
        self.ram_write(self.reg[pointer], reg_v)

    def POP_Handle(self, x, _):
        #Where is the sp pointing to
        sp = self.ram_read(self.reg[pointer])

        #set value to register at index
        self.reg[x] = sp
        self.pc += 2

    def CALL_Handle(self, x, y):

        return_address = self.pc + 2

        self.reg[pointer] -= 1

        self.ram_write(self.reg[pointer], return_address)

        self.pc = self.reg[x]



    def handle_RET(self, x, y):
        return_address = self.ram[self.reg[pointer]]
        self.pc = return_address
        self.reg[pointer] += 1



    def handle_JEQ(self, x, _y):
        # if flag is equal
        if self.fl == 0b00000001:
            # jump to register we pass in
            self.pc = self.reg[x]
        else:
            self.pc += 2

    def handle_JNE(self, x, _y):
        # if flag is not equal
        if self.fl != 0b00000001:
            # jump to register we pass in
            self.pc = self.reg[x]
        else:
            self.pc += 2
            

    def handle_JMP(self, x, y):
        self.pc = self.reg[x]

    def handle_CMP(self, x, y):
        self.alu("CMP", x, y)
        self.pc += 3

    


    

    
        