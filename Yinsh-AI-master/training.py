# python3
# generalising code for (5,5,5) ,(6,6,5) ,(6,6,6)
from __future__ import print_function
import sys
# import math
import random


my_player_no=-1
opponent_player=-1
BOARD_SIZE=-1
time_limit=-1
RUN_SIZE=-1
BOARD=[]
idxToHex5=[
	[ ( -1, -1 ), ( -1, -1 ), ( -1, -1 ), ( -1, -1 ), ( 5, 29 ), ( -1, -1 ), ( 5, 1 ), ( -1, -1 ), ( -1, -1 ),( -1, -1 ), ( -1, -1 ) ],
	[ ( -1, -1 ), ( -1, -1 ), ( -1, -1 ), ( 5, 28 ), ( -1, -1 ), ( 4, 0 ), ( -1, -1 ), ( 5, 2 ), ( -1, -1 ),( -1, -1 ), ( -1, -1 ) ],
	[ ( -1, -1 ), ( -1, -1 ), ( 5, 27 ), ( -1, -1 ), ( 4, 23 ), ( -1, -1 ), ( 4, 1 ), ( -1, -1 ), ( 5, 3 ),	( -1, -1 ), ( -1, -1 ) ],
	[ ( -1, -1 ), ( 5, 26 ), ( -1, -1 ), ( 4, 22 ), ( -1, -1 ), ( 3, 0 ), ( -1, -1 ), ( 4, 2 ), ( -1, -1 ),	( 5, 4 ), ( -1, -1 ) ],
	[ ( -1, -1 ), ( -1, -1 ), ( 4, 21 ), ( -1, -1 ), ( 3, 17 ), ( -1, -1 ), ( 3, 1 ), ( -1, -1 ), ( 4, 3 ),( -1, -1 ), ( -1, -1 ) ],
	[ ( -1, -1 ), ( 4, 20 ), ( -1, -1 ), ( 3, 16 ), ( -1, -1 ), ( 2, 0 ), ( -1, -1 ), ( 3, 2 ), ( -1, -1 ),( 4, 4 ), ( -1, -1 ) ],
	[ ( 5, 24 ), ( -1, -1 ), ( 3, 15 ), ( -1, -1 ), ( 2, 11 ), ( -1, -1 ), ( 2, 1 ), ( -1, -1 ), ( 3, 3 ),( -1, -1 ), ( 5, 6 ) ],
	[ ( -1, -1 ), ( 4, 19 ), ( -1, -1 ), ( 2, 10 ), ( -1, -1 ), ( 1, 0 ), ( -1, -1 ), ( 2, 2 ), ( -1, -1 ),( 4, 5 ), ( -1, -1 ) ],
	[ ( 5, 23 ), ( -1, -1 ), ( 3, 14 ), ( -1, -1 ), ( 1, 5 ), ( -1, -1 ), ( 1, 1 ), ( -1, -1 ), ( 3, 4 ),( -1, -1 ), ( 5, 7 ) ],
	[ ( -1, -1 ), ( 4, 18 ), ( -1, -1 ), ( 2, 9 ), ( -1, -1 ), ( 0, 0 ), ( -1, -1 ), ( 2, 3 ), ( -1, -1 ),( 4, 6 ), ( -1, -1 ) ],
	[ ( 5, 22 ), ( -1, -1 ), ( 3, 13 ), ( -1, -1 ), ( 1, 4 ), ( -1, -1 ), ( 1, 2 ), ( -1, -1 ), ( 3, 5 ),(-1, -1 ), ( 5, 8 ) ],
	[ ( -1, -1 ), ( 4, 17 ), ( -1, -1 ), ( 2, 8 ), ( -1, -1 ), ( 1, 3 ), ( -1, -1 ), ( 2, 4 ), ( -1, -1 ),( 4, 7 ), ( -1, -1 ) ],
	[ ( 5, 21 ), ( -1, -1 ), ( 3, 12 ), ( -1, -1 ), ( 2, 7 ), ( -1, -1 ), ( 2, 5 ), ( -1, -1 ), ( 3, 6 ),( -1, -1 ), ( 5, 9 ) ],
	[ ( -1, -1 ), ( 4, 16 ), ( -1, -1 ), ( 3, 11 ), ( -1, -1 ), ( 2, 6 ), ( -1, -1 ), ( 3, 7 ), ( -1, -1 ),( 4, 8 ), ( -1, -1 ) ],
	[ ( -1, -1 ), ( -1, -1 ), ( 4, 15 ), ( -1, -1 ), ( 3, 10 ), ( -1, -1 ), ( 3, 8 ), ( -1, -1 ), ( 4, 9 ),( -1, -1 ), ( -1, -1 ) ],
	[ ( -1, -1 ), ( 5, 19 ), ( -1, -1 ), ( 4, 14 ), ( -1, -1 ), ( 3, 9 ), ( -1, -1 ), ( 4, 10 ), ( -1, -1 ),( 5, 11 ), ( -1, -1 ) ],
	[ ( -1, -1 ), ( -1, -1 ), ( 5, 18 ), ( -1, -1 ), ( 4, 13 ), ( -1, -1 ), ( 4, 11 ), ( -1, -1 ), ( 5, 12 ),( -1, -1 ), ( -1, -1 ) ],
	[ ( -1, -1 ), ( -1, -1 ), ( -1, -1 ), ( 5, 17 ), ( -1, -1 ), ( 4, 12 ), ( -1, -1 ), ( 5, 13 ), ( -1, -1 ),( -1, -1 ), ( -1, -1 ) ],
	[ ( -1, -1 ), ( -1, -1 ), ( -1, -1 ), ( -1, -1 ), ( 5, 16 ), ( -1, -1 ), ( 5, 14 ), ( -1, -1 ), ( -1, -1 ),( -1, -1 ), ( -1, -1 ) ]
]

idxToHex6=[[(-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (6, 35), (-1, -1), (6, 1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)],
 [(-1, -1), (-1, -1), (-1, -1), (-1, -1), (6, 34), (-1, -1), (5, 0), (-1, -1), (6, 2), (-1, -1), (-1, -1), (-1, -1), (-1, -1)],
 [(-1, -1), (-1, -1), (-1, -1), (6, 33), (-1, -1), (5, 29), (-1, -1), (5, 1), (-1, -1), (6, 3), (-1, -1), (-1, -1), (-1, -1)], 
 [(-1, -1), (-1, -1), (6, 32), (-1, -1), (5, 28), (-1, -1), (4, 0), (-1, -1), (5, 2), (-1, -1), (6, 4), (-1, -1), (-1, -1)], 
 [(-1, -1), (6, 31), (-1, -1), (5, 27), (-1, -1), (4, 23), (-1, -1), (4, 1), (-1, -1), (5, 3), (-1, -1), (6, 5), (-1, -1)], 
 [(-1, -1), (-1, -1), (5, 26), (-1, -1), (4, 22), (-1, -1), (3, 0), (-1, -1), (4, 2), (-1, -1), (5, 4), (-1, -1), (-1, -1)], 
 [(-1, -1), (5, 25), (-1, -1), (4, 21), (-1, -1), (3, 17), (-1, -1), (3, 1), (-1, -1), (4, 3), (-1, -1), (5, 5), (-1, -1)], 
 [(6, 29), (-1, -1), (4, 20), (-1, -1), (3, 16), (-1, -1), (2, 0), (-1, -1), (3, 2), (-1, -1), (4, 4), (-1, -1), (6, 7)], 
 [(-1, -1), (5, 24), (-1, -1), (3, 15), (-1, -1), (2, 11), (-1, -1), (2, 1), (-1, -1), (3, 3), (-1, -1), (5, 6), (-1, -1)], 
 [(6, 28), (-1, -1), (4, 19), (-1, -1), (2, 10), (-1, -1), (1, 0), (-1, -1), (2, 2), (-1, -1), (4, 5), (-1, -1), (6, 8)], 
 [(-1, -1), (5, 23), (-1, -1), (3, 14), (-1, -1), (1, 5), (-1, -1), (1, 1), (-1, -1), (3, 4), (-1, -1), (5, 7), (-1, -1)], 
 [(6, 27), (-1, -1), (4, 18), (-1, -1), (2, 9), (-1, -1), (0, 0), (-1, -1), (2, 3), (-1, -1), (4, 6), (-1, -1), (6, 9)], 
 [(-1, -1), (5, 22), (-1, -1), (3, 13), (-1, -1), (1, 4), (-1, -1), (1, 2), (-1, -1), (3, 5), (-1, -1), (5, 8), (-1, -1)], 
 [(6, 26), (-1, -1), (4, 17), (-1, -1), (2, 8), (-1, -1), (1, 3), (-1, -1), (2, 4), (-1, -1), (4, 7), (-1, -1), (6, 10)], 
 [(-1, -1), (5, 21), (-1, -1), (3, 12), (-1, -1), (2, 7), (-1, -1), (2, 5), (-1, -1), (3, 6), (-1, -1), (5, 9), (-1, -1)],
 [(6, 25), (-1, -1), (4, 16), (-1, -1), (3, 11), (-1, -1), (2, 6), (-1, -1), (3, 7), (-1, -1), (4, 8), (-1, -1), (6, 11)],
 [(-1, -1), (5, 20), (-1, -1), (4, 15), (-1, -1), (3, 10), (-1, -1), (3, 8), (-1, -1), (4, 9), (-1, -1), (5, 10), (-1, -1)],
 [(-1, -1), (-1, -1), (5, 19), (-1, -1), (4, 14), (-1, -1), (3, 9), (-1, -1), (4, 10), (-1, -1), (5, 11), (-1, -1), (-1, -1)], 
 [(-1, -1), (6, 23), (-1, -1), (5, 18), (-1, -1), (4, 13), (-1, -1), (4, 11), (-1, -1), (5, 12), (-1, -1), (6, 13), (-1, -1)],
 [(-1, -1), (-1, -1), (6, 22), (-1, -1), (5, 17), (-1, -1), (4, 12), (-1, -1), (5, 13), (-1, -1), (6, 14), (-1, -1), (-1, -1)],
 [(-1, -1), (-1, -1), (-1, -1), (6, 21), (-1, -1), (5, 16), (-1, -1), (5, 14), (-1, -1), (6, 15), (-1, -1), (-1, -1), (-1, -1)],
 [(-1, -1), (-1, -1), (-1, -1), (-1, -1), (6, 20), (-1, -1), (5, 15), (-1, -1), (6, 16), (-1, -1), (-1, -1), (-1, -1), (-1, -1)],
 [(-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (6, 19), (-1, -1), (6, 17), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)]
]


def getindex(board_size,hex_no,pos):
	Ci,Cj = 2*board_size - 1, board_size
	if hex_no==0 and pos==0:
		return(Ci,Cj)
	if pos<0 or pos>6*hex_no-1:
		return((-1,-1))
	elif hex_no==board_size and pos%hex_no==0:
		return(-1,-1)
	v=pos//hex_no
	i,j=-1,-1
	if v==0:
		i,j=Ci -2 *hex_no+pos,Cj+pos
	elif v==1:
		i,j=Ci -hex_no+2*(pos%hex_no),Cj +hex_no
	elif v==2:
		i,j=Ci +hex_no+(pos%hex_no),Cj+hex_no- pos%hex_no
	elif v==3:
		i,j=Ci+2*hex_no-pos%hex_no,Cj-pos%hex_no
	elif v==4:
		i,j=Ci +hex_no-2*(pos%hex_no),Cj-hex_no
	elif v==5:
		i,j=Ci -hex_no-pos%hex_no,Cj -hex_no+pos%hex_no
	return((i,j))

def initial_config(board_size):
	Xdim, Ydim = 4*board_size - 1, 2*board_size + 1
	# if board_size==6:
	# 	Xdim=23
	# 	Ydim=13
	# else:
	# 	Xdim=19
	# 	Ydim=11
	for i in range(0,Xdim):
		l = ["X"]*Ydim
		# l=[]
		# for j in range(0,Ydim):
		# 	l.append("X")
		BOARD.append(l)
	for h in range(0,board_size+1):
		for p in range(0,6*h):
			i,j=getindex(board_size,h,p)
			if (h != board_size and p%h!= 0 or (i != -1 and j != -1)):
				BOARD[i][j] = "O"
	if board_size==6:
		BOARD[11][6]="O"
	else:
		BOARD[9][5]="O"

def showboard(gboard):
	for i in range(0,len(gboard)):
		for j in range(0,len(gboard[0])):
			if gboard[i][j]=="X":
				sys.stderr.write(" ")
				# print(" ",file=sys.stderr),
			else:
				# print(gboard[i][j]+"",file=sys.stderr),
				sys.stderr.write(gboard[i][j])
		sys.stderr.write("\n")
		# print("\n",file=sys.stderr),
				
def flipDisc(gboard,hex_no1, pos1, hex_no2,pos2):
	start=getindex(BOARD_SIZE,hex_no1,pos1)
	end=getindex(BOARD_SIZE,hex_no2,pos2)
	si=-1
	sj=-1
	ei=-1
	ej=-1
	if(start[0] + start[1] == end[0] + end[1]):
		if (start[0] > end[0]):
			si = start[0]
			sj = start[1]
			ei = end[0]
			ej = end[1]
		else: 
			ei = start[0]
			ej = start[1]
			si = end[0]
			sj = end[1]
		si-=1
		sj+=1
		ei+=1
		ej-=1
		while si>=ei:
			if (gboard[si][sj]==("r")):
				gboard[si][sj] = "b"
			elif (gboard[si][sj]==("b")):
				gboard[si][sj] = "r"
			si-=1
			sj+=1
	elif(start[0] - start[1] == end[0] - end[1]):
		if (start[0] < end[0]):
			si = start[0]
			sj = start[1]
			ei = end[0]
			ej = end[1]
		else: 
			ei = start[0]
			ej = start[1]
			si = end[0]
			sj = end[1]
		si+=1
		sj+=1
		ei-=1
		ej-=1
		while si <= ei:
			if (gboard[si][sj]==("r")):
				gboard[si][sj] = "b";
			elif (gboard[si][sj]==("b")):
				gboard[si][sj] = "r"
			si+=1
			sj+=1
	elif(start[1] == end[1]):
		if (start[0] < end[0]):
			si = start[0]
			sj = start[1]
			ei = end[0]
			ej = end[1]
		else:
			ei = start[0]
			ej = start[1]
			si = end[0]
			sj = end[1]
		si += 2
		ei -= 2
		while si<=ei:
			if (gboard[si][sj]==("r")):
				gboard[si][sj] = "b"
			elif (gboard[si][sj]==("b")):
				gboard[si][sj] = "r"
			si+=2
	return


def placeRing(gboard,player_no,hex_no,pos):
	board_size=BOARD_SIZE
	x, y = getindex(board_size,hex_no, pos);
	pieceToPlace = ["R", "B"][player_no - 1]
	gboard[x][y] = pieceToPlace
	# if (player_no == 1):
	# 	gboard[index[0]][index[1]] = "R"
 # 	else:
	# 	gboard[index[0]][index[1]] = "B"
	

def moveRing(gboard,player_no,shex,spos,fhex,fpos):
	si=-1
	sj=-1
	fi=-1
	fj=-1
	board_size=-1
	if len(gboard)==23:
		board_size=6
	else:
		board_size=5
	index=getindex(board_size,shex,spos)
	si = index[0]
	sj = index[1]
	index = getindex(board_size,fhex, fpos);
	fi = index[0]
	fj = index[1]
	if (player_no == 1):
		gboard[si][sj] = "r";
		gboard[fi][fj] = "R";
		flipDisc(gboard, shex, spos, fhex, fpos);
	elif (player_no == 2):
		gboard[si][sj] = "b";
		gboard[fi][fj] = "B";
		flipDisc(gboard, shex, spos, fhex, fpos);
	return

def removeRing(gboard,player_no,hex_no,pos):
	board_size=BOARD_SIZE
	index=getindex(board_size,hex_no,pos)
	if (gboard[index[0]][index[1]]==("R") and player_no == 1):
		gboard[index[0]][index[1]] = "O"
		return (True)
	elif(gboard[index[0]][index[1]]==("B") and player_no == 2):
		gboard[index[0]][index[1]] = "O"
		return (True)
	return (False)


def removeRow(gboard,shex,spos,fhex,fpos):
	board_size=-1
	if len(gboard)==23:
		board_size=6
	else:
		board_size=5
	# RUN_SIZE=??
	index=getindex(board_size,shex,spos)
	si=index[0]
	sj=index[1]
	index=getindex(board_size,fhex,fpos)
	fi=index[0]
	fj=index[1]
	i=-1
	j=-1
	if si+sj==fi+fj:
		if (si > fi):
			i = si
			j = sj
		else:
			i = fi
			j = fj
		for k in range(0,RUN_SIZE):
			gboard[i][j]="O"
			i-=1
			j+=1
	elif si-sj==fi-fj:
		if(si<fi):
			i = si
			j = sj
		else:
			i=fi
			j=fj
		for k in range(0,RUN_SIZE):
			gboard[i][j]="O"
			i+=1
			j+=1
	elif(sj==fj):
		j=sj
		if si<fi:
			i=si
		else:
			i=fi
		for k in range(0,RUN_SIZE):
			gboard[i][j]="O"
			i+=2
	return

# return hex,pos of the ring to be removed
def removingRingGreedly(curr_board,player_no):
	hex_pos=(-1,-1)
	board_size=BOARD_SIZE
	lookForRing=[]
	if player_no==1:
		lookForRing="R"
	elif player_no==2:
		lookForRing="B"
	ring_arr=getPositionOfRing(player_no,curr_board)
	util=0
	i=0
	for p in ring_arr:
		x,y=getindex(board_size,p[0],p[1])
		curr_board[x][y]="O"
		u=Utility(curr_board)
		if i==0:
			util=u
			hex_pos=p
		if u>util:
			util=u
			hex_pos=p
		curr_board[x][y]=lookForRing
	return(hex_pos)


def getruns(gboard,player_no):
	runs=[]
	board_size=BOARD_SIZE
	if board_size==6:
		# vertical
		runs+=DiscRemovalPossible(gboard,player_no,7,0,15,0)
		runs+=DiscRemovalPossible(gboard,player_no,4,1,18,1)
		runs+=DiscRemovalPossible(gboard,player_no,3,2,19,2)
		runs+=DiscRemovalPossible(gboard,player_no,2,3,20,3)

		runs+=DiscRemovalPossible(gboard,player_no,1,4,21,4)
		runs+=DiscRemovalPossible(gboard,player_no,0,5,22,5)
		runs+=DiscRemovalPossible(gboard,player_no,1,6,21,6)
		runs+=DiscRemovalPossible(gboard,player_no,0,7,22,7)
		
		runs+=DiscRemovalPossible(gboard,player_no,1,8,21,8)
		runs+=DiscRemovalPossible(gboard,player_no,2,9,20,9)
		runs+=DiscRemovalPossible(gboard,player_no,3,10,19,10)
		runs+=DiscRemovalPossible(gboard,player_no,4,11,18,11)
		runs+=DiscRemovalPossible(gboard,player_no,7,12,15,12)
		
		# right runs
		runs+=DiscRemovalPossible(gboard,player_no,0,7,4,11)
		runs+=DiscRemovalPossible(gboard,player_no,0,5,7,12)
		runs+=DiscRemovalPossible(gboard,player_no,1,4,9,12)
		runs+=DiscRemovalPossible(gboard,player_no,2,3,11,12)

		runs+=DiscRemovalPossible(gboard,player_no,3,2,13,12)
		runs+=DiscRemovalPossible(gboard,player_no,4,1,15,12)
		runs+=DiscRemovalPossible(gboard,player_no,6,1,16,11)
		runs+=DiscRemovalPossible(gboard,player_no,7,0,18,11)
		
		runs+=DiscRemovalPossible(gboard,player_no,9,0,19,10)
		runs+=DiscRemovalPossible(gboard,player_no,11,0,20,9)
		runs+=DiscRemovalPossible(gboard,player_no,13,0,21,8)
		runs+=DiscRemovalPossible(gboard,player_no,15,0,22,7)
		runs+=DiscRemovalPossible(gboard,player_no,18,1,22,5)

		# left runs
		runs+=DiscRemovalPossible(gboard,player_no,4,1,0,5)
		runs+=DiscRemovalPossible(gboard,player_no,7,0,0,7)
		runs+=DiscRemovalPossible(gboard,player_no,9,0,1,8)
		runs+=DiscRemovalPossible(gboard,player_no,11,0,2,9)

		runs+=DiscRemovalPossible(gboard,player_no,13,0,3,10)
		runs+=DiscRemovalPossible(gboard,player_no,15,0,4,11)
		runs+=DiscRemovalPossible(gboard,player_no,16,1,6,11)
		runs+=DiscRemovalPossible(gboard,player_no,18,1,7,12)

		runs+=DiscRemovalPossible(gboard,player_no,19,2,9,12)
		runs+=DiscRemovalPossible(gboard,player_no,20,3,11,12)
		runs+=DiscRemovalPossible(gboard,player_no,21,4,13,12)
		runs+=DiscRemovalPossible(gboard,player_no,22,5,15,12)
		runs+=DiscRemovalPossible(gboard,player_no,22,7,18,11)

	elif board_size==5:
		# vertical
		runs +=(DiscRemovalPossible(gboard, player_no, 3, 1, 15, 1)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 2, 2, 16, 2)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 1, 3, 17, 3)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 0, 4, 18, 4)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 1, 5, 17, 5)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 0, 6, 18, 6)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 1, 7, 17, 7)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 2, 8, 16, 8)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 3, 9, 15, 9)) 

		# rightRun
		runs +=(DiscRemovalPossible(gboard, player_no, 0, 4, 6, 10)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 1, 3, 8, 10)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 2, 2, 10, 10)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 3, 1, 12, 10)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 5, 1, 13, 9)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 6, 0, 15, 9)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 8, 0, 16, 8)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 10, 0, 17, 7)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 12, 0, 18, 6)) 

		# left Runs
		runs +=(DiscRemovalPossible(gboard, player_no, 6, 0, 0, 6)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 8, 0, 1, 7)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 10, 0, 2, 8)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 12, 0, 3, 9)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 13, 1, 5, 9)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 15, 1, 6, 10)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 16, 2, 8, 10)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 17, 3, 10, 10)) 
		runs +=(DiscRemovalPossible(gboard, player_no, 18, 4, 12, 10)) 

	return runs
