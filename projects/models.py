class Project():
    def __init__(self, name, target):
        self.name = name
        self.target = target

    # def save(self):
    #     print u'Saving'
    #     try:
    #         with open(LOCAL_DATA, 'w') as db:
    #             db.write(string_from_data(self.name))
    #     except:
    #         print u'that did not work'

    def __str__(self):
        return self.name