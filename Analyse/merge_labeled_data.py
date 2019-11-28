# -*- coding:utf-8 -*-
import os
import utils.Utils as Utils

def merge_labeled_data(domain):

    topic_list = Utils.get_topics_by_domain(domain)

    for topic in topic_list:
        topic = topic.strip()
        with open('../output/' + domain + '/Preprocess/E_deleteInitFacet/' + topic + '.txt', 'r', encoding='utf-8') as init_f:
            init_facets = init_f.readlines()
        with open('../dataset/labeled_facets/' + domain + '/' + topic + '.txt', 'r', encoding='utf-8') as labeled_f:
            labeled_facets = labeled_f.readlines()

        final_labeled_list = []
        for f in init_facets:
            final_labeled_list.append(f.strip())

        for f in labeled_facets:
            f = f.strip()
            if(f not in final_labeled_list):
                final_labeled_list.append(f)

        final_labeled_list = [f + '\n' for f in final_labeled_list]

        with open('../output/' + domain + '/Analyse/merge_labeled_data/' + topic + '.txt', 'w', encoding='utf-8') as file:
            file.writelines(final_labeled_list)

merge_labeled_data('Data_structure')