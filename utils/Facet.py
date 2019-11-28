# -*- coding: utf-8 -*-


# 主题下的一个分面
class Facet(object):

    def __init__(self, name, nextFacets):
        self.name = name
        self.nextFacets = nextFacets

    def get_name(self):
        return self.name

    def get_nextFacets(self):
        return self.nextFacets

    def set_nextFacets(self, nf):
        self.nextFacets = nf