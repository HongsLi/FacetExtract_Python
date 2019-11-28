# -*- coding:utf-8 -*-
import utils.Utils as Utils
import numpy as np


def get_origin_facet_nums(domain):
    facet_nums = []
    topic_list = Utils.get_topics_by_domain(domain)
    for topic in topic_list:
        with open('../output/' + domain + '/Preprocess/E_deleteInitFacet/' + topic.strip() + '.txt', 'r',
                  encoding='utf-8') as f:
            facet_nums.append(len(f.readlines()))
    return facet_nums


def get_labeled_facet_num(domain, topic):
    with open('../dataset/labeled_facets/' + domain + '/' + topic.strip() + '.txt', 'r',
              encoding='utf-8') as f:
        fs = f.readlines()
        return len(fs)

def is_in_candidate_facets(f, cflist):
    if(f in cflist):
        return True
    else:
        return False

def analyse(domain):
    print('analysing...')
    # 初始分面数
    origin_facet_nums = get_origin_facet_nums(domain)
    with open('../output/' + domain + '/Analyse/appeared_facet_in_labeled_data.txt', 'r', encoding='utf-8') as f:
        af = f.readlines()
        af = [a.strip() for a in af]

    # 分面查询字典
    with open('../output/' + domain + '/Algorithm/B_generateF/facet_list.txt', 'r', encoding='utf-8') as f:
        facet_list = f.readlines()
        facet_dict = {}
        i = 0
        # 构建字典
        for facet in facet_list:
            if (facet.strip() == ''):
                continue
            facet_dict[i] = facet.strip()
            i += 1

    # 主题查询字典
    topic_dict, topic_index_dict = Utils.get_topic_dict(domain)

    result_matrix = np.loadtxt('../output/' + domain + '/Algorithm/C_LP/result0.0001.txt')
    for i in range(len(topic_index_dict)):
        print(i + 1, 'of', len(topic_index_dict))
        topic = topic_index_dict[i]
        tf = result_matrix[i]
        facets = ['application', 'property', 'example', 'definition']
        # facet_nums = int((origin_facet_nums[i]) * 1.1)
        # facet_nums = get_labeled_facet_num(domain, topic) - 4
        facet_nums = int((origin_facet_nums[i]))
        for i in range(facet_nums):
            # 找到最大的位置
            max_pos = np.where(tf == np.max(tf))
            y = max_pos[0][0]
            # 取出对应位置的分面
            target_facet = facet_dict[y]
            facets.append(facet_dict[y])
            if(is_in_candidate_facets(target_facet, af)):
                facets.append(facet_dict[y])
            else:
                # i -= 1
                 pass
            # 最大位置置0
            tf[y] = 0

        # 加入回车，写入最终结果
        facets = [fa + '\n' for fa in facets]
        facets = list(set(facets))
        with open('../output/' + domain + '/Algorithm/D_analyse/' + topic + '.txt', 'w',
                  encoding='utf-8') as result_file:
            result_file.writelines(facets)
    print('done')



analyse('Data_mining')
