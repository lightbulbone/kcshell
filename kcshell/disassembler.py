import os
from kcshell.kcshell import Kcshell
from capstone import *
from binascii import unhexlify

class Disassembler(Kcshell):
    def __init__(self):
        ''' creates a new disassembler instance '''
        Kcshell.__init__(self)
        self.prompt = 'disasm> '
        self.intro = 'Default Disassembler architecture is x86 (32 bits)'
        self._cs = Cs(CS_ARCH_X86, CS_MODE_32)
        self.base_address = 0x00400000

    def get_cs_archs(self):
        ''' capstone disassembler '''
        cs_archs = {
            'x16':     {'arch': CS_ARCH_X86,
                        'mode': CS_MODE_16,
                        'desc': "x86 (16-bit)"},
            'x86':     {'arch': CS_ARCH_X86,
                        'mode': CS_MODE_32,
                        'desc': "x86 (32-bit)"},
            'x64':     {'arch': CS_ARCH_X86,
                        'mode': CS_MODE_64,
                        'desc': "x86 (64-bit)"},
            'arm':     {'arch': CS_ARCH_ARM,
                        'mode': CS_MODE_ARM,
                        'desc': "ARM (32-bit)"},
            'arm_t':   {'arch': CS_ARCH_ARM,
                        'mode': CS_MODE_THUMB,
                        'desc': "ARM (Thumb/Thumb-2)"},
            'arm_m':   {'arch': CS_ARCH_ARM,
                        'mode': CS_MODE_MCLASS+CS_MODE_THUMB,
                        'desc': "ARMv7-M (Cortex-M4)"},
            'arm64':   {'arch': CS_ARCH_ARM64,
                        'mode': CS_MODE_LITTLE_ENDIAN,
                        'desc': "ARMv8 (AArch64)"},
            }
        return cs_archs

    def cleanup(self, input_str):
        input_str = input_str.replace(" ", "")
        input_str = input_str.replace("\\x", "")
        return input_str.replace("0x", "")

    def help_lsarchs(self):
        print("List supported Disassembler architectures.")

    def do_lsarchs(self, dummy):
        archs_dict = self.get_cs_archs()
        for k, v in archs_dict.items():
            print("{}: {}".format(k, v['desc']))

    def help_setarch(self):
        print("Set Disassembler architecture. To list available options type 'lsarchs'.")

    def do_setarch(self, arch):
        try:
            if arch:
                cs_dict = self.get_cs_archs()[arch]
                self._cs = Cs(cs_dict['arch'], cs_dict['mode'])
                print('Disassembler architecture is now {}'.format(cs_dict['arch']))
            else:
                print("Usage: setarch <arch>\nType 'lsarchs' to list all supported architectures.")
        except CsError as e:
            print("Error: %s" %e)

    def default(self, user_input):
        ''' if no other command was invoked '''
        try:
            for i in self._cs.disasm(unhexlify(self.cleanup(user_input)), self.base_address):
                print("0x%08x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))
        except CsError as e:
            print("Error: %s" %e)

