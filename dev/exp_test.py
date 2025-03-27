import unittest

class Test_TreeMerge(unittest.TestCase):
    def test_level_zero(self):
        a = etree.fromstring("""<top></top>""")
        b = etree.fromstring("""<top2></top2>""")
        #result = donkey.treeMerge(a, b)

        # should give us an error

    def test_level_one(self):
        a = etree.fromstring("""<top><a/><b/><d><d2/></d></top>""")
        b = etree.fromstring("""<top><c/></top>""")
        result = donkey.treeMerge(a, b)

        self.assertEqual(len(result.xpath("/top")[0]), 4)
        self.assertEqual(len(result.xpath("/top/d/d2")), 1)

    def test_no_duplicates(self):
        a = etree.fromstring("""<top><a/></top>""")
        b = etree.fromstring("""<top><a/></top>""")
        result = donkey.treeMerge(a, b)

        self.assertEqual(len(result.xpath("/top")[0]), 1)

    def test_level_two(self):
        a = etree.fromstring("""<top><a/><b><b1/></b></top>""")
        b = etree.fromstring("""<top><b><b2/></b></top>""")
        result = donkey.treeMerge(a, b)
        print(etree.tostring(result))
        self.assertEqual(len(result.xpath("/top/a")), 1)
        self.assertEqual(len(result.xpath("/top/b/b1")), 1)
        self.assertEqual(len(result.xpath("/top/b/b2")), 1)

    def test_level_three(self):
        a = etree.fromstring("""<top><a/><b><b1><b11/><b22/></b1></b></top>""")
        b = etree.fromstring("""<top><a/><b><b1><b12/><b22/></b1></b></top>""")
        result = donkey.treeMerge(a, b)
        print(etree.tostring(result))
        self.assertEqual(len(result.xpath("/top/a")), 1)
        self.assertEqual(len(result.xpath("/top/b/b1/b11")), 1)
        self.assertEqual(len(result.xpath("/top/b/b1/b12")), 1)
        self.assertEqual(len(result.xpath("/top/b/b1/b22")), 1)

    def test_replaces_same_named_child(self):
        a = etree.fromstring("""<top><b foo=1></top>""")
        b = etree.fromstring("""<top><b foo=2></top>""")
        result = donkey.treeMerge(a, b)
        print(etree.tostring(result))
        self.assertEqual(len(result.xpath("/top/b[@foo=1]")), 0)
        self.assertEqual(len(result.xpath("/top/b[@foo=2]")), 1)


    def deal_with_namespaces(self):
        pass