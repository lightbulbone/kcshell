# kcshell

### What is it:

Simple Python3 based interactive assembly/disassembly shell for various architectures powered by [Keystone](http://www.keystone-engine.org/)/[Capstone](http://www.capstone-engine.org/).

I simply got tired of using [metasm_shell](https://github.com/rapid7/metasploit-framework/blob/master/tools/exploit/metasm_shell.rb) and [nasm_shell](https://github.com/rapid7/metasploit-framework/blob/master/tools/exploit/nasm_shell.rb) to assemble and disassemble code. [Keystone](https://github.com/keystone-engine/keystone) and [Capstone](https://github.com/aquynh/capstone) are awesome and... I like Python.

## Dependencies

* Keystone python binding: http://www.keystone-engine.org
* Capstone python binding: http://www.capstone-engine.org

## Usage

```C
$ python3 main.py 
-=[ kcshell v0.0.1b ]=-
Default Assembler architecture is x86 (32 bits)
asm> jmp esp
"\xff\xe4"
asm> ?

Documented commands (type help <topic>):
========================================
EOF  exit  help  lsarchs  lsmodes  quit  setarch  setmode

asm> help setarch
Set Assembler architecture. To list available options type 'lsarchs'.
asm> lsarchs
x16, systemz, sparc64, mips64, hexagon, ppc32, x64, arm_t, arm64, ppc64, sparc, arm, x86, mips32
asm> setarch x64
Assembler architecture is now x64
asm> inc rax
"\x48\xff\xc0"
asm> help setmode
Sets 'kcshell' operational mode. For available options run 'lsmodes'.
asm> lsmodes
asm, disasm
asm> setmode disasm
Default Disassembler architecture is x86 (32 bits)
disasm> \xff\xe4
0x00400000:	jmp	esp
disasm> ?

Documented commands (type help <topic>):
========================================
EOF  exit  help  lsarchs  lsmodes  quit  setarch  setmode

disasm> lsarchs
x16, arm, x86, mips32, mips64, x64, arm_t, arm64
disasm> setarch x64
Disassembler architecture is now x64
disasm> \x48\xff\xc0
0x00400000:	inc	rax
disasm> 
```

### TODO

* Create Python package
* Read input from files
* Set a proper base address for 64 bits architectures

