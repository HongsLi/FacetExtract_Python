# -*- coding:utf-8 -*-
import utils.Utils as Utils
import numpy as np
import json


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


## 是否出现在标注分面中
def is_in_candidate_facets(f, cflist):
    if (f in cflist):
        return True
    else:
        return False


def get_part_dict(domain):
    with open('../output/' + domain + '/Algorithm_sxw/B_partition/part_dict.json', 'r', encoding='utf-8') as f:
        part_dict = json.load(f)
    return part_dict


def analyse(domain):
    with open('../output/' + domain + '/Analyse/appeared_facet_in_labeled_data.txt', 'r', encoding='utf-8') as f:
        af = f.readlines()
        af = [a.strip() for a in af]

    print('analysing...')
    origin_facet_nums = get_origin_facet_nums(domain)
    # 分面查询字典
    with open('../output/' + domain + '/Algorithm_sxw/C_generateF/facet_list.txt', 'r', encoding='utf-8') as f:
        facet_list = f.readlines()
        facet_dict = {}
        i = 0
        # 构建字典
        for facet in facet_list:
            if (facet.strip() == ''):
                continue
            facet_dict[i] = facet.strip()
            i += 1

    topic_dict, topic_index_dict = Utils.get_topic_dict(domain)

    # 切割字典
    part_dict = get_part_dict(domain)
    part_nums = len(part_dict)

    # 在每一个簇内进行分析， index是簇标号
    for index in part_dict.keys():
        # if index == '-1':
        #     continue
        print(str(index) + 'th cluster')
        result = np.loadtxt('../output/' + domain + '/Algorithm_sxw/D_LP/result' + str(index) + '.txt')
        topic_list = part_dict[str(index)]  # 这个簇内的主题标号
        # topic_index表示是簇内的第几个主题
        for topic_index in range(len(topic_list)):
            # 该矩阵的某一行
            tf = result[topic_index]

            facets = ['application', 'property', 'example', 'definition']
            facet_nums = int((origin_facet_nums[topic_list[topic_index]]) * 1)
            if facet_nums == 0:
                facet_nums = 2
            # facet_nums = get_labeled_facet_num(domain, topic_index_dict[topic_list[topic_index]]) - 4
            for i in range(facet_nums):
                # 找到最大的位置
                max_pos = np.where(tf == np.max(tf))
                y = max_pos[0][0]
                # 取出对应位置的分面
                target_facet = facet_dict[y]

                if (is_in_candidate_facets(target_facet, af)):
                    facets.append(facet_dict[y])
                else:
                    # i -= 1
                    pass
                # 最大位置置0
                tf[y] = 0
            facets = [fa + '\n' for fa in facets]
            facets = list(set(facets))

            with open('../output/' + domain + '/Algorithm_sxw/E_analyse/' + topic_index_dict[
                topic_list[topic_index]] + '.txt', 'w',
                      encoding='utf-8') as result_file:
                result_file.writelines(facets)


analyse('Data_structure_new')
