import os
import time

import bfs_study
import const
import dfs_study
import map_manager
import map_renderer


ALGO = "dfs"  # "bfs" 또는 "dfs" 중 선택


def create_algo(name: str, mm: map_manager.MapManager):
    name = name.lower()
    if name == "bfs":
        return bfs_study.Bfs(mm)
    if name == "dfs":
        return dfs_study.Dfs(mm)
    raise ValueError(f"Unknown algorithm: {name}")


if __name__ == "__main__":
    map_m = map_manager.MapManager()
    map_r = map_renderer.MapRenderer()
    algo = create_algo(ALGO, map_m)

    while True:
        os.system("clear")
        status = algo.one_step()
        map_r.print_path(map_m, algo.get_path_list())
        if status == const.FOUND:
            print("FOUND")
            break
        if status == const.STUCK:
            print("STUCK")
            break
        time.sleep(0.2)
