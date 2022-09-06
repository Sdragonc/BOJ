import sys
input = lambda: sys.stdin.readline().rstrip()
A, B = map(int, input().split())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0] # N, W, S, E
n, m = map(int, input().split())
wall_flag = False
robot_flag = False
mtr = [[0 for _ in range(B)]for _ in range(A)]
robot_hash = {}
for i in range(n):
    x, y, dir = input().split()
    x, y = int(x), int(y)
    x -= 1
    y -= 1
    if dir == "N":
        dir = 0
    elif dir == "W":
        dir = 1
    elif dir == "S":
        dir = 2
    elif dir == "E":
        dir = 3
    robot_hash[i+1] = [x, y, dir]
    mtr[x][y] = i+1
wall_robot = 0
robot_crash = []
commands = []
for _ in range(m):
    commands.append(list(input().split()))
for comman in commands:
    robot = comman[0]
    com = comman[1]
    lit = comman[2]
    robot, lit = int(robot), int(lit)
    if com == 'F':
        mtr[robot_hash[robot][0]][robot_hash[robot][1]] = 0
        for _ in range(lit):
            robot_hash[robot][0] += dx[robot_hash[robot][2]]
            robot_hash[robot][1] += dy[robot_hash[robot][2]]
            if robot_hash[robot][0] < 0 or robot_hash[robot][1] < 0 or robot_hash[robot][0] >= A or robot_hash[robot][1] >= B:
                wall_flag = True
                wall_robot = robot
                break
            if mtr[robot_hash[robot][0]][robot_hash[robot][1]] != 0:
                robot_flag = True
                robot_crash = [robot, mtr[robot_hash[robot][0]][robot_hash[robot][1]]]
                break
        if wall_flag or robot_flag:
            break
        mtr[robot_hash[robot][0]][robot_hash[robot][1]] = robot
    elif com == "L":
        for _ in range(lit):
            robot_hash[robot][2] += 1
            if robot_hash[robot][2] == 4:
                robot_hash[robot][2] = 0
    else:
        for _ in range(lit):
            robot_hash[robot][2] -= 1
            if robot_hash[robot][2] == -1:
                robot_hash[robot][2] = 3
if wall_flag:
    print('Robot {0} crashes into the wall'.format(wall_robot))
elif robot_flag:
    print('Robot {0} crashes into robot {1}'.format(robot_crash[0], robot_crash[1]))
else:
    print('OK')