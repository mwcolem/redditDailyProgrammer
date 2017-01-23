import sys, re
from collections import namedtuple

def defused():
	print "Bomb defused"

def boom():
	print "Boom"

colors = namedtuple('colors', 'start white red black orange green purple'.split())

goodCombos = colors(start='white red black orange green purple',
	white='red green orange purple',
	red='green',
	black='red black orange purple',
	orange='red black',
	green='orange white',
	purple='red black')

def defuse(wires):
	current_wire = 'start'
	for wire in wires:
		if wire in getattr(goodCombos, current_wire):
			current_wire = wire
		else:
			boom()
			return
	defused()
		

wires = sys.argv[1];

with open(wires, 'r') as target_file:
	wires = target_file.read().splitlines()
	defuse(wires)

target_file.close()	
