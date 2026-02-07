import const
import map_manager
START_POS = [0,0]
class Node:
    def __init__(self,row,col):
        self.pos = (row,col)
        self.G = 0
        self.H = 0
        self.F = 0
class MyHeap:
    def __init__(self):
        self.__body = []
    def __heapify(self):
        # r child : 2*n+1
        # l child : 2*n+2
        # parent : floor(log_2(n))
        pointer = 
        #TODO
    def get_size(self):
        return len(self.__body)
    def push(self,node:Node):
        self.__body.append(node)
        self.__heapify()
    def pop(self)->Node:
        if self.get_size()==0:
            raise Exception
        self.__body[0],self.__body[self.get_size()-1] = self.__body[self.get_size()-1], self.__body[0]
        return_value = self.__body.pop()
        self.__heapify()
        return return_value
class Astar:
    def __init__(self,map_manager:map_manager.MapManager):
        self.__path_list = []
        self.__move = {const.LEFT:(0,-1),const.RIGHT:(0,1),const.UP:(1,0),const.DOWN:(-1,0)}
        self.__map_manager = map_manager
        init_node = Node(START_POS[0],START_POS[1])
        init_node.H = self.__get_h(init_node)
        init_node.F = init_node.G + init_node.H
        self.__que = [init_node]
    def __get_h(self,node:Node):
        goal_pos = self.__map_manager.get_goal_pos()
        node_pos = node.pos
        return abs(goal_pos[0]+node_pos[0]) + abs(goal_pos[1]+node_pos[1])
    def one_step(self):
        if len(self.__que)==0 and len(self.__path_list)==0:
            return const.STUCK
        print(f"DEBUG: 현재 큐 사이즈 = {len(self.__que)}")
        #pop most small F
        current_node = self.__que.pop()
        self.__path_list.append(current_node)
        for move,dif in self.__move.items():
            row,col = current_node.pos[0]+dif[0],current_node.pos[1]+dif[1]
            if not self.__map_manager.is_out_of_map([row,col]) :
                if not self.__map_manager.is_wall([row,col]):
                    if self.__map_manager.is_game_end([row,col]):
                        return const.FOUND
                    elif not [row,col] in self.__path_list and not [row,col] in self.__que :
                        self.__que.append([row,col])
        return const.SEARCHING