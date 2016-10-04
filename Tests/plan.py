import ConfigParser


class Plan(object):
    def __init__(self):
        self.station_type = None
        self.station_name = None
        self.test_number = None
        self.plan = []

    def read(self):
        config = ConfigParser.ConfigParser()

        config.read('Tests/my_plan.cfg')
        for section in config.sections():
            if section == 'Globals':
                self.station_name = config.get(section, 'Name')
                self.station_type = config.get(section, 'Type')
            if section == 'Tests':
                num = zip(*config.items(section))[0]
                self.test_number = [x for x in num]
                tests = zip(*config.items(section))[1]
                self.plan = [x for x in tests]

if __name__ == '__main__':
    print 'Get file attributes'
    my_plan = Plan()
    my_plan.read()
    print 'test list {}'.format(my_plan.test_number)
    print 'test plan {}'.format(my_plan.plan)



