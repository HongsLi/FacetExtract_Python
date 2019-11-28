# -*- coding:utf-8 -*-
from Preprocess.A_deleteInherentFacets import useless_filter_list
from Preprocess.B_getCentralWord import get_central_word
from Preprocess.C_toLowerCase import to_lower_case
from Preprocess.D_deleteTopicFacet import delete_topic_facet
from Preprocess.E_deleteInitFacet import delete_init_facet
from Preprocess.F_process_summary import ProcessSummary


def preprocess(domain):
    # print('1. Get original facet')
    # all_appeared_facet(domain)
    print('2. Filter')
    useless_filter_list(domain)
    print('3. Get central words')
    get_central_word(domain)
    print('4. To lower case')
    to_lower_case(domain)
    print('5. Delete topic facet')
    delete_topic_facet(domain)
    print('6. Delete init facet')
    delete_init_facet(domain)
    print('Summary to matrix...')
    PS = ProcessSummary(domain)
    PS.generate_matrix()
    print('done')

preprocess('Computer_network')