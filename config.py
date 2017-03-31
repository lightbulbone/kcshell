from assembler import Assembler
from disassembler import Disassembler

def get_op_modes():
    OP_MODES = {
        'asm' : Assembler(),
        'disasm' : Disassembler()
    }
    return OP_MODES

def get_default_op_mode():
    return 'asm'

def get_cs_archs():
    ''' capstone disassembler '''
    cs_archs = (
        {
	'x16':     (CS_ARCH_X86,     CS_MODE_16),
	'x86':     (CS_ARCH_X86,     CS_MODE_32),
	'x64':     (CS_ARCH_X86,     CS_MODE_64),
        'arm':     (CS_ARCH_ARM,     CS_MODE_ARM),
	'arm_t':   (CS_ARCH_ARM,     CS_MODE_THUMB),
	'arm64':   (CS_ARCH_ARM64,   CS_MODE_LITTLE_ENDIAN),
	'mips32':  (CS_ARCH_MIPS,    CS_MODE_MIPS32),
	'mips64':  (CS_ARCH_MIPS,    CS_MODE_MIPS64),
        })
    return cs_archs
