MATRIX_SIZE = 10

import const
class MapManager:
    def __init__(self,map_size=MATRIX_SIZE):
        #맵 생성
        self.__map_size = map_size
        self.__map = [[const.ROAD]*self.__map_size for _ in range(self.__map_size)]
        self.__set_wall()
        self.__set_goal()
        
    #Wall과 Goal은 하드코딩으로 위치를 정해뒀음.
    def __set_wall(self)->None:
        walls = [
            # 1. 첫 번째 거대한 벽 (왼쪽 -> 오른쪽 가는 길 막음)
            # 0번 행부터 8번 행까지 3번 열을 꽉 막음. (9번 행으로만 통과 가능)
            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
            
            # 2. 두 번째 거대한 벽 (오른쪽 -> 목표점 가는 길 막음)
            # 1번 행부터 9번 행까지 7번 열을 꽉 막음. (0번 행으로만 통과 가능)
            (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7),

            # 3. 낚시용 장애물 (중간중간 길을 헷갈리게 만듦)
            (9, 5), (4, 5), (2, 1), (6, 8)
        ]
        for r, c in walls:
            self.__map[r][c] = const.WALL # 1은 벽
    def __set_goal(self)->None:
        self.__map[9][9] = const.GOAL
        
        
    def is_out_of_map(self,coordinate)->bool:
        row,col = coordinate
        return not (0<=row<self.__map_size) or not (0<=col<self.__map_size)
    def is_wall(self,coordinate)->bool:
        row,col = coordinate
        return self.__map[row][col]==const.WALL
    def is_game_end(self,coordinate)->bool:
        row,col = coordinate
        return self.__map[row][col]==const.GOAL
    def get_current_map(self):
        return [row[:] for row in self.__map]