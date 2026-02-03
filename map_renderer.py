import const
import map_manager

class MapRenderer:
    def __init__(self):
        self.img = {const.ROAD:'. ',const.WALL:'■ ',const.GOAL:'G ',const.PATH:'● '}
    def print_map(self,map_manager:map_manager.MapManager):
        current_map = map_manager.get_current_map()
        print("\n"+"="*22)
        for row in range(len(current_map)):
            one_row = []
            for col in range(len(current_map[0])):
                one_row.append(self.img[current_map[row][col]])
            print("".join(one_row))
        print("="*22)
    def print_path(self,map_manager:map_manager.MapManager,path_list):
        current_map = map_manager.get_current_map()
        for row,col in path_list:
            current_map[row][col] = const.PATH
        print("\n"+"="*22)
        for row in range(len(current_map)):
            one_row = []
            for col in range(len(current_map[0])):
                one_row.append(self.img[current_map[row][col]])
            print("".join(one_row))
        print("="*22)
        
