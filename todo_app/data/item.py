import dateutil.parser
class TrelloItem: 

    def __init__(self, id, status, title, update_time): 
        self.id = id
        self.status = status
        self.name = title
        self.update_time = dateutil.parser.parse(update_time)
        