# list of list eg.[[s1,e1,s2,e2],[..],..]
def DiscRemovalPossible(gboard,player_no,si,sj,fi,fj):
	board_size=BOARD_SIZE
	lookForMarker=""
	if player_no==1:
		lookForMarker="r"
	elif player_no==2:
		lookForMarker="b"
	idcies_for_removal_in_this_row=[]
	if si+sj==fi+fj:
		i=-1
		j=-1
		ii=-1
		jj=-1
		if(si>fi):
			i=si
			j=sj
			ii=fi
			jj=fj
		else:
			ii=si
			jj=sj
			i=fi
			j=fj
		count=0
		initial_index=(-1,-1)
		final_index=(-1,-1)
		sx=i
		sy=j
		while sx>=ii:
			if gboard[sx][sy]==lookForMarker:
				if count==0:
					initial_index=sx,sy
				count+=1
				if count==RUN_SIZE:
					index=[-1,-1,-1,-1]
					final_index=sx,sy
					index[0]=initial_index[0]
					index[1]=initial_index[1]
					index[2]=final_index[0]
					index[3]=final_index[1]
					idcies_for_removal_in_this_row.append(index)
					sx = initial_index[0] - 1
					sy = initial_index[1] + 1
					count=0
			else:
				count=0
			sx-=1
			sy+=1
	elif si-sj==fi-fj:
		i=-1
		j=-1
		ii=-1
		jj=-1
		if si<fi:
			i=si
			j=sj
			ii=fi
			jj=fj
		else:
			ii=si
			jj=sj
			i=fi
			j=fj
		count=0
		initial_index=(-1,-1)
		final_index=(-1,-1)
		sx=i
		sy=j
		while sx<=ii:
			if gboard[sx][sy]==lookForMarker:
				if count==0:
					initial_index=sx,sy
				count+=1
				if count==RUN_SIZE:
					index=[-1,-1,-1,-1]
					final_index=sx,sy
					index[0]=initial_index[0]
					index[1]=initial_index[1]
					index[2]=final_index[0]
					index[3]=final_index[1]
					idcies_for_removal_in_this_row.append(index)
					sx = initial_index[0] + 1
					sy = initial_index[1] + 1
					count=0
			else:
				count=0
			sx+=1
			sy+=1
	elif fj==sj:
		i=-1
		ii=-1
		if si<fi:
			i=si
			ii=fi
		else:
			i=fi
			ii=si
		count=0
		initial_index=(-1,-1)
		final_index=(-1,-1)
		sx=i
		sy=sj
		while sx<=ii:
			if gboard[sx][sy]==lookForMarker:
				if count==0:
					initial_index=sx,sy
				count+=1
				if count==RUN_SIZE:
					index=[-1,-1,-1,-1]
					final_index=sx,sy
					index[0]=initial_index[0]
					index[1]=initial_index[1]
					index[2]=final_index[0]
					index[3]=final_index[1]
					idcies_for_removal_in_this_row.append(index)
					sx = initial_index[0] + 2
					count=0
			else:
				count=0
			sx+=2

	return idcies_for_removal_in_this_row
	



