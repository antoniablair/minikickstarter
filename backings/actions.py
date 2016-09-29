from utils import *

def back_project(backer, project_name, card, price):
    """back <given name> <project> <credit card number> <backing amount>"""
    project = fetch_project(project_name)

    CARD_ERROR = paint.red(u'Please enter a correct credit card number.')

    # format numbers (move)
    # if project is None or not card_is_correct(card):
    if project is None:
        return

    project.currently_raised = float(project.currently_raised)
    project.target = float(project.target)
    card = float(card)
    price = float(price)

    if float(card).is_integer():
        card = int(card)
    else:
        print CARD_ERROR
        return

    if not card_is_correct(card):
        print CARD_ERROR
        return

    # # Todo: Move into a check parameters function
    else:
        backings = [b for b in BACKING_LIST if b.project == project_name and b.card == card]
        print 'BACKINGS -------'
        print backings
        print BACKING_LIST
        print '//////'
        if len(backings):
            print paint.red(u'This card has already been used to back this project.')
            return

        else:
            new_backing = Backing(backer, project_name, card, price)
            BACKING_LIST.append(new_backing)
            # new_backing.save()
            project.currently_raised = project.currently_raised + price
            # new_funds_needed = funds_needed - price

            # Update project
            # project.funds_needed = new_funds_needed
            # todo: delete this?
            project.backers[backer] = price

            print paint.green(u'This project has now raised ${}.'.format(project.currently_raised))
            print project.target
            print type(project.target)
            if project.currently_raised >= project.target:
                print paint.green(u'Congratulations on reaching your funding goal!')
            # todo: save project here

#     Todo: Finish this