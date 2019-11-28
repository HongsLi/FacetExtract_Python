# -*- coding:utf-8 -*-
import utils.Utils as Utils
import nltk


def change_bad_word(word):
    word = word.lower()
    if (word.find("advantage") != -1):
        return "property"
    if (word.find("performance") != -1):
        return "property"
    if (word.find("efficiency") != -1):
        return "property"
    if (word.find("characterization") != -1):
        return "property"
    if (word.find("analysis") != -1):
        return "property"
    if (word.find("comparison") != -1):
        return "property"
    if (word.find("implemantation") != -1):
        return "implementation"
    if (word.find("implemantations") != -1):
        return "implementation"
    if (word.find("language support") != -1):
        return "implementation"
    if (word.find("pseudocode") != -1):
        return "implementation"
    if (word.find("usage") != -1):
        return "application"
    if (word.find("using") != -1):
        return "application"
    if (word.find("use") != -1):
        return "application"
    if (word.find("description") != -1):
        return "definition"
    if (word.find("algorithm") != -1):
        return "method"
    if (word.strip() == "concept"):
        return "definition"
    return word


def get_central_word(domain):
    # preps = ["of", "for", "at", "in", "on", "over", "to", "by", "about", "under", "after"]

    topic_list = Utils.get_topics_by_domain(domain)
    length = len(topic_list)
    index = 0
    for topic in topic_list:
        index += 1
        print('analysing: ', index, ' of ', length)
        topic = topic.strip()
        with open('../output/' + domain + '/Preprocess/A_deleteInherentFacets_list/' + topic + '.txt', 'r',
                  encoding='utf-8') as f:
            facet_list = f.readlines()
            new_list = []
            for facet in facet_list:
                facet = facet.lower()
                # facet = ''.join(f for f in facet if f not in [':', ',', '(', ')'])
                tokens = nltk.word_tokenize(facet)
                if (len(tokens) == 1):
                    pos_tags = nltk.pos_tag(tokens)
                    if (pos_tags[0][1].startswith('NN') and (len(tokens[0]) > 1)):
                        new_list.append(change_bad_word(tokens[0]) + '\n')
                else:
                    central_facet = ''
                    pos_tags = nltk.pos_tag(tokens)
                    record = False
                    for word in pos_tags:
                        if word[1].startswith('JJ'):
                            record = True
                            continue
                        if (record and word[1] == 'IN'):
                            break

                        if (word[1].startswith('NN') and not record):
                            record = True

                        if (record and word[1] in [':', ',', '(', ')', '#']):
                            break

                        if (record):
                            # central_facet += (word[0] + ' ')
                            central_facet = word[0]  # 只提取一个中心词

                    if central_facet != '' and len(central_facet) > 1:
                        central_facet = central_facet.strip()
                        new_list.append(change_bad_word(central_facet) + '\n')

            file = open('../output/' + domain + '/Preprocess/B_getCentralWord/' + topic + '.txt', 'w', encoding='utf-8')
            file.writelines(new_list)
            file.close()


get_central_word('Physical_chemistry')