def idxToHex(board_size,i,j):
	if board_size==5:
		return(idxToHex5[i][j][0],idxToHex5[i][j][1])
	else:
		return(idxToHex6[i][j][0],idxToHex6[i][j][1])

def getCopyOfboard(gboard):
	copyBoard=[]
	for i in range(0,len(gboard)):
		l=[]
		for j in range(0,len(gboard[0])):
			l.append(gboard[i][j])
		copyBoard.append(l)
	return(copyBoard)

# list of tuple of (hex,pos)
def getPositionOfRing(player_no,gboard):
	positions=[]
	board_size=BOARD_SIZE
	for i in range(0,len(gboard)):
		for j in range(0,len(gboard[0])):
			if player_no==1:
				if gboard[i][j]=="R":
					positions.append(idxToHex(board_size,i,j))
			elif player_no==2:
				if gboard[i][j]=="B":
					positions.append(idxToHex(board_size,i,j))
	return(positions)

def getValidPosOfTheRing(gboard,hex_no,pos):
	validPos=[]
	board_size=BOARD_SIZE
	idx=getindex(board_size,hex_no,pos)
	# Direction1
	i=idx[0]
	j=idx[1]
	overDisc=False
	i-=2
	while i>=0:
		if gboard[i][j]=="X":
			break
		if gboard[i][j]=="O" and overDisc==False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc==True:
			validPos.append(idxToHex(board_size,i,j))
			break
		if gboard[i][j]=="r" or gboard[i][j]=="b":
			overDisc=True
		if gboard[i][j]=="R" or gboard[i][j]=="B":
			break
		i-=2
	# Direction2
	i=idx[0]
	j=idx[1]
	overDisc=False
	i-=1
	j+=1
	while (i>=0 and j<11 and board_size==5) or (i>=0 and j<13 and board_size==6) :
		if gboard[i][j]=="X":
			break
		if gboard[i][j]=="O" and overDisc==False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc==True:
			validPos.append(idxToHex(board_size,i,j))
			break
		if gboard[i][j]=="r" or gboard[i][j]=="b":
			overDisc=True
		if gboard[i][j]=="R" or gboard[i][j]=="B":
			break
		i-=1
		j+=1

	# Direction3
	i = idx[0]
	j = idx[1]
	overDisc = False
	i+=1
	j+=1
	while((board_size==5 and i<19 and j<11) or (board_size==6 and i<23 and j<13)):
		if gboard[i][j]=="X":
			break
		if gboard[i][j]=="O" and overDisc==False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc==True:
			validPos.append(idxToHex(board_size,i,j))
			break
		if gboard[i][j]=="r" or gboard[i][j]=="b":
			overDisc=True
		if gboard[i][j]=="R" or gboard[i][j]=="B":
			break
		i+=1
		j+=1
	
	# Direction4
	i = idx[0]
	j = idx[1]
	overDisc = False
	i+=2
	while((board_size==5 and i<19) or (board_size==6 and i<23)):
		if gboard[i][j]=="X":
			break
		if gboard[i][j]=="O" and overDisc==False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc==True:
			validPos.append(idxToHex(board_size,i,j))
			break
		if gboard[i][j]=="r" or gboard[i][j]=="b":
			overDisc=True
		if gboard[i][j]=="R" or gboard[i][j]=="B":
			break
		i+=2

	# Direction5
	i = idx[0]
	j = idx[1]
	overDisc = False
	i+=1
	j-=1
	while((board_size==5 and i<19 and j>=0) or (board_size==6 and i<23 and j>=0) ):
		if gboard[i][j]=="X":
			break
		if gboard[i][j]=="O" and overDisc==False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc==True:
			validPos.append(idxToHex(board_size,i,j))
			break
		if gboard[i][j]=="r" or gboard[i][j]=="b":
			overDisc=True
		if gboard[i][j]=="R" or gboard[i][j]=="B":
			break
		i+=1
		j-=1

	# Direction6
	i = idx[0]
	j = idx[1]
	overDisc = False
	i-=1
	j-=1
	while(i>=0 and j>=0):
		if gboard[i][j]=="X":
			break
		if gboard[i][j]=="O" and overDisc==False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc==True:
			validPos.append(idxToHex(board_size,i,j))
			break
		if gboard[i][j]=="r" or gboard[i][j]=="b":
			overDisc=True
		if gboard[i][j]=="R" or gboard[i][j]=="B":
			break
		i-=1
		j-=1

	return(validPos)
	

