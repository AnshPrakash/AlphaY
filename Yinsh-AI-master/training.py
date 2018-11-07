# python3
# generalising code for (5,5,5) ,(6,6,5) ,(6,6,6)
import sys
import random

player_no=-1
board_size=-1
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
 [(6, 27), (-1, -1), (4, 18), (-1, -1), (2, 9), (-1, -1), (-1, -1), (-1, -1), (2, 3), (-1, -1), (4, 6), (-1, -1), (6, 9)], 
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
	Ci,Cj=-1,-1
	if board_size==5:
		Ci,Cj=9,5
	else:
		Ci,Cj=11,6
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
	Xdim=-1
	Ydim=-1
	if board_size==6:
		Xdim=23
		Ydim=13
	else:
		Xdim=19
		Ydim=11
	for i in range(0,Xdim):
		l=[]
		for j in range(0,Ydim):
			l.append("X")
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
				print(" "),
			else:
				print(gboard[i][j]+""),
		print("\n"),
				
def flipDisc(gboard,hex_no1, pos1, hex_no2,pos2):
	start=getindex(hex_no1,pos1)
	end=getindex(hex_no2,pos2)
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
		else 
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
			else if (gboard[si][sj]==("b")):
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
			if (givenboard[si][sj]==("r")):
				gboard[si][sj] = "b"
			elif (givenboard[si][sj]==("b")):
				gboard[si][sj] = "r"
			si+=2
	return


def placeRing(gboard,player_no,hex_no,pos):
	board_size=-1
	if len(gboard)==23:
		board_size=6
	else:
		board_size=5
	index = getindex(board_size,hex_no, pos);
	if (player_no == 1):
		gboard[index[0]][index[1]] = "R"
 	else:
		gboard[index[0]][index[1]] = "B"
	

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
		flipDiscs(gboard, shex, spos, fhex, fpos);
	elif (player_no == 2):
		gboard[si][sj] = "b";
		gboard[fi][fj] = "B";
		flipDiscs(gboard, shex, spos, fhex, fpos);
	return

def removeRing(gboard,player_no,hex_no,pos):
	board_size=-1
	if len(gboard)==23:
		board_size=6
	else:
		board_size=5
	index=getindex(board_size,hex_no,pos)
	if (gboard[index[0]][index[1]]==("R") and player_no == 1):
		gboard[index[0]][index[1]] = "O"
		return (true)
	elif(gboard[index[0]][index[1]]==("B") and player_no == 2):
		gboard[index[0]][index[1]] = "O"
		return (true)
	return (false)


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


def removingRingGreedly(curr_board,player_no):
	pass

def getrun(gboard,player_no):
	# RUN_SIZE
	pass

def FiveDiscRemovalPossible(gboard,player_no,si,sj,fi,fj):
	pass

def SixDiscRemovalPossible(gboard,player_no,si,sj,fi,fj):
	pass

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

def getPositionOfRing(player_no,gboard):
	positions=[]
	board_size=-1
	if len(gboard)==23:
		board_size=6
	else:
		board_size=5
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
	board_size=-1
	if len(gboard)==23;
		board_size=6
	else:
		board_size=5
	idx=getindex(board_size,hex_no,pos)
	# Direction1
	i=idx[0]
	j=idx[1]
	overDisc=False
	i-=2
	while i>=0:
		if gboard[i][j]=="X":
			break
		if gboard[i][j]=="O" and overDisc=False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc=True:
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
		if gboard[i][j]=="O" and overDisc=False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc=True:
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
		if gboard[i][j]=="O" and overDisc=False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc=True:
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
		if gboard[i][j]=="O" and overDisc=False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc=True:
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
		if gboard[i][j]=="O" and overDisc=False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc=True:
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
		if gboard[i][j]=="O" and overDisc=False:
			validPos.append(idxToHex(board_size,i,j))
		elif gboard[i][j]=="O" and overDisc=True:
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
	pass


def opening(board_size):
	move="P "
	while True:
		hexagon=random.randint(0,3)
		position=0
		if hexagon!=0:
			position=random.randint(0,6*hexagon-1)
		index=getindex(board_size,hexagon,position)
		if(BOARD[index[0]][index[1]]=="O"):
			move=move+hexagon +" "+position
			return move



if __name__ == '__main__':
	player_no=int(input())
	board_size=int(input())
	time_limit=int(input())
	RUN_SIZE=int(input())
	initial_config(5)
	showboard(BOARD)
	