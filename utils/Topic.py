# -*- coding:utf-8 -*-
import json
from utils.Facet import Facet


class Topic(object):
    def __init__(self, topic):
        self.name = topic['name']
        self.facets = self.create_facets(topic['facets'])
        self.original_topic = topic

    def create_facets(self, facets_list):
        facets = []
        if len(facets_list) == 0:
            return None
        for facet in facets_list:
            f = Facet(facet['name'], self.create_facets(facet['nextFacets']))
            facets.append(f)
        return facets

    # 将分面转化为字典
    def convert_to_dict(self, facets_list):
        facets = []
        if (facets_list == None):
            return []
        for facet in facets_list:
            if facet == None:
                continue
            if facet.get_name() == None:
                continue
            f = {'name': facet.get_name(), 'nextFacets': self.convert_to_dict(facet.get_nextFacets())}
            facets.append(f)
        return facets

    # 将分面列表转化为原本形式
    def to_dict(self):
        topic = {'name': self.name, 'facets': self.convert_to_dict(self.facets)}
        return topic

    # 对每个分面进行操作 递归访问每一个结点
    def operate_facets(self, facets, func):
        if facets == None:
            return None
        i = 0
        for facet in facets:
            if (facet == None):
                continue
            if (facet.get_name() == None):
                continue
            facets[i] = func(facet)
            if (facet == None):
                continue
            if (facet.get_name() == None):
                continue
            i += 1
            self.operate_facets(facet.get_nextFacets(), func)

    # 对主题-分面树下的每一个结点进行操作，返回值是每一个结点的新的facet。 相当于对每一个结点执行func(facet)。func是一个函数 参数是某个结点facet
    def operation(self, func):
        self.operate_facets(self.facets, func)

    # 将带有上下位关系的主题分面数写入txt
    def write_to_txt(self, path):
        with open(path + self.name + '.txt', 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f)

    def get_all_appeared_facet(self):
        facets = self.original_topic['facets'].copy()
        facets_list = []

        while (len(facets) != 0):
            facet = facets.pop()
            facets_list.append(facet['name'] + '\n')
            facets += facet['nextFacets']
        return facets_list