def AllSingleMoves(gboard,player_no,moved,moves):
	runs=getruns(gboard,player_no)
	allmoves=[] #list of board,string to get to that move
	if(len(runs)!=0 and len(getPositionOfRing(player_no,gboard))>=BOARD_SIZE-2 ):
		for run in runs:
			temp_board=getCopyOfboard(gboard)
			tmp=moves
			idx=[-1,-1,-1,-1]
			idx[0],idx[1]=idxToHex(BOARD_SIZE,run[0],run[1])
			idx[2],idx[3]=idxToHex(BOARD_SIZE,run[2],run[3])

			removeRow(temp_board,idx[0],idx[1],idx[2],idx[3])
			hex_pos=removingRingGreedly(temp_board,player_no)
			temp_board[getindex(BOARD_SIZE,hex_pos[0], hex_pos[1])[0]][getindex(BOARD_SIZE,hex_pos[0], hex_pos[1])[1]]="O"
			tmp += " RS " + str(idx[0]) + " " + str(idx[1]) + " RE " + str(idx[2]) + " " + str(idx[3]) + " X " + str(hex_pos[0]) + " "+ str(hex_pos[1])

			allmoves+=AllSingleMoves(temp_board,player_no,moved,tmp)
	elif(moved==False and len(getPositionOfRing(player_no,gboard))>=BOARD_SIZE-2):
		pos_of_Rings=getPositionOfRing(player_no,gboard)
		neigh_states=[]
		for posR in pos_of_Rings:
			validPos=getValidPosOfTheRing(gboard,posR[0],posR[1])
			for vPos in validPos:
				s=""
				temp_board=getCopyOfboard(gboard)
				moveRing(temp_board,player_no,posR[0],posR[1],vPos[0],vPos[1])
				s="S "+ str(posR[0])+" "+str(posR[1])+" "+"M "+str(vPos[0])+" "+str(vPos[1])
				allmoves+=AllSingleMoves(temp_board,player_no,True,s)
	else:
		temp=(getCopyOfboard(gboard),moves) #pair of board,string
		# print("temp",file=sys.stderr)
		# print(temp,file=sys.stderr)
		allmoves+=[temp]
		# print(allmoves,file=sys.stderr)
	# print("damit",file=sys.stderr)
	# print(allmoves[0],file=sys.stderr)
	return(allmoves)

