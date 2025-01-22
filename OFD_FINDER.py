import time
import turtle
import numpy as np
class Node():

    """A node class for A* Pathfinding"""
    """2025.01.22일 깃허브테스트용으로 약간수정"""
    """한 줄 더 추가"""

    def __init__(self, parent=None, position=None,facility=None,location=None ):

        self.parent = parent
        self.position = position
        self.facility = facility
        self.location = location
        self.g = 0
        self.h = 0
        self.f = 0


    def __eq__(self, other):

        return self.position == other.position #and self.facility == other.facility


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    print ("start :", start[1], start[2])
    print("end :",end[1], end[2])
    #for x in maze :
        #print (x)

    # Create start and end node
    #print ("in astar")

    start_node = Node(None, start[0], start[1])
    start_node.g = start_node.h = start_node.f = 0

    end_node = Node(None, end[0], end[1])
    end_node.g = end_node.h = end_node.f = 0



    # Initialize both open and closed list

    open_list = []

    closed_list = []

    # Add the start node

    open_list.append(start_node)

    # Loop until you find the end

    current_index = 0
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):

            if item.f < current_node.f:

                current_node = item


                current_index = index

        # Pop current off open list, add to closed list

        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal

        if current_node == end_node:

            path = []

            current = current_node

            while current is not None:

                path.append(current.position)

                current = current.parent

            return path[::-1] # Return reversed path

        # Generate children

        children = []

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: #, (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position

            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])


            # Make sure within range

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:

                continue

            # Make sure walkable terrain

            if maze[node_position[0]][node_position[1]] != 0:

                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children

        for child in children:



            # Child is on the closed list

            for closed_child in closed_list:

                if child == closed_child:

                    continue

            # Create the f, g, and h values

            child.g = current_node.g + 1
            child.h = (abs(child.position[0] - end_node.position[0])) + (abs(child.position[1] - end_node.position[1]))

            child.f = child.g + child.h

            # Child is already in the open list

            for open_node in open_list:

                if child == open_node and child.g > open_node.g:

                    continue



            # Add the child to the open list

            open_list.append(child)


def main():


    SEJ171 = ((18,5),'SEJ171','NAMCHEONGJU_2F')







    #OFD2F_4324=(8,3)
    OFD2F_4341 = ((4,5),'OFD2F_4341','NAMCHEONGJU_3F')


    FO_2F07 = (20,4)
    XLG001 = (20,4)

    OFD_ALL = []
    #OFD_ALL.append(OFD2F_4324)
    OFD_ALL.append(OFD2F_4341)
    #OFD_ALL.append(FO_2F07)

    Facility = SEJ171


    Vertical={'01':2.4,  \
              '12': 2.4,  \
              '23': 2.4,  \
              '34': 3.2,  \
              '45': 2.4,  \
              '56': 2.4, \
              '67': 2.2, \
              '78': 2.8,  \
              '89': 2.8, \
              '78': 2.8, \
              '89': 2.8,\
              '78': 2.8, \
              '89': 2.8,\
              '910': 2.8, \
              '1011': 1.8, \
              '1112': 1.8, \
              '1213': 1.8,\
              '1314': 1.8, \
              '1415': 1.8,\
              '1516': 1.8, \
              '1617': 1.8,\
              '1718': 1.8, \
              '1819': 1.8, \
              '1920': 1.8,  }

    Vertical_3F_NamCheongJu = {'01': 2.4, \
                '12': 2.4, \
                '23': 2.4, \
                '34': 3.2, \
                '45': 2.4, \
                '56': 2.4, \
                '67': 2.2, \
                '78': 2.8, \
                '89': 2.8, \
                '78': 2.8, \
                '89': 2.8, \
                '78': 2.8, \
                '89': 2.8, \
                '910': 2.8, \
                '1011': 2.8, \
                '1112': 2.8, \
                '1213': 2.8, \
                '1314': 2.8, \
                '1415': 2.8, \
                '1516': 2.8, \
                '1617': 2.8, \
                '1718': 2.8, \
                '1819': 2.8, \
                '1920': 2.8, }
    maze = [
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 100베이 (0,0) ~ (0,13) 100베이 200베이 0-1-2
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 200베이
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 300베이
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 400베이
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 500베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 600베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 700베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 800베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 900베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1000베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 1100베이  (20,0) ~ (20,13)
    np.save('maze.npy',maze)

    maze_3F_NamCheongJu = [
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 100베이 (0,0) ~ (0,13) 100베이 200베이 0-1-2
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 200베이
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 300베이
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 400베이
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 500베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 600베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 700베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 800베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 900베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1000베이
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 1100베이  (20,0) ~ (20,13)

    for x in OFD_ALL :


        start = 0
        total_move = 0
        now = 0
        path = astar(maze, Facility, x)

        print("Cable Path : ",path)
        for z in path:
            if start == 0 :
                now = z[0]
                start = 1
                continue

            else :
                if now != z[0] :
                    if int(now) < int (z[0]):
                        vertical_position_move = str(now)+str(z[0])
                    else :
                        vertical_position_move =  str(z[0])+str(now)
                    total_move = total_move + float(Vertical[vertical_position_move])

                else :
                    total_move = total_move + float(0.6)

                now = z[0]
        print("Total optical cable length : ", round(total_move, 1))

        maze_solved = maze
        for z in path:
            maze_solved[z[0]][z[1]] = 7
        print ("\n############# Cable Path Map #############")



        # 그림그리는 부분
        # 녹색 : 장비 또는 OFD
        # 노란색 : 케이블트레이
        # 빨간색 : 최적 케이블 거리
        x_position = -250
        y_position = 180
        row_add = 10
        step = 0
        turtle.penup()
        turtle.goto(-250, 210)
        turtle.pendown()
        turtle.write("Total optical cable length : "+str( round(total_move, 1)), font=("serif",10,"normal"))  # 문자 쓰기
        turtle.penup()
        turtle.goto(-250, 250)
        turtle.pendown()
        turtle.write("Start Facility(OFD) : "+str( Facility[1]), font=("serif",10,"normal"))
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(-250, 230)
        turtle.pendown()
        turtle.write("End Facility(OFD) : "+str( x[1]), font=("serif",10,"normal"))
        turtle.hideturtle()
        for row in maze_solved:
            for x in row:
                turtle.tracer(1000)
                turtle.pensize(1)  # 펜의 두께를 1 픽셀
                turtle.penup()
                turtle.goto(x_position + 20 * step, y_position + row_add)
                turtle.pendown()
                turtle.begin_fill()
                if x == 1:
                    turtle.color("green")
                elif x == 7:
                    turtle.color("orange")
                else:
                    turtle.color("yellow")
                turtle.setheading(45)
                turtle.circle(12, steps=4)  # 사각형 그리기
                turtle.end_fill()
                step = step + 1
            row_add = row_add - 20
            x_position = x_position - 20 * len(row)

        turtle.mainloop()


        for y in maze_solved :
            print (y)
        print ("##########################################\n\n")





if __name__ == '__main__':

    main()