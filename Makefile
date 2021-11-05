SHELL:=/bin/bash

all:
	@echo "choose explicit target = type 'make ' and press TAB"

S=scripts
I=data
O=out


# ===== MAIN STUFF 

SCRIPT=$S/deduphash.py
deduphash:
	cat $I/test.txt | python3 $(SCRIPT) > $O/test.txt

