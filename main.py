import map_manager
import map_renderer
import bfs_study
import dfs_study
import os
import time
import const
if __name__ == "__main__" :
    map_m = map_manager.MapManager()
    map_r = map_renderer.MapRenderer()
    #algo = bfs_study.Bfs(map_m)
    algo = dfs_study.Dfs(map_m)
    #algo = astar_study.Astar(map_m)
    while True:
        os.system('clear')
        status = algo.one_step()
        map_r.print_path(map_m,algo.get_path_list())
        if status == const.FOUND:
            print("FOUND")
            break
        elif status == const.STUCK:
            print("STUCK")
            break
        time.sleep(0.2)
    #한발짝 가기
    #print
    #기다리기
    