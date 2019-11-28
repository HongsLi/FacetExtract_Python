# -*- coding:utf-8 -*-
import json
import os
import numpy as np
import utils.Utils as Utils


## 获取划分矩阵
def get_part_dict(domain):
    with open('../output/' + domain + '/Algorithm_sxw/B_partition/part_dict.json', 'r', encoding='utf-8') as f:
        part_dict = json.load(f)
    return part_dict
    
## 构建主题分面矩阵 主题列表就是在dataset中的主题列表 分面列表需要生成
def get_all_appeared_facets_in_domain(domain):
    all_facets = []
    for root, dirs, files in os.walk('../output/' + domain + '/Preprocess/E_deleteInitFacet/'):
        for file in files:
            with open(root + file, 'r', encoding='utf-8') as f:
                list = f.readlines()
                for l in list:
                    l = l.strip()
                    if l not in all_facets:
                        all_facets.append(l)

    all_facets = [a + '\n' for a in all_facets]
    print('All facet nums:', len(all_facets))
    with open('../output/' + domain + '/Algorithm_sxw/C_generateF/facet_list.txt', 'w', encoding='utf-8') as f:
        f.writelines(all_facets)

# 针对每一个簇，分别构造F
def constructF(domain):
    part_dict = get_part_dict(domain)
    part_nums = len(part_dict)
    with open('../output/' + domain + '/Algorithm_sxw/C_generateF/facet_list.txt', 'r', encoding='utf-8') as f:
        facet_list = f.readlines()
        facet_dict = {}
        i = 0

        # 构建字典，key=分面名 value=标号
        for facet in facet_list:
            if (facet.strip() == ''):
                continue
            facet_dict[facet.strip()] = i
            i += 1
        
        # tid是标号-主题字典
        td, tid = Utils.get_topic_dict(domain)

    # 循环构建F
    for k in part_dict.keys():
        topic_list = part_dict[str(k)]
        topic_nums = len(topic_list)
        class_name = 'F' + str(k)
        print('constructing ' + class_name)
        F = np.zeros([len(topic_list), len(facet_dict)])
        for topic_index in range(topic_nums):
            with open('../output/' + domain + '/Preprocess/E_deleteInitFacet/' + tid[topic_list[topic_index]] + '.txt', 'r', encoding='utf-8') as f:
                flist = f.readlines()
                for fl in flist:
                    fl = fl.strip()
                    F[topic_index, facet_dict[fl]] = 1
        np.savetxt('../output/' + domain + '/Algorithm_sxw/C_generateF/' + class_name + '.txt', F, fmt='%s')


def C_generateF(domain):
    get_all_appeared_facets_in_domain(domain)
    constructF(domain)

C_generateF('Physical_chemistry')