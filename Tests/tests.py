from abc import ABCMeta, abstractmethod
from collections import defaultdict

import re

pattern = '(\d)(-)(\w+)'

class TestPlan(object):
    def __init__(self):
        print 'creating the tests'
        self.test_steps = []

    def register_test(self, test):
        self.test_steps.append(test)

    def start(self):
        pass

    def run(self):
        pass

    def cleanup(self):
        pass


class Test(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


class Voltage(Test):
    def __init__(self, parent_test):
        self.parent_test = parent_test
        self.parent_test.register_test(self)

    def start(self):
        print 'setup voltage'

    def run(self):
        print 'running voltage test'

    def cleanup(self):
        print 'close voltage test'


class Audio(Test):
    def __init__(self, parent_test):
        self.parent_test = parent_test
        self.parent_test.register_test(self)

    def start(self):
        print 'setup audio'

    def run(self):
        print 'running audio test'

    def cleanup(self):
        print 'close audio test'


class SelfTest(Test):
    def __init__(self, parent_test):
        self.parent_test = parent_test
        self.parent_test.register_test(self)

    def start(self):
        print 'setup SelfTest'

    def run(self):
        print 'running SelfTest test'

    def cleanup(self):
        print 'close SelfTest test'


class OOB(Test):
    def __init__(self, parent_test):
        self.parent_test = parent_test
        self.parent_test.register_test(self)

    def start(self):
        print 'setup OOB'

    def run(self):
        print 'running OOB test'

    def cleanup(self):
        print 'close OOB test'


class InBand(Test):
    def __init__(self, parent_test):
        self.parent_test = parent_test
        self.parent_test.register_test(self)

    def start(self):
        print 'setup InBand'

    def run(self):
        print 'running InBand test'

    def cleanup(self):
        print 'close InBand test'


class DVR(Test):
    def __init__(self, parent_test):
        self.parent_test = parent_test
        self.parent_test.register_test(self)

    def start(self):
        print 'setup DVR'

    def run(self):
        print 'running DVR test'

    def cleanup(self):
        print 'close DVR test'


class Sata(Test):
    def __init__(self, parent_test):
        self.parent_test = parent_test
        self.parent_test.register_test(self)

    def start(self):
        print 'setup Sata'

    def run(self):
        print 'running Sata test'

    def cleanup(self):
        print 'close Sata test'


class Recording(Test):
    def __init__(self, parent_test):
        self.parent_test = parent_test
        self.parent_test.register_test(self)

    def start(self):
        print 'setup Recording'

    def run(self):
        print 'running Recording test'

    def cleanup(self):
        print 'close Recording test'


class Diagnostics(Test):
    def __init__(self, parent_test):
        self.parent_test = parent_test
        self.parent_test.register_test(self)

    def start(self):
        print 'setup Diagnostics'

    def run(self):
        print 'running Diagnostics test'

    def cleanup(self):
        print 'close Diagnostics test'


class HDD(Test):
    def __init__(self, parent_test):
        self.parent_test = parent_test
        self.parent_test.register_test(self)

    def start(self):
        print 'setup HDD'

    def run(self):
        print 'running HDD test'

    def cleanup(self):
        print 'close HDD test'


class RunTests(object):
    def __init__(self, all_tests):
        steps = defaultdict()
        print 'initialize objects here'
        plan = TestPlan()
        for test in all_tests:
            set = re.search(pattern, test)
            test_name = set.groups()[2]

            steps[test_name] = eval(test_name)
            steps[test_name](plan)

    def run_all(self):
        print 'start running each test'

    def end(self):
        print 'close instruments'