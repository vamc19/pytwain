import unittest
from six.moves import tkinter


class MyTestCase(unittest.TestCase):
    def test_dsm(self):
        import twain
        root = tkinter.Tk()
        root.title('scan.py')
        with twain.SourceManager(root) as sm:
            ds_name = sm.source_list[0]
            with sm.open_source(str(ds_name)) as ds:
                pass
