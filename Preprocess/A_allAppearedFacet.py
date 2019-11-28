# -*- coding:utf-8 -*-
import utils.Utils as Utils
# 这个文件是测试用的，用来读入师姐定义的分面结构的文件

def all_appeared_facet(domain):
    # 领域主题词列表
    topic_list = Utils.get_topics_by_domain(domain)
    for topic in topic_list:
        # 获得原始分面
        topic = topic.strip()
        original_facets = Utils.get_facets(domain, topic)
        facet_list = original_facets.get_all_appeared_facet()
        with open('../output/' + domain + '/Preprocess/A_allAppearedFacet/' + topic + '.txt', 'w', encoding='utf-8') as f:
            f.writelines(facet_list)




# 这个函数是写着玩的
def get_percent(domain):
    topic_list = Utils.get_topics_by_domain(domain)
    for topic in topic_list:
        # 获得原始分面
        topic = topic.strip()
        with open('../output/' + domain + '/Preprocess/E_deleteInitFacet/' + topic + '.txt', 'r', encoding='utf-8') as f:
            origin_num = len(f.readlines())

        with open('../dataset/labeled_facets/' + domain + '/' + topic + '.txt', 'r', encoding='utf-8') as f:
            labeled_num = len(f.readlines())
        print(topic, (labeled_num - origin_num)/(origin_num + 1))


all_appeared_facet('Data_structure')