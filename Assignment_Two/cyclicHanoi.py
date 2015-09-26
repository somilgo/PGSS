#Figure out whether relationship between start and stop peg is normal or reverse
def towers(n_disks, start, stop, other):
	picker = stop - start
	if picker == 1 or picker == -2:
		normal(n_disks, start, stop, other)
	else:
		reverse(n_disks, start, stop, other)

#Move tower in reverse
def reverse(n_disks, start, stop, other):
	if n_disks >= 1:
		reverse(n_disks-1, start, stop, other)
		moveDisk(start, start+1)
		normal(n_disks-1, stop, start, other)
		moveDisk(start+1, start+2)
		reverse(n_disks-1, start, stop, other)

#Move tower in normal direction
def normal(n_disks, start, stop, other):
	if n_disks >= 1:
		reverse(n_disks-1, start, other, stop)
		moveDisk(start, start+1)
		reverse(n_disks-1, other, stop, start)

#Move disk from one tower to another
def moveDisk(tower1,tower2):
	global count
	count += 1
	#Corrects for towers that go beyond the third tower
	if tower1 > 3:
		tower1 = tower1 % 3
	if tower2 > 3:
		tower2 = tower2 % 3
	print "Move {0}: Move from Tower {1} to Tower {2}".format(count, tower1, tower2)

count = 0 #Move count
#towers(number of disks, start tower #, stop tower #, thru tower #)
towers(3,1,3,2)