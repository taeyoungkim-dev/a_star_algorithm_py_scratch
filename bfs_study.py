import const
import map_manager
START_POS = [0,0]
class Bfs:
    def __init__(self,map_manager:map_manager.MapManager):
        self.__que = [START_POS]
        self.__path_list = []
        self.__move = {const.LEFT:(0,-1),const.RIGHT:(0,1),const.UP:(1,0),const.DOWN:(-1,0)}
        self.__map_manager = map_manager
    def one_step(self):
        if len(self.__que)==0 and len(self.__path_list)==0:
            return const.STUCK
        print(f"DEBUG: 현재 큐 사이즈 = {len(self.__que)}")
        current_pos = self.__que.pop(0)
        self.__path_list.append(current_pos)
        for move,dif in self.__move.items():
            row,col = current_pos[0]+dif[0],current_pos[1]+dif[1]
            if not self.__map_manager.is_out_of_map([row,col]) :
                if not self.__map_manager.is_wall([row,col]):
                    if self.__map_manager.is_game_end([row,col]):
                        return const.FOUND
                    elif not [row,col] in self.__path_list and not [row,col] in self.__que :
                        self.__que.append([row,col])
        return const.SEARCHING
    def get_path_list(self):
        return [coordinate for coordinate in self.__path_list]