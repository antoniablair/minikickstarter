class Backing():
    def __init__(self, name, project, card, amount):
        self.name = name
        self.project = project
        self.card = card
        self.amount = amount

    # def save(self):
    #     print u'Saving'
    #     try:
    #         with open(LOCAL_DATA, 'w') as db:
    #             db.write(string_from_data(self.name))
    #     except:
    #         print u'that did not work'

    def __str__(self):
        return u'{} - {}'.format(self.name, self.project)