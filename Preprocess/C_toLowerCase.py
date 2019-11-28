# -*-coding:utf-8 -*-

import utils.Utils as Utils
from nltk.stem.wordnet import WordNetLemmatizer


# 大写变小写 复数变单数
def to_lower_case(domain):
    topic_list = Utils.get_topics_by_domain(domain)
    length = len(topic_list)
    index = 0
    lmtzr = WordNetLemmatizer()
    for topic in topic_list:
        index += 1
        print('analysing: ', index, ' of ', length)
        topic = topic.strip()
        with open('../output/' + domain + '/Preprocess/B_getCentralWord/' + topic + '.txt', 'r',
                  encoding='utf-8') as f:
            facet_list = f.readlines()
            new_list = []
            for facet in facet_list:
                facet = facet.lower().strip()
                facet = ' '.join([lmtzr.lemmatize(w, pos='n') for w in facet.split(' ')])
                new_list.append(facet.strip() + '\n')

            file = open('../output/' + domain + '/Preprocess/C_toLowerCase/' + topic + '.txt', 'w', encoding='utf-8')
            file.writelines(new_list)
            file.close()

to_lower_case('Physical_chemistry')