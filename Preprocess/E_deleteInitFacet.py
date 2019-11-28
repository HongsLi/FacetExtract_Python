# -*- coding:utf-8 -*-
import os
import utils.Utils as Utils

# 去除固有分面以及重复分面

def delete_init_facet(domain):
    for root, dirs, files in os.walk('../output/' + domain + '/Preprocess/D_deleteTopicFacet/'):
        for file in files:
            with open(root + file, 'r', encoding='utf-8') as f:
                facet_list = f.readlines()
                # 去掉空格和空行
                facet_list = [fl.strip() for fl in facet_list if fl.strip() != '']
                # 去重
                facet_list = list(set(facet_list))
                # 去掉固有分面
                if 'application' in facet_list:
                    facet_list.remove('application')
                if 'property' in facet_list:
                    facet_list.remove('property')
                if 'example' in facet_list:
                    facet_list.remove('example')
                if 'definition' in facet_list:
                    facet_list.remove('definition')

                processedf = open('../output/' + domain + '/Preprocess/E_deleteInitFacet/' + file, 'w', encoding='utf-8')

                # 加上空格
                facet_list = [fl+'\n' for fl in facet_list]
                processedf.writelines(facet_list)

delete_init_facet('Physical_chemistry')