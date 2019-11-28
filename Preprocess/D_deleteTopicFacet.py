# -*-coding:utf-8 -*-

import utils.Utils as Utils
from nltk.stem.wordnet import WordNetLemmatizer

def contains_topic(facet, topic_list):
    for t in topic_list:
        if(facet.find(t) != -1):
            return True
        else:
            return False

def delete_topic_facet(domain):
    topic_list = Utils.get_topics_by_domain(domain)
    search_topic_list = [t.replace('_', ' ').strip() for t in topic_list]
    length = len(topic_list)
    index = 0
    for topic in topic_list:
        index += 1
        print('analysing: ', index, ' of ', length)
        topic = topic.strip()
        with open('../output/' + domain + '/Preprocess/C_toLowerCase/' + topic + '.txt', 'r',
                  encoding='utf-8') as f:
            facet_list = f.readlines()
            remove_list = []

            for facet in facet_list:
                if contains_topic(facet, search_topic_list):
                    remove_list.append(facet)

            for r in remove_list:
                facet_list.remove(r)

            file = open('../output/' + domain + '/Preprocess/D_deleteTopicFacet/' + topic + '.txt', 'w', encoding='utf-8')
            file.writelines(facet_list)
            file.close()

delete_topic_facet('Physical_chemistry')
