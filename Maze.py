"lines 13 - 54 & 59 - 61 were taken from ....."

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
            s = line[:15]       #takes first 15 characters from line
            q = s + s[::-1]     #add the same characters but in reverse for symmetry
            for e in range(len(q)):
                temp_row.append(q[e])   #put characters in list
            if counterForSomeReason == 0:
                self.temp_2d_list = temp_row    #adds first list to 2d list
                counterForSomeReason += 1
            else:
                self.temp_2d_list.append(temp_row)  #add the others lists to 2d list

        self.final_2d_list = [['.' for x in range(len(self.temp_2d_list))] for i in range(len(self.temp_2d_list[0]))]
        #define final 2d list since the orientation of the maze is wrong
        for a in range(len(self.temp_2d_list)):
            for b in range(len(self.temp_2d_list[0])):
                self.final_2d_list[b][a] = self.temp_2d_list[a][b]  #turn maze 90 degrees
        return self.final_2d_list

    def get_tile(self, position, tile_size):    #calculate tile according to position and tile size
        self.tile_size = tile_size
        self.tile = (int((position[0]) / self.tile_size), int((position[1]) / self.tile_size))
        return self.tile

    def manhat_dist(self, current, target):
        dx = abs(current[0]-target[0])
        dy = abs(current[1]-target[1])
        return dx+dy

    def get_neighbours(self, tile):
        neighbours = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for a in range(len(directions)):
            next_x = tile[0] + directions[a][0]
            next_y = tile[1] + directions[a][1]
            # print(len(self.final_2d_list[next_x]), next_y, len(self.final_2d_list), next_x)
            if len(self.final_2d_list[next_x])-1 >= next_y and next_y >= 0 and \
                    len(self.final_2d_list)-1 >= next_x and next_x >= 0:
                # print("t")
                if self.final_2d_list[tile[0]+directions[a][0]][tile[1]+directions[a][1]] != '|':
                    neighbours.append((tile[0]+directions[a][0], tile[1]+directions[a][1]))
        return neighbours

    def collision_detection_straight(self, pos, direction, tile_size):
        self.tile_size = tile_size
        self.pos = [pos[0]+self.tile_size/2, pos[1] + self.tile_size/2] #set position to center of tile
        self.direction = direction
        self.current_tile = self.get_tile(self.pos, self.tile_size)
        self.next_tile = self.get_tile(((self.pos[0] + self.direction[0]*(.5*tile_size)),
                                       (self.pos[1] + self.direction[1]*(.5*tile_size))),self.tile_size)
            #add .5 tilesize to position in order to see if border of the tile is almost hit
        if self.current_tile == self.next_tile:
            return False    #return false if border of tile is not reached
        else:
            if self.final_2d_list[self.next_tile[0]][self.next_tile[1]] == '|':
                return True #if border is reached and the next tile is a wall return true
            else:
                return False    # if next tile is not a wall return false

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
            #if the new direction is the opposite direction there is never a collision
            print("k")
            return False
        if (self.pos[0] % self.tile_size)**2 > 2 and (self.pos[1] % self.tile_size)**2 > 2 or \
                self.final_2d_list[self.next_tile[0]][self.next_tile[1]] == '|':
            #if too far from the center of a tile there is always a collision
            print("t")
            return True
        else:
            if self.final_2d_list[self.next_tile[0]][self.next_tile[1]] == '.': #and (self.pos[0] % (self.tile_size)**2 < 2) \
                     #and ((self.pos[1] % self.tile_size)**2 < 2): #and self.direction != [0, 0]:
                 return False   # if next tile is open there is no collision
            else:
                print("j")
                return True

    def center_detection(self, pos):
        if pos == [self.current_tile[0] * self.tile_size, self.current_tile[1] * self.tile_size]:
            return True
        else:
            return False

        # and self.pos != [current_tile[0] * tile_size, current_tile[1] * tile_size]: