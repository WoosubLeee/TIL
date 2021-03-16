import socket
import time
import math

# User and Launcher Information
NICKNAME = 'SEOUL03_LEEWOOSUB'
HOST = '127.0.0.1'

# Static Value(Do not modify)
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# Predefined Variables(Do not modify)
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]


class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: %s:%d' % (HOST, PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: %s:%d' % (HOST, PORT))
        send_data = '%d/%s/' % (CODE_SEND, NICKNAME)
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play!\n--------------------')

    def request(self):
        self.sock.send('%d/%d' % (CODE_REQUEST, CODE_REQUEST).encode())
        print('Received Data has been currupted, Resend Requested.')

    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: %s' % recv_data)
        return recv_data

    def send(self, angle, power):
        if power <= 0:
            print('Power must be bigger than 0, Try again.')
            return False
        merged_data = '%f/%f/' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: %s' % merged_data)

    def close(self):
        self.sock.close()
        print('Connection Closed.\n--------------------')


class GameData:
    def __init__(self):
        self.order = 0
        self.reset()

    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)

    def arrange(self):
        self.order = self.balls[0][1]
        print('\n* You will be the %s player. *\n' %
              ('first' if self.order == 1 else 'second'))

    def show(self):
        print('====== Arrays ======')
        for i in range(NUMBER_OF_BALLS):
            print('Ball %d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print('====================')


def play(conn, gameData):
    angle = 0.0
    power = 0.0

    ##############################
    # Begining of Your Code
    # Put your code here to set angle and power values.
    # angle(float) must be between 0.0 and 360.0
    # power(float) must be between 1.0 and 100.0
    def make_new_holes(increase):
        NEW_H = []
        for hole in HOLES:
            temp = []
            if hole[0] == 0:
                temp.append(increase)
            elif hole[0] == 254:
                temp.append(254 - increase)
            else:
                temp.append(127)
            if hole[1] == 0:
                temp.append(increase)
            else:
                temp.append(127 - increase)
            NEW_H.append(temp)
        return NEW_H

    def calc_radian(s_x, s_y, e_x, e_y):
        width = abs(e_x - s_x)
        height = abs(e_y - s_y)
        try:
            if e_x > s_x:
                if e_y > s_y:
                    result = math.atan(width / height)
                else:
                    result = math.atan(height / width)
            else:
                if e_y < s_y:
                    result = math.atan(width / height)
                else:
                    result = math.atan(height / width)
        except:
            result = 180
        return result

    def calc_angle(s_x, s_y, e_x, e_y):
        angle_r = calc_radian(s_x, s_y, e_x, e_y)
        if e_x > s_x:
            if e_y > s_y:
                result = 180 / math.pi * angle_r
            else:
                result = (180 / math.pi * angle_r) + 90
        else:
            if e_y < s_y:
                result = (180 / math.pi * angle_r) + 180
            else:
                result = (180 / math.pi * angle_r) + 270
        return result

    def calc_distance(s_x, s_y, e_x, e_y):
        distance_w = abs(e_x - s_x)
        distance_h = abs(e_y - s_y)
        return math.sqrt(distance_w**2 + distance_h**2)

    def find_my_ball(gameData):
        if gameData.order == 1:
            for i in [1, 3, 5]:
                if gameData.balls[i][0] > 0:
                    targetBall_x = gameData.balls[i][0]
                    targetBall_y = gameData.balls[i][1]
                    return targetBall_x, targetBall_y
        else:
            for i in [2, 4, 5]:
                if gameData.balls[i][0] > 0:
                    targetBall_x = gameData.balls[i][0]
                    targetBall_y = gameData.balls[i][1]
                    return targetBall_x, targetBall_y

    def find_best_hole(white_x, white_y, target_x, target_y):
        shot_angle = calc_angle(white_x, white_y, target_x, target_y)
        min_gap = 360
        for i in range(6):
            hole_angle = calc_angle(target_x, target_y, NEW_H[i][0], NEW_H[i][1])
            gap = abs(hole_angle - shot_angle)
            if gap < min_gap:
                min_hole = i
                min_gap = gap
        return min_hole

    def calc_target_point(ball_x, ball_y, hole):
        radian = calc_radian(ball_x, ball_y, NEW_H[hole][0], NEW_H[hole][1])
        if NEW_H[hole][0] > ball_x:
            if NEW_H[hole][1] > ball_y:
                x_increase = -math.sin(radian)*5.72
                y_increase = -math.cos(radian)*5.72
            else:
                x_increase = -math.cos(radian)*5.72
                y_increase = math.sin(radian)*5.72
        else:
            if NEW_H[hole][1] < ball_y:
                x_increase = math.sin(radian)*5.72
                y_increase = math.cos(radian)*5.72
            else:
                x_increase = math.cos(radian)*5.72
                y_increase = -math.sin(radian)*5.72
        return ball_x + x_increase, ball_y + y_increase

    NEW_H = make_new_holes(2)

    whiteBall_x = gameData.balls[0][0]
    whiteBall_y = gameData.balls[0][1]

    targetBall_x, targetBall_y = find_my_ball(gameData)

    target_hole = find_best_hole(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)
    target_point = calc_target_point(targetBall_x, targetBall_y, target_hole)
    print(target_point[0], target_point[1])
    print(calc_distance(target_point[0], target_point[1], targetBall_x, targetBall_y))

    angle = calc_angle(whiteBall_x, whiteBall_y, target_point[0], target_point[1])
    distance = calc_distance(whiteBall_x, whiteBall_y, target_point[0], target_point[1])

    power = distance/2

    print(calc_angle(targetBall_x, targetBall_y, NEW_H[target_hole][0], NEW_H[target_hole][1]))

    # You can clear Stage 1 with the pre-written code above.
    # Those will help you to figure out how to clear other Stages.
    # Good luck!!
    # End of Your Code
    ##############################

    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        if gameData.balls[0][0] == SIGNAL_ORDER:
            gameData.arrange()
            continue
        elif gameData.balls[0][0] == SIGNAL_CLOSE:
            break
        gameData.show()
        play(conn, gameData)
    conn.close()


if __name__ == '__main__':
    main()