def opening(board_size):
	while True:
		hexagon=random.randint(0,3)
		position=0
		if hexagon!=0:
			position=random.randint(0,6*hexagon-1)
		index=getindex(board_size,hexagon,position)
		if(BOARD[index[0]][index[1]]=="O"):
                        return "P {} {}".format(hexagon, position)


def gameOver(gboard):
	count1=0
	count2=0
	count3=0
	board_size=BOARD_SIZE
	for i in range(0,len(gboard)):
		for j in range(0,len(gboard[0])):
			if gboard[i][j]=="O":
				count3+=1
			if gboard[i][j]=="R":
				count1+=1
			if gboard[i][j]=="B":
				count2+=1
	if count3==0:
		return(True)
	elif(count1>=board_size-2 and count2>=board_size-2):
		return(False)
	return True


def Gamescore(gboard):
	Rring=0
	Bring=0
	Rmarker=0
	Bmarker=0
	score=0.0
	score2=0.0
	board_size=BOARD_SIZE
	for i in range(0,len(gboard)):
		for j in range(0,len(gboard[0])):
			if gboard[i][j]=="R":
				Rring+=1
			if gboard[i][j]=="B":
				Bring+=1
			if gboard[i][j]=="r":
				Rmarker+=1
			if gboard[i][j]=="b":
				Bmarker+=1
	Rring=board_size-Rring
	Bring=board_size-Bring

	if(Rring == 3 and Bring==0):
		score = score+10
		score2 = score2 + 0	
	elif(Rring == 3 and Bring==1):
		score = score + 9
		score2 = score2+1
	elif(Rring == 3 and Bring==2):
		score = score + 8
		score2 = score2+2
	elif(Rring == 2 and Bring==0):
		score = score + 7
		score2 = score2+3
	elif(Rring == 2 and Bring==1):
		score = score + 6
		score2 = score2+ 4
	elif(Rring == 1 and Bring==0):
		score = score + 6
		score2 = score2+ 4
	elif(Rring == 2 and Bring==2):
		score = score + 5
		score2 = score2+ 5
	elif(Rring == 1 and Bring==1):
		score = score + 5
		score2 = score2+ 5
	elif(Rring ==0 and Bring==0):
		score = score + 5
		score2 = score2+ 5
	elif(Rring == 0 and Bring==1):
		score = score + 4
		score2 = score2+ 6
	elif(Rring == 1 and Bring==2):
		score = score + 4
		score2 = score2+ 6
	elif(Rring == 0 and Bring==2):
		score = score + 3
	elif(Rring == 2 and Bring==3):
		score = score + 2
		score2 = score2+ 8
	elif(Rring == 1 and Bring==3):
		score = score + 1
		score2 = score2 + 9
	elif(Rring == 0 and Bring==3):
		score = score + 0
		score2 = score2+10

	score=score+Rmarker/1000
	score2=score2+Bmarker/1000
	if my_player_no==1:
		score=score-score2
	else:
		score=score2-score
	return 10*score


	
def DiscInCol(gboard):
	return(MarkersInCol(gboard,my_player_no)-MarkersInCol(gboard,opponent_player))


def evalfunction(gboard):
	score=0.0
	score+=DiscInDiag(gboard)
	score+=DiscInCol(gboard)
	return(score)

def DiscInDiag(gboard):
	scores=[]
	for player_no in range(1,3):
		score=0.0
		if BOARD_SIZE==5:
			# rightRun
			score +=(MarkerInDiag(gboard, player_no, 0, 4, 6, 10)) 
			score +=(MarkerInDiag(gboard, player_no, 1, 3, 8, 10)) 
			score +=(MarkerInDiag(gboard, player_no, 2, 2, 10, 10)) 
			score +=(MarkerInDiag(gboard, player_no, 3, 1, 12, 10)) 
			score +=(MarkerInDiag(gboard, player_no, 5, 1, 13, 9)) 
			score +=(MarkerInDiag(gboard, player_no, 6, 0, 15, 9)) 
			score +=(MarkerInDiag(gboard, player_no, 8, 0, 16, 8)) 
			score +=(MarkerInDiag(gboard, player_no, 10, 0, 17, 7)) 
			score +=(MarkerInDiag(gboard, player_no, 12, 0, 18, 6)) 

			# left Runs
			score +=(MarkerInDiag(gboard, player_no, 6, 0, 0, 6)) 
			score +=(MarkerInDiag(gboard, player_no, 8, 0, 1, 7)) 
			score +=(MarkerInDiag(gboard, player_no, 10, 0, 2, 8)) 
			score +=(MarkerInDiag(gboard, player_no, 12, 0, 3, 9)) 
			score +=(MarkerInDiag(gboard, player_no, 13, 1, 5, 9)) 
			score +=(MarkerInDiag(gboard, player_no, 15, 1, 6, 10)) 
			score +=(MarkerInDiag(gboard, player_no, 16, 2, 8, 10)) 
			score +=(MarkerInDiag(gboard, player_no, 17, 3, 10, 10)) 
			score +=(MarkerInDiag(gboard, player_no, 18, 4, 12, 10)) 
		elif BOARD_SIZE==6:
			# right score
			score+=MarkerInDiag(gboard,player_no,0,7,4,11)
			score+=MarkerInDiag(gboard,player_no,0,5,7,12)
			score+=MarkerInDiag(gboard,player_no,1,4,9,12)
			score+=MarkerInDiag(gboard,player_no,2,3,11,12)

			score+=MarkerInDiag(gboard,player_no,3,2,13,12)
			score+=MarkerInDiag(gboard,player_no,4,1,15,12)
			score+=MarkerInDiag(gboard,player_no,6,1,16,11)
			score+=MarkerInDiag(gboard,player_no,7,0,18,11)
			
			score+=MarkerInDiag(gboard,player_no,9,0,19,10)
			score+=MarkerInDiag(gboard,player_no,11,0,20,9)
			score+=MarkerInDiag(gboard,player_no,13,0,21,8)
			score+=MarkerInDiag(gboard,player_no,15,0,22,7)
			score+=MarkerInDiag(gboard,player_no,18,1,22,5)

			# left score
			score+=MarkerInDiag(gboard,player_no,4,1,0,5)
			score+=MarkerInDiag(gboard,player_no,7,0,0,7)
			score+=MarkerInDiag(gboard,player_no,9,0,2,8)
			score+=MarkerInDiag(gboard,player_no,11,0,2,9)

			score+=MarkerInDiag(gboard,player_no,13,0,3,10)
			score+=MarkerInDiag(gboard,player_no,15,0,4,11)
			score+=MarkerInDiag(gboard,player_no,16,1,6,11)
			score+=MarkerInDiag(gboard,player_no,18,1,7,12)

			score+=MarkerInDiag(gboard,player_no,19,2,9,12)
			score+=MarkerInDiag(gboard,player_no,20,3,11,12)
			score+=MarkerInDiag(gboard,player_no,21,4,13,12)
			score+=MarkerInDiag(gboard,player_no,22,5,15,12)
			score+=MarkerInDiag(gboard,player_no,22,7,18,11)
		scores.append(score)
	if my_player_no==1:
		return(scores[0]-scores[1])
	else:
		return(scores[1]-scores[0])

def MarkersInCol(gboard,player_no):
	ver_score=0.0
	n=[0.0,0.0,0.0,0.0,0.0]
	lookForMarker=""
	if player_no==1:
		lookForMarker="r"
	else:
		lookForMarker="b"
	count=-1
	for j in range(0,len(gboard[0])):
		i=0
		while i<len(gboard):
			if gboard[i][j]!="X":
				if gboard[i][j]==lookForMarker:
					count+=1
					if(i+2<len(gboard) and gboard[i+2][j]==lookForMarker) :
						count+=1
						if(i+4<len(gboard) and gboard[i+4][j]==lookForMarker):
							count+=1
							if(i+6 <len(gboard) and gboard[i+6][j]==lookForMarker):
								count+=1
								if(i+8<len(gboard) and gboard[i+8][j]==lookForMarker):
									count+=1
									n[count]=n[count]+1
								else:
									n[count]=n[count]+1
							else:
								n[count]=n[count]+1
						else:
							n[count]=n[count]+1
					else:
						n[count]=n[count]+1
					i+=count*2
					count=-1
				i+=2
			else:
				i+=1
			count=-1	

	ver_score=10000*n[4]+1000*n[3]+100*n[2]+10*n[1]+n[0]
	return(ver_score)


def MarkerInDiag(gboard,player_no,i1,j1,i2,j2):
	lookForMarker=""
	if player_no==1:
		lookForMarker="r"
	else:
		lookForMarker="b"
	diag_score=0.0
	n=[0.0,0.0,0.0,0.0,0.0]
	count=-1
	if(i1+j1==i2+j2):
		i=i1
		j=j1
		while i2<=i and j<=j2:
			if i2<=i and j<=j2 and gboard[i][j]==lookForMarker:
				count+=1
				if(i2<=i-1 and j+1<=j2 and gboard[i-1][j+1]==lookForMarker):
					count+=1
					if(i2<=i-2 and j+2<=j2 and gboard[i-2][j+2]==lookForMarker):
						count+=1
						if(i2<=i-3 and j+3<=j2 and gboard[i-3][j+3]==lookForMarker):
							count+=1
							if(i2<=i-4 and j+4<=j2 and gboard[i-4][j+4]==lookForMarker):
								count+=1
								n[count]=n[count]+1
							else:
								n[count]=n[count]+1
						else:
							n[count]=n[count]+1
					else:
						n[count]=n[count]+1
				else:
					n[count]=n[count]+1
			if count==-1:
				i-=1
				j+=1
			else:
				i=i-count-1
				j=j+count+1
				count=-1
	elif(i1-j1==i2-j2):
		i=i1
		j=j1
		while(i<=i2 and j<=j2):
			if i<=i2 and j<=j2 and gboard[i][j]==lookForMarker:
				count+=1
				if(i+1<=i2 and j+1<=j2 and gboard[i+1][j+1]==lookForMarker):
					count+=1
					if(i+2<=i2 and j+2<=j2 and gboard[i+2][j+2]==lookForMarker):
						count+=1
						if(i+3<=i2 and j+3<=j2 and gboard[i+3][j+3]==lookForMarker):
							count+=1
							if(i+4<=i2 and j+4<=j2 and gboard[i+4][j+4]==lookForMarker):
								count+=1
								n[count]=n[count]+1
							else:
								n[count]=n[count]+1
						else:
							n[count]=n[count]+1
					else:
						n[count]=n[count]+1
				else:
					n[count]=n[count]+1
			if count==-1:
				i+=1
				j+=1
			else:
				i=i+count+1
				j=j+count+1
				count=-1


	diag_score=10000*n[4]+1000*n[3]+100*n[2]+10*n[1]+n[0]		
	return(diag_score)				

				
			


