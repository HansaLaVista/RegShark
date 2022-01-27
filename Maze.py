from Map import Map
import sys

class Maze:
    # reflect the first 14 columns to print the map
    def __init__(self):
        self.next_tile = (-1, -1)
        self.final_2d_list = [[]]
        self.current_tile = (0,0)

    def generate_matrix(self):

        tileMap = Map(16, 31, """
                            ||||||||||||||||
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |.........||||||
                            |.........||||||
                            |.........||||||
                            |.........||||||
                            |.........||||||
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            |...............
                            ||||||||||||||||
                            """)
        # verbosity option (-v)
        if len(sys.argv) > 1 and sys.argv[1] == "-v":
            tileMap.verbose = True

        # generate map by adding walls until there's no more room
        while tileMap.add_wall_obstacle(extend=True):
            pass

        self.temp_2d_list = [[]]    #make list for map
        counterForSomeReason = 0    #counter makes sure that the 2d list get set right

        for line in str(tileMap).splitlines():
            temp_row = []
            s = line[:15]
            q = s + s[::-1]
            for e in range(len(q)):
                temp_row.append(q[e])
            if counterForSomeReason == 0:
                self.temp_2d_list = temp_row
                counterForSomeReason += 1
            else:
                self.temp_2d_list.append(temp_row)

        self.final_2d_list = [['.' for x in range(len(self.temp_2d_list))] for i in range(len(self.temp_2d_list[0]))]
        for a in range(len(self.temp_2d_list)):
            for b in range(len(self.temp_2d_list[0])):
                self.final_2d_list[b][a] = self.temp_2d_list[a][b]
        #print(self.temp_2d_list)
        #print(temp_2d_list[1][1])
        #print(self.final_2d_list)
        return self.final_2d_list

    def get_tile(self, position, tile_size):
        self.tile_size = tile_size
        self.tile = (int((position[0]) / self.tile_size), int((position[1]) / self.tile_size))
        return self.tile

    def collision_detection_straight(self, pos, direction, tile_size):
        self.tile_size = tile_size
        self.pos = [pos[0]+self.tile_size/2, pos[1] + self.tile_size/2]
        self.direction = direction
        self.current_tile = self.get_tile(self.pos, self.tile_size)
        self.next_tile = self.get_tile((self.pos[0]+ self.direction[0]*12.5,self.pos[1]+ self.direction[1]*12.5), self.tile_size)
        if self.current_tile == self.next_tile:

            return False
        else:
            if self.final_2d_list[self.next_tile[0]][self.next_tile[1]] == '|':
                return True
            else:
                return False

    def collision_detection_direction(self, pos, direction, new_direction, tile_size):
        self.tile_size = tile_size
        self.pos = pos
        self.direction = direction
        self.new_direction = new_direction
        self.current_tile = self.get_tile(self.pos, self.tile_size)
        self.next_tile = (self.current_tile[0]+self.new_direction[0],self.current_tile[1]+self.new_direction[1])
        print(self.pos, (self.pos[0] % self.tile_size)**2, (self.pos[1] % self.tile_size)**2)
        if (self.new_direction[0] == -self.direction[0] or self.new_direction[1] == -self.direction[1]) and \
                self.direction != [0, 0]:
            print("k")
            return False
        if (self.pos[0] % self.tile_size)**2 > 2 and (self.pos[1] % self.tile_size)**2 > 2 and \
                self.final_2d_list[self.next_tile[0]][self.next_tile[1]] == '|':
            print("t")
            return True
        else:

            if self.final_2d_list[self.next_tile[0]][self.next_tile[1]] == '.':# and (self.pos[0] % (self.tile_size)**2 < 2) \
                     #and ((self.pos[1] % self.tile_size)**2 < 2): #and self.direction != [0, 0]:
                 return False
            else:
                print("j")
                return True

    def center_detection(self):
        if self.pos == [self.current_tile[0] * self.tile_size, self.current_tile[1] * self.tile_size]:
            return True
        else:
            return False

        # and self.pos != [current_tile[0] * tile_size, current_tile[1] * tile_size]: