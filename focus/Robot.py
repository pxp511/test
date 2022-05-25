from operator import index
import os
import pickle
import shutil
from time import sleep
from focus.Ftree import *


def fetch_from_origin(debug: bool):
    try:
        # print("Fetching new changes from origin......")
        if not debug:
            sh(f"git fetch")
        # print("Done fetching, you don't need to fetch anymore")
    except Exception as e:
        print(e)
        exit()
    

def get_local_head_hashnumber() -> str:
    try:
        hashnumber = os.popen(f"git rev-parse HEAD").read()[:-1]
    except Exception as e:
        print(e)
        exit()
    return hashnumber


def add_focus_file(file_path, tree):
    node, is_find = find_node(file_path, tree)
    if is_find:
        node.data.is_focused = True


class Robot(object):

    def __init__(
        self,
        repository: str,
        debug: bool,
        queryinterval: int 
        ):
        self._debug = debug
        self._query_interval = queryinterval
        self._repository = repositorys
    
    def get_show_list(self):
        show_list = []
        change_list = self._change_list
        children = self._tree.leaves()
        while indexl < lengthl:
            record = change_list[indexl]
            node = children[indext]
            pathl = record["path"]