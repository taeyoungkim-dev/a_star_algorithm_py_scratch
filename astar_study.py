import const
import map_manager
START_POS = [0,0]
class Node:
    def __init__(self,row,col):
        self.pos = (row,col)
        # G : 과거에 왔던 거리
        # H : 남은 거리(장애물 고려 X)
        # F = G+H
        self.G = 0
        self.H = 0
        self.F = 0
class MyHeap:
    def __init__(self):
        self.__body = []
    def get_size(self):
        return len(self.__body)
    def __heapify_up(self,index):
        # r child : 2*n+1
        # l child : 2*n+2
        # parent : (n-1)//2
        parent_index = (index-1)//2
        if not index==0 and self.__body[parent_index].F > self.__body[index].F:
            self.__body[parent_index],self.__body[index] = self.__body[index],self.__body[parent_index]
            self.__heapify_up(parent_index)
    def __heapify_down(self,index):
        l_child_index = 2*index+1
        r_child_index = 2*index+2
        if l_child_index>=len(self.__body):
            return
        elif r_child_index >= len(self.__body) :
            if self.__body[l_child_index].F<self.__body[index].F:
                self.__body[l_child_index],self.__body[index] = self.__body[index],self.__body[l_child_index]
                self.__heapify_down(l_child_index)
                return
        if self.__body[l_child_index].F<self.__body[index].F and self.__body[r_child_index].F<self.__body[index].F:
            if self.__body[l_child_index].F < self.__body[r_child_index].F:
                self.__body[l_child_index],self.__body[index] = self.__body[index],self.__body[l_child_index]
                self.__heapify_down(l_child_index)
            else :
                self.__body[r_child_index],self.__body[index] = self.__body[index],self.__body[r_child_index]
                self.__heapify_down(r_child_index)
        elif self.__body[l_child_index].F<self.__body[index].F:
            self.__body[l_child_index],self.__body[index] = self.__body[index],self.__body[l_child_index]
            self.__heapify_down(l_child_index)
        elif self.__body[r_child_index].F<self.__body[index].F:
            self.__body[r_child_index],self.__body[index] = self.__body[index],self.__body[r_child_index]
            self.__heapify_down(r_child_index)
    def get_size(self):
        return len(self.__body)
    def push(self,node:Node):
        self.__body.append(node)
        self.__heapify_up(len(self.__body)-1)
    def pop(self)->Node:
        if self.get_size()==0:
            raise Exception
        self.__body[0],self.__body[self.get_size()-1] = self.__body[self.get_size()-1], self.__body[0]
        return_value = self.__body.pop()
        self.__heapify_down(0)
        return return_value
    def is_in(self,pos)->bool:
        row,col = pos
        for node in self.__body:
            n_row, n_col = node.pos
            if n_row==row and n_col==col:
                return True
        return False
class Astar:
    def __init__(self,map_manager:map_manager.MapManager):
        self.__path_list = []
        self.__move = {const.LEFT:(0,-1),const.RIGHT:(0,1),const.UP:(1,0),const.DOWN:(-1,0)}
        self.__map_manager = map_manager
        init_node = Node(START_POS[0],START_POS[1])
        init_node.H = self.__get_h(init_node)
        init_node.F = init_node.G + init_node.H
        self.__heap = MyHeap()
        self.__heap.push(init_node)
    def __get_h(self,node:Node):
        goal_pos = self.__map_manager.get_goal_pos()
        node_pos = node.pos
        return abs(goal_pos[0]-node_pos[0]) + abs(goal_pos[1]-node_pos[1])
    def one_step(self):
        if self.__heap.get_size()==0 and len(self.__path_list)==0:
            return const.STUCK
        print(f"DEBUG: 현재 힙 사이즈 = {self.__heap.get_size()}")
        #pop most small F
        current_node = self.__heap.pop()
        self.__path_list.append(current_node.pos)
        for move,dif in self.__move.items():
            row,col = current_node.pos[0]+dif[0],current_node.pos[1]+dif[1]
            if not self.__map_manager.is_out_of_map([row,col]) :
                if not self.__map_manager.is_wall([row,col]):
                    if self.__map_manager.is_game_end([row,col]):
                        return const.FOUND
                    elif not (row,col) in self.__path_list and not self.__heap.is_in((row,col)) :
                        push_node = Node(row,col)
                        push_node.G = current_node.G+1
                        push_node.H = self.__get_h(push_node)
                        push_node.F = push_node.G + push_node.H
                        self.__heap.push(push_node)
        return const.SEARCHING
    def get_path_list(self):
        return [coordinate for coordinate in self.__path_list]