def Utility(gboard):
	util=(10**8)*Gamescore(gboard)+evalfunction(gboard)
	return(util)


returnMove=""
def MinMax(gboard,player_no,depth,alpha,beta,cutoff):
	global returnMove
	returnMove=""
	board_size=BOARD_SIZE
	runs=getruns(gboard,player_no)
	tmp=""
	while len(runs)!=0 and len(getPositionOfRing(player_no,gboard))>=board_size-2:
		idx=runs[0]
		idx[0],idx[1]=idxToHex(board_size,idx[0],idx[1])
		idx[2],idx[3]=idxToHex(board_size,idx[2],idx[3])
		removeRow(gboard,idx[0],idx[1],idx[2],idx[3])
		hex_pos=removingRingGreedly(gboard,player_no)
		gboard[getindex(board_size,hex_pos[0], hex_pos[1])[0]][getindex(board_size,hex_pos[0], hex_pos[1])[1]]="O"
		tmp+="RS " + str(idx[0]) + " " + str(idx[1]) + " RE " + str(idx[2]) + " " + str(idx[3]) + " X " + str(hex_pos[0]) + " "+ str(hex_pos[1])+" "
		runs=getruns(gboard,player_no)
	if (len(getPositionOfRing(player_no,gboard))>=board_size-2):
		# print("yo I am here",file=sys.stderr)
		AlphaBeta(gboard,player_no,depth,alpha,beta,cutoff)

	returnMove=tmp+returnMove
	return returnMove.strip()

def AlphaBeta(gboard,player_no,depth,alpha,beta,cutoff):
	global returnMove
	if(gameOver(gboard)==True or depth==cutoff):
		return(Utility(gboard))
	elif(player_no==my_player_no):
		v=-float("inf")
		neighbours=AllSingleMoves(gboard,my_player_no,False,"")
		# Order States
		for nei in neighbours:
			u=max(v,AlphaBeta(nei[0],opponent_player,depth+1,alpha,beta,cutoff))
			if u>v:
				if depth==0:
					# global variable return move
					# print("modifying print",file=sys.stderr)
					# print(nei[1],file=sys.stderr)
					returnMove=nei[1]
				v=u
			alpha=max(alpha,v)
			if beta<=alpha:
				break
		return(v)
	else:
		v=float("inf")
		neighbours=AllSingleMoves(gboard,opponent_player,False,"")
		for nei in neighbours:
			v=min(v,AlphaBeta(nei[0],my_player_no,depth+1,alpha,beta,cutoff))
			beta=min(beta,v)
			if beta<=alpha:
				break
		return v





def update_move(move,player_no):
	movesplit=move.strip().split()
	# print(move,file=sys.stderr)
	if len(movesplit)==0:
		return
	if movesplit[0]=="P":
		placeRing(BOARD,player_no,int(movesplit[1]),int(movesplit[2]))
	elif(movesplit[0]=="S"):
		moveRing(BOARD,player_no,int(movesplit[1]),int(movesplit[2]),int(movesplit[4]),int(movesplit[5]))
		remains=""
		for rem in movesplit[6:]:
			remains+=rem+" "
		remains=remains.strip()
		update_move(remains,player_no)
	elif(movesplit[0]=="RS"):
		removeRow(BOARD,int(movesplit[1]),int(movesplit[2]),int(movesplit[4]),int(movesplit[5]))
		removeRing(BOARD,player_no,int(movesplit[7]),int(movesplit[8]))
		remains=""
		for rem in movesplit[9:]:
			remains+=rem+" "
		remains=remains.strip()
		update_move(remains,player_no)

def get_move():
	if BOARD_SIZE==5:
		s=MinMax(BOARD,my_player_no,0,-float("inf"),float("inf"),2)
	else:
		s=MinMax(BOARD,my_player_no,0,-float("inf"),float("inf"),2)
	return s





move=""
data=sys.stdin.readline().strip().split()
my_player_no=int(data[0])
BOARD_SIZE=int(data[1])
time_limit=int(data[2])
RUN_SIZE=int(data[3])
gameover=False
# print(str(BOARD_SIZE) +" "+str(my_player_no)+" "+str(time_limit)+" "+str(RUN_SIZE),file=sys.stderr)
# print("Player id: {}".format(my_player_no), file=sys.stderr)
if my_player_no==2:
        opponent_player=1
else:
        opponent_player=2
initial_config(BOARD_SIZE)
# showboard(BOARD)
if my_player_no==1:
        for i in range(0,BOARD_SIZE):
                move=opening(BOARD_SIZE)
                update_move(move,1)
                sys.stdout.write(move+'\n')
                sys.stdout.flush()
                move=sys.stdin.readline()
                update_move(move,2)
        while (not gameover):
                move=get_move()
                update_move(move,1)
                # print(move+'\n')
                sys.stdout.write(move+'\n')
                sys.stdout.flush()
                move=sys.stdin.readline()
                update_move(move,2)
elif my_player_no==2:
        for i in range(0,BOARD_SIZE):
                move=sys.stdin.readline()
                update_move(move,1)
                # showboard(BOARD)
                move=opening(BOARD_SIZE)
                update_move(move,2)
                # showboard(BOARD)
                # print(move+'\n')
                sys.stdout.write(move+'\n')
                sys.stdout.flush()
        move=sys.stdin.readline()
        update_move(move,1)
        while (not gameover):
                move=get_move()
                update_move(move,2)
                # showboard(BOARD)
                # print(move+'\n')
                # print("move is "+move,file=sys.stderr)
                sys.stdout.write(move+'\n')
                sys.stdout.flush()
                move=sys.stdin.readline()
                update_move(move,1)
                # showboard(BOARD)

                

