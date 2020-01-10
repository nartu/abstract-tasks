inTxt = '''
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
'''

n = int(input())
fbM = [[i for i in input().split(';')] for s in range(n)]
#fbM = [i.split(';') for i in inTxt.strip().split('\n')[1:]]

#Command: Plays(0), Win(1), Drawn game(2), Not win(3), Points(4)
def win(win,notWin):
    tab[win][1] += 1 #Win
    tab[win][4] += 3 #Win points
    tab[notWin][3] += 1 #Not win
def drawnGame(c1,c2):
    tab[c1][2] += 1 #DG
    tab[c1][4] += 1 #Points
    tab[c2][2] += 1 #DG
    tab[c2][4] += 1 #Points

tab = dict()
for p in fbM:
    if(p[0] not in tab.keys()): #if not in table
        tab[p[0]] = [0,0,0,0,0]
    if(p[2] not in tab.keys()):
        tab[p[2]] = [0,0,0,0,0]
    tab[p[0]][0] += 1 #Plays
    tab[p[2]][0] += 1

    if(p[1]==p[3]):
        drawnGame(p[0],p[2])
    elif(p[1]>p[3]):
        win(p[0],p[2])
    else:
        win(p[2],p[0])

for c,t in tab.items():
    print(c+':',end='')
    print(*t)


'''
def command(c, res):
    if not c in dct: dct[c] = [0, 0, 0, 0, 0]
    dct[c] = [dct[c][0] + 1,
                dct[c][1] + 1 if res == 3 else dct[c][1],
                dct[c][2] + 1 if res == 1 else dct[c][2],
                dct[c][3] + 1 if res == 0 else dct[c][3],
                dct[c][4] + res,]
dct = {}
for i in range(int(input())):
    c1, g1, c2, g2 = input().split(';')
    command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
    command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
for c in dct:
    print('{}:{} {} {} {} {}'.format(c, *dct[c]))


def points_counter(team, goals1, goals2):
    if team not in teams:
        teams[team] = [0] * 5
    teams[team][0] += 1
    teams[team][1] += int(goals1 > goals2)
    teams[team][2] += int(goals1 == goals2)
    teams[team][3] += int(goals1 < goals2)
    teams[team][4] += int(goals1 > goals2) * 3 + int(goals1 == goals2)


teams = dict()

for _ in range(int(input())):
    k = input().split(';')
    points_counter(k[0], int(k[1]), int(k[3]))
    points_counter(k[2], int(k[3]), int(k[1]))

for el in teams:
    print('{}:{} {} {} {} {}'.format(el, *teams[el]))
'''
