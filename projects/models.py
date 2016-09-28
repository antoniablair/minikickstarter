class Project():
    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.backers = {}
        self.currently_raised = 0.0

    def funds_needed(self):
        print 'inside funds_needed'
        sum = float(self.target) - float(self.currently_raised)
        print sum
        return sum

    # def save(self):
    #     print u'Saving'
    #     try:
    #         with open(LOCAL_DATA, 'w') as db:
    #             db.write(string_from_data(self.name))
    #     except:
    #         print u'that did not work'

    def __str__(self):
        return self.name
