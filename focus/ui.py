import os
from tkinter import *
from focus.Robot import Robot, fetch_from_origin

a = 1
b = 2
def path_to_list(path):
    l = []
    dname = os.path.dirname(path)
    while dname != "":
        l.append(os.path.basename(dname))
        dname = os.path.dirname(dname)
    l.reverse()
    l.append(bname)
    return l


def find_node(file_path):
    is_find = True
    path_list = path_to_list(file_path)
    tree = robot._tree
    node = tree.get_node(tree.root)
    for path in path_list:
        children = tree.children(node.identifier)
        is_exist = False
        for child in children:
            if child.tag == path:
                node = child
                is_exist = True
                break
        if not is_exist:
            is_find = False
    return node, is_find



def renew():
    if robot.tree_need_change():
        robot.init()
    print('*'*50 + '\n')
    robot._tree.show()
    robot._tree.show(data_property="is_focused")
    robot._tree.show(data_property="path")
