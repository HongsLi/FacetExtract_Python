# -*-coding:utf-8 -*-
import os
import utils.Utils as Utils
import numpy as np

# 构建主题分面矩阵 主题列表就是在dataset中的主题列表 分面列表需要生成
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
    with open('../output/' + domain + '/Algorithm/B_generateF/facet_list.txt', 'w', encoding='utf-8') as f:
        f.writelines(all_facets)


# 构建向量F
def construct_F(domain):
    with open('../output/' + domain + '/Algorithm/B_generateF/facet_list.txt', 'r', encoding='utf-8') as f:
        facet_list = f.readlines()
        facet_dict = {}
        topic_dict = {}
        i = 0

        # 构建字典
        for facet in facet_list:
            if (facet.strip() == ''):
                continue
            facet_dict[facet.strip()] = i
            i += 1

        topic_list = Utils.get_topics_by_domain(domain)
        i = 0
        for topic in topic_list:
            if (topic.strip() == ''):
                continue
            topic_dict[topic.strip()] = i
            i += 1

    F = np.zeros([len(topic_dict), len(facet_dict)])

    # 遍历分面文件夹 设置F
    for root, dirs, files in os.walk('../output/' + domain + '/Preprocess/E_deleteInitFacet/'):
        for file in files:
            with open(root + file, 'r', encoding='utf-8') as f:
                topic = file[:file.rindex('.')]
                flist = f.readlines()
                for f in flist:
                    f = f.strip()
                    F[topic_dict[topic], facet_dict[f]] = 1
    np.set_printoptions(suppress=True)
    np.set_printoptions(precision=3)  # 设精度为3
    np.savetxt('../output/' + domain + '/Algorithm/B_generateF/F.txt', F, fmt='%s')

#

get_all_appeared_facets_in_domain('Physical_chemistry')
construct_F('Physical_chemistry')
