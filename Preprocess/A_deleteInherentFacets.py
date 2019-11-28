# -*- coding:utf-8 -*-
import utils.Utils as Utils
import os
import utils.consts as consts

stop_save_words = ["see also", "references", "external links", "further reading", "vs.", "citations", 'notes']
# useless_words = ["overview", "bibliography", "other", "type", "types", "case", "class", "summary", 'papers']
useless_words = ["overview", "bibliography", "other", "case", "class", "summary", 'papers']

def delete(facet):
    for w in stop_save_words:
        if(facet.get_name().lower().find(w) != -1):
            return None
    for w in useless_words:
        if (facet.get_name().lower().find(w) != -1):
            return None
    return facet

def useless_filter(domain):
    # 领域主题词列表
    topic_list = Utils.get_topics_by_domain(domain)
    for topic in topic_list:
        # 获得原始分面
        topic = topic.strip()
        original_facets = Utils.get_facets(domain, topic)
        original_facets.operation(delete)

        original_facets.write_to_txt(consts.BASE_PATH + domain + '/Preprocess/A_deleteInherentFacets/')


def useless_filter_list(domain):
    topic_list = Utils.get_topics_by_domain(domain)
    for topic in topic_list:
        topic = topic.strip()
        path = '../output/' + domain + '/Preprocess/A_allAppearedFacet/'
        if os.path.exists(path):
            with open('../output/' + domain + '/Preprocess/A_allAppearedFacet/' + topic + '.txt', 'r', encoding='utf-8') as f:
                facet_list = f.readlines()
        else:
            with open('../dataset/domain_original_facets/' + domain + '/' + topic + '.txt', 'r', encoding='utf-8') as f:
                facet_list = f.readlines()
        remove_list = []
        for facet in facet_list:
            for w in stop_save_words:
                if(facet.lower().find(w) != -1):
                    remove_list.append(facet)
            for w in useless_words:
                if(facet.lower().find(w) != -1):
                    remove_list.append(facet)
        remove_list = list(set(remove_list))
        for r in remove_list:
            facet_list.remove(r)
        with open('../output/' + domain + '/Preprocess/A_deleteInherentFacets_list/' + topic + '.txt', 'w',
                  encoding='utf-8') as f:
            f.writelines(facet_list)



useless_filter_list('Physical_chemistry')


