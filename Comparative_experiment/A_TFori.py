# -*- coding:utf-8 -*-
import utils.Utils as Utils


def performance(domain):
    # 混淆矩阵
    P = 0
    R = 0
    F1 = 0

    TP = 0
    FN = 0
    FP = 0
    # 没有TN
    topic_list = Utils.get_topics_by_domain(domain)
    for topic in topic_list:
        p = 0
        r = 0
        f1 = 0

        tp = 0
        fn = 0
        fp = 0

        # 默认实验结果
        with open('../output/' + domain + '/Preprocess/E_deleteInitFacet/' + topic.strip() + '.txt', 'r',
                  encoding='utf-8') as model_data:
            model_facet_list = model_data.readlines()

        # 师姐的实验结果
        # with open('F:\\分面生成\\数据集\\Facet\\Data_structure\\experiment\\result\\' + topic.strip() + '.txt', 'r',
        #           encoding='utf-8') as model_data:
        #     model_facet_list = model_data.readlines()

        model_facet_list = [m.strip() for m in model_facet_list]

        # 师姐的标注数据
        with open('../dataset/labeled_facets/' + domain + '/' + topic.strip() + '.txt', 'r',
                  encoding='utf-8') as labeled_data:
            labeled_facet_list = labeled_data.readlines()

        # 合并的标注数据
        # with open('../output/' + domain + '/Analyse/merge_labeled_data/' + topic.strip() + '.txt', 'r',
        #           encoding='utf-8') as labeled_data:
        #     labeled_facet_list = labeled_data.readlines()

        labeled_facet_list = [l.strip() for l in labeled_facet_list]

        flag = True
        for m in model_facet_list:
            for l in labeled_facet_list:
                if(l.find(m) != -1 or m.find(l) != -1):
                    tp += 1
                    flag = False
                    break
                # elif(m == 'history'):
                #     tp += 1
                #     flag = False
                #     break
            if(flag):
                fp += 1
            flag = True

        flag = True
        for l in labeled_facet_list:
            for m in model_facet_list:
                if l.find(m) != -1:
                    flag = False
                    break
            if(flag):
                fn += 1
            flag = True
        p = tp / (len(model_facet_list) + 0.001)
        r = tp / (len(labeled_facet_list))
        f1 = 2*p * r / (p + r + 0.001)

        P += p
        R += r
        F1 += f1

        TP += tp
        FP += fp
        FN += fn

    P = P / len(topic_list)
    R = R / len(topic_list)
    F1 = 2 * P * R / (P + R)

    print('domain: ', domain)
    print('P:', P)
    print('R:', R)
    print('F1:', F1)
    print('TP:', TP)
    print('FP:', FP)
    print('FN:', FN)

    with open('../output/' + domain + '/Algorithm_new/F_performance/result.txt', 'w', encoding='utf-8') as f:
        f.writelines(['P: ', str(P) + '\n', 'R: ', str(R) + '\n', 'F1: ', str(F1) + '\n'])

performance('Data_structure_new')