title: ELF 32bit su architetture a 64bit
lang: it
tags: mix, linux
Category: Mix
Date: 2014-10-15
Status: draft

[http://unix.stackexchange.com/questions/13391/getting-not-found-message-when-running-a-32-bit-binary-on-a-64-bit-system/13409#13409](http://unix.stackexchange.com/questions/13391/getting-not-found-message-when-running-a-32-bit-binary-on-a-64-bit-system/13409#13409)

Prima

	:::sh
	gambuzzi@vq19:~/bin/polygen-1.0.6$ ./polygen
	-bash: ./polygen: No such file or directory


I comandi da dare

	:::sh
	sudo dpkg --add-architecture i386
	sudo apt-get update
	sudo apt-get install libc6:i386 zlib1g:i386


Dopo 

	:::sh
	gambuzzi@vq19:~/bin/polygen-1.0.6$ ./polygen
	Polygen (type 2) v1.0.6 built 20040628 - http://www.polygen.org
	Manta/Spinning Kids alias Alvise Spano' anno MMII ac insequenti fecit.
	
	usage: polygen [OPTION]... SOURCES...
	
	 SOURCE     source file(s) providing grammar definition
	
	 OPTION
	  -eof STR  use string STR as end-of-file (default: STR = "\n")
	  -help     display this help message
	  -info     alias for '-S I'
	  -l LABEL  add LABEL to initial active label environment
	  -o DEST   output to DEST file
	  -pedantic set warning level to maximum
	  -pre      output preprocessed source grammar
	  -seed N   pass unsigned integer N as random seed
	  -S SYM    use SYM as starting non-terminal symbol (default: SYM = S)
	  -t        check source grammar and output inferred global label groups
	  -v        be verbose
	  -X N      iterate generation for N times (default: N = 1)
	  -W N      set warning pedantry at level N (default: N = 1)
