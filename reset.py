#!/usr/bin/python3
from applib import read_ini, reset
reset(read_ini('left'), 6)
reset(read_ini('right'), 6)
reset(read_ini('hand'), 7)
