import os.path
from hashlib import md5

TESTCASE_PREFIX = u'# testcase:'

class HashableDict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.iteritems())))

class UnitTestFactory(object):
    TESTCASE_FILENAME = 'unittests.py'

    def setupfile(self, filepaths):
        """
            Create a file with header imports etc
        """
        if not os.path.isfile(self.TESTCASE_FILENAME):
            imports_statements = set()
            with open(self.TESTCASE_FILENAME, 'a') as f:
                try:
                    for fp in filepaths:
                        functionpath, function_fn = os.path.split(fp)
                        imports_statements.add('from %s import *\n' % function_fn.replace('.py',''))
                    for imports_statement in imports_statements:
                        f.write('%s\n' % imports_statement)
                    f.write('import unittest\n')
                    f.write('class SimpleTest(unittest.TestCase):\n\n')
                except AttributeError:
                    print 'attribute err'

    def create_test_case_line(self, data, prefix=TESTCASE_PREFIX):
        """
            Open the unit test fn & write out a test case
        """
        with open(self.TESTCASE_FILENAME, 'a') as f:
            f.write("{0:s}{1:s}\n".format(prefix, data))
            test_hex = md5(data).hexdigest()[:6]
            data =eval(data)
            if isinstance(data['result'], float):
                data['testtype'] = 'assertAlmostEqual'
            elif isinstance(data['result'], int):
                data['testtype'] = 'assertEqual'
            elif isinstance(data['result'], dict):
                data['testtype'] = 'assertDictEqual'
            elif isinstance(data['result'], str):
                data['result'] = "'%s'" % data['result']
                data['testtype'] = 'assertEqual'
            elif isinstance(data['result'], object):
                # not supported
                return
            else:
                # unknown result type
                return

            testtemplate='    def test_%(testname)s(self):\n' \
                         '        self.%(testtype)s(%(fn)s(*%(args)s, **%(kwargs)s), %(result)s)\n\n'
            testcase = testtemplate % {'testname': '%s_%s' % (data['fn'], test_hex),
                                       'fn': data['fn'],
                                       'args': data['args'],
                                       'kwargs': data['kwargs'],
                                       'testtype': data['testtype'],
                                       'result': data['result'],
                                       }
            f.write(testcase)

    def read_test_file(self):
        """
            read out the data from comments
        """
        with open(self.TESTCASE_FILENAME, 'r') as f:
            data =self.extract_testcase_comments_from_file(f)
        return data

    def extract_testcase_comments_from_file(self, f):
        data = []
        for testcasedata in f:
            if testcasedata.startswith(TESTCASE_PREFIX):
                try:
                    casedata = testcasedata.replace(TESTCASE_PREFIX, '')
                    r = eval(casedata)
                    data.append(r)
                except SyntaxError:
                    print 'err:', testcasedata
        return data


class test_logger(object):

    def __init__(self, f):
        self.func = f
        self.data = {}
        self.filepath = []
        self.unittestfile = UnitTestFactory()

    def __call__(self, *args, **kwargs):
        function_name = self.func.__name__
        self.filepath.append(self.func.func_globals['__file__'])
        r = self.func(*args, **kwargs)
        if not args:
            args = ()
        if not kwargs:
            kwargs = {}
        try:
            kwargs = HashableDict(kwargs)
            self.data[function_name, args, kwargs] = r
        except:
            pass
        return r

    def __del__(self):
        try:
            self.unittestfile.setupfile(filepaths=self.filepath)
            data = self.unittestfile.read_test_file()
            for fn, args, kwargs in self.data:
                funct_result = self.data[fn, args, kwargs]
                r = {'fn': fn,
                     'args': args,
                     'kwargs': kwargs,
                     'result': funct_result
                     }
                funct_arg_sig = str(r)
                if eval(funct_arg_sig) not in data:
                    self.unittestfile.create_test_case_line(data=funct_arg_sig)
        except AttributeError:
            print 'running in a unit test, so no logging'
            return



