# kcshell

### What is it:

Simple Python3 based interactive assembly/disassembly shell for various architectures powered by [Keystone](http://www.keystone-engine.org/)/[Capstone](http://www.capstone-engine.org/).

I simply got tired of using [metasm_shell](https://github.com/rapid7/metasploit-framework/blob/master/tools/exploit/metasm_shell.rb) and [nasm_shell](https://github.com/rapid7/metasploit-framework/blob/master/tools/exploit/nasm_shell.rb) to assemble and disassemble code. [Keystone](https://github.com/keystone-engine/keystone) and [Capstone](https://github.com/aquynh/capstone) are awesome and... I like Python.

## How to install it:

```C
pip3 install kcshell
```

OR (assuming you have Keystone and Capstone build toolchains installed)

```C
git clone https://github.com/fdiskyou/kcshell
cd kcshell
python setup.py install
```

## Usage

By default 'kcshell' starts in 'assembler' mode (x86 32 bits). You can change modes with 'setmode', and you can also change the default architecture for both the 'assembler' and 'disassembler' with 'setarch'. 

```C
$ kcshell
-=[ kcshell 0.0.4 ]=-
Default Assembler architecture is x86 (32 bits)
asm> lsmodes
disasm, asm
asm> setmode disasm
Default Disassembler architecture is x86 (32 bits)
disasm> lsarchs
x86, mips32, arm_t, x64, arm, x16, arm64, mips64
disasm> setarch x64
Disassembler architecture is now x64
disasm> 
```

To assemble instructions just type the instructions in the command line.

```C
asm> jmp esp
"\xff\xe4"
asm> xor eax, eax
"\x31\xc0"
asm> jmp -500
"\xe9\x07\xfe\xff\xff"
asm> add esp,-1500
"\x81\xc4\x24\xfa\xff\xff"
asm> xor ecx,ecx ; mov ch, 0xc8 ; mov esi, edi ; mov edi, esp ; rep movsb
"\x31\xc9\xb5\xc8\x89\xfe\x89\xe7\xf3\xa4"
asm> setarch x64
Assembler architecture is now x64
asm> inc rax
"\x48\xff\xc0"
asm> 

```

To go from opcodes to instructions just type them in the command line.

```C
disasm> \xff\xe4
0x00400000:     jmp     esp
disasm> \x31\xc0
0x00400000:     xor     eax, eax
disasm> \x31\xc9\xb5\xc8\x89\xfe\x89\xe7\xf3\xa4
0x00400000:	xor	ecx, ecx
0x00400002:	mov	ch, 0xc8
0x00400004:	mov	esi, edi
0x00400006:	mov	edi, esp
0x00400008:	rep movsb	byte ptr es:[edi], byte ptr [esi]
disasm> setarch x64
Disassembler architecture is now x64
disasm> \x48\xff\xc0
0x00400000:     inc     rax
disasm> 

```

For help just use '?' or 'help \<command\>'.

```C
asm> ?

Documented commands (type help <topic>):
========================================
EOF  exit  help  lsarchs  lsmodes  quit  setarch  setmode

asm> setmode disasm
Default Disassembler architecture is x86 (32 bits)
disasm> ?

Documented commands (type help <topic>):
========================================
EOF  exit  help  lsarchs  lsmodes  quit  setarch  setmode

disasm>
```

To list all the supported architectures just go to the desired mode and use 'lsarchs'.

```C
asm> lsarchs
mips64, sparc64, sparc, arm_t, x64, x16, arm64, hexagon, systemz, mips32, ppc64, x86, arm, ppc32
asm> lsmodes
asm, disasm
asm> setmode disasm
Default Disassembler architecture is x86 (32 bits)
disasm> lsarchs
mips64, x16, arm64, mips32, arm_t, x86, arm, x64
disasm> 
```

### TODO

* ~~Create Python package~~
* Read input from files
* Set a proper base address for 64 bits architectures

#### Python Package Index

* https://pypi.python.org/pypi/kcshell
