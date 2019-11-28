# -*- coding:utf-8 -*-
import json
import os
from utils.Topic import Topic


# 获得某个领域下的主题列表，返回一个数组
def get_topics_by_domain(domain_name):
    with open('../dataset/domain_topics/' + domain_name + '_topics.txt', 'r', encoding='utf-8') as f:
        topic_list = f.readlines()
    return topic_list


# 加载某个领域，主题下的分面
def get_facets(domain, topic, basepath='../dataset/domain_original_facets/'):
    with open(basepath + domain + '/' + topic + '.txt', 'r', encoding='utf-8') as f:
        j = json.load(f)
        return Topic(j)

# 直接表示的分面
def get_facets_directly(domain, topic, basepath='../dataset/domain_original_facets/'):
    with open(basepath + domain + '/' + topic + '.txt', 'r', encoding='utf-8') as f:
        list = f.readlines()
        facet_list = [l.strip() for l in list]
        return facet_list

# 获得主题序列字典
def get_topic_dict(domain):
    topic_dict = {}
    topic_index_dict = {}
    topic_list = get_topics_by_domain(domain)
    i = 0
    for topic in topic_list:
        if (topic.strip() == ''):
            continue
        topic_dict[topic.strip()] = i
        topic_index_dict[i] = topic.strip()
        i += 1
    return topic_dict, topic_index_dict


# 生成所需文件夹
def generate_dirs(domain):
    preprocess = ['A_deleteInherentFacets_list', 'B_getCentralWord', 'C_toLowerCase', 'D_deleteTopicFacet', 'E_deleteInitFacet', 'F_process_summary']
    algorithm = ['A_generateP', 'B_generateF', 'C_LP', 'D_analyse', 'E_performance']
    algorithm_new = ['A_generateP', 'B_partition', 'C_generateF', 'D_LP', 'E_analyse', 'F_performance']
    os.mkdir('../output/' + domain)
    os.mkdir('../output/' + domain + '/Algorithm/')
    os.mkdir('../output/' + domain + '/Algorithm_new/')
    os.mkdir('../output/' + domain + '/Algorithm_sxw/')
    os.mkdir('../output/' + domain + '/Analyse/')
    os.mkdir('../output/' + domain + '/Preprocess/')
    for p in preprocess:
        os.mkdir('../output/' + domain + '/Preprocess/' + p)

    for a in algorithm:
        os.mkdir('../output/' + domain + '/Algorithm/' + a)

    for a in algorithm_new:
        os.mkdir('../output/' + domain + '/Algorithm_new/' + a)
        os.mkdir('../output/' + domain + '/Algorithm_sxw/' + a)

# generate_dirs('Physical_chemistry')
