import map_manager
import map_renderer
import bfs_study
import os
import time
import const
if __name__ == "__main__" :
    map_m = map_manager.MapManager()
    map_r = map_renderer.MapRenderer()
    bfs = bfs_study.Bfs(map_m)
    while True:
        os.system('clear')
        status = bfs.one_step()
        map_r.print_path(map_m,bfs.get_path_list())
        if status == const.FOUND:
            print("FOUND")
            break
        elif status == const.STUCK:
            print("STUCK")
            break
    #한발짝 가기
    #print
    #기다리기
    