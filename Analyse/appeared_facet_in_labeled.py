# -*- coding:utf-8 -*-
import os


def appeared_facet_in_labeled(domain):
    result = []
    for root, dirs, files in os.walk('../dataset/labeled_facets/' + domain + '/'):
        for file in files:
            with open(root + file, 'r', encoding='utf-8') as f:
                facets = f.readlines()
                for f in facets:
                    if(f.strip() not in result):
                        if(f.strip() == 'algorithm'):
                            print(file)
                        result.append(f.strip())
    print('标注数据中出现的分面数：' , len(result))

    with open('../output/' + domain + '/Analyse/appeared_facet_in_labeled_data.txt', 'w', encoding='utf-8') as f:
        res = [r + '\n' for r in result]
        f.writelines(res)

appeared_facet_in_labeled('Physical_chemistry')

# dict = {}
# for root, dirs, files in os.walk('../output/Data_structure/Algorithm/D_analyse/'):
#     for file in files:
#         with open(root + file, 'r', encoding='utf-8') as f:
#             facets = f.readlines()
#             for f in facets:
#                 f = f.strip()
#                 if f in dict:
#                     dict[f] += 1
#                 else:
#                     dict[f] = 1
#
#
# a = sorted(dict.items(), key=lambda x: x[1], reverse=True)
#
# for items in a:
#     print(items[0])
def static(domain):
    sum_f = 0
    min_f = 666
    max_f = 0
    tps = 0
    for root, dirs, files in os.walk('../dataset/labeled_facets/' + domain + '/'):
        tps = len(files)
        for file in files:
            with open(root + file, 'r', encoding='utf-8') as f:
                flist = f.readlines()
                num = len(flist)
                if(num < 4):
                    print(file)
                if num < min_f:
                    min_f = num
                if num > max_f:
                    max_f = num
                sum_f += num

    print('max:', max_f)
    print('min:', min_f)
    print('avg:', sum_f / tps)

static('Algebraic_geometry')