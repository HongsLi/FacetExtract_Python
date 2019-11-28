# -*- coding:utf-8 -*-
import numpy as np
import community
import networkx as nx
import json
import csv
import utils.Utils as Utils


## 加载上下位关系
def load_sxw(domain):
    sxw = open('../dataset/domain_sxw/' + domain + '_auto.csv', 'r' ,encoding='utf-8')
    csv_reader = csv.reader(sxw)
    # 上下位关系是乱序的，所以需要从字典里查找
    topic_dict, topic_index_dict = Utils.get_topic_dict(domain)
    sxw = []
    nodes = len(topic_index_dict)
    for row in csv_reader:
        source = topic_dict.get(row[0])
        target = topic_dict.get(row[1])
        if source:
            sxw.append([source, target])
    # 返回用标号表示的上下位关系
    return nodes, sxw


## 根据上下位生成网络图
def generate_graph(nodes, sxw):
    G = nx.Graph()
    for i in range(nodes):
        G.add_node(i)
    for j in range(len(sxw)):
        G.add_edge(sxw[j][0], sxw[j][1])
    return G


## 根据网络图进行louvain划分，返回结果是一个字典，字典的每一个value列表代表一个类
def get_partition(G):
    partition = community.best_partition(G)
    node_nums = G.number_of_nodes()
    part_dict = {}
    for i in range(node_nums):
        if (partition[i] in part_dict):
            part_dict[partition[i]].append(i)
        else:
            part_dict[partition[i]] = [i]

    ## 将簇中结点过少的主题进行合并
    merge_dict = {-1: []}
    for k in part_dict.keys():
        if len(part_dict[k]) < 5:
            merge_dict[-1].extend(part_dict[k])
        else:
            merge_dict[k] = part_dict[k]
    return merge_dict


## 根据分割结果对P进行分割
def split_p(domain, part_dict):
    ori_p = np.loadtxt('../output/' + domain + '/Algorithm_sxw/A_generateP/P.txt')
    dict_len = len(part_dict)
    for k in part_dict.keys():
        # 每一个簇内的主题结点集合
        topic_list = part_dict[k]
        # 将主题结点提出作为子矩阵
        sub_topic_nums = len(topic_list)
        matrix = np.ones([sub_topic_nums, sub_topic_nums])
        for i in range(sub_topic_nums):
            for j in range(i + 1, sub_topic_nums):
                matrix[i][j] = ori_p[topic_list[i]][topic_list[j]]
                matrix[j][i] = matrix[i][j]
        # 簇的名字
        class_name = 'P' + str(k)
        # 将新的P写入
        np.savetxt('../output/' + domain + '/Algorithm_sxw/B_partition/' + class_name + '.txt', matrix)


## 写入社团划分结果
def write_part_dict(domain, part_dict):
    with open('../output/' + domain + '/Algorithm_sxw/B_partition/part_dict.json', 'w', encoding='utf-8') as f:
        json.dump(part_dict, f)


def B_partition(domain):
    nodes, sxw = load_sxw(domain)
    G = generate_graph(nodes, sxw)
    part_dict = get_partition(G)
    split_p(domain, part_dict)
    write_part_dict(domain, part_dict)


B_partition('Data_structure')
