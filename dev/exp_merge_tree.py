from lxml import etree
from copy import deepcopy

"""
This is an attempt to merge to XML trees.  It works but it probably doesn't do what you want because XML elements are not only identified
by their tag.  Take a POM for example, it will have many <dependency> nodes that are only distinguished by the text on their daughter
node 'GroupId'.  This code does not take that into account.
"""

def treeMerge(a, b):
    """Merge two xml trees A and B, so that each recursively found leaf element of B is added to A.  If the element
    already exists in A, it is replaced with B's version.  Tree structure is created in A as required to reflect the
    position of the leaf element in B.
    Given <top><first><a/><b/></first></top> and  <top><first><c/></first></top>, a merge results in
    <top><first><a/><b/><c/></first></top> (order not guaranteed)
    """

    def inner(aparent, bparent):
        for bchild in bparent:
            achild = aparent.xpath('./' + bchild.tag)
            if not achild:
                aparent.append(bchild)
            elif bchild.getchildren():
                inner(achild[0], bchild)

    res = deepcopy(a)
    inner(res, b)
    return res