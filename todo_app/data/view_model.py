import datetime
class ViewModel:
    def __init__(self, items):
        self._items = items
    @property
    def items(self): return self._items

    @property
    def to_do_items(self):
        todo = [item for item in self._items if item.status == "TODO ITEMS"]
        return todo
        
    @property
    def doing_items(self):
        return [item for item in self._items if item.status == "PENDING ITEMS"]

    @property
    def done_items(self):
        return [item for item in self._items if item.status == "DONE ITEMS"]

    @property
    def done_today(self):
        done = self.done_items
        today = datetime.date.today()
        return [item for item in done if item.update_time.date() == today]

    @property
    def done_older(self):
        done = self.done_items
        today = datetime.date.today()
        return [item for item in done if item.update_time.date() < today]

    @property
    def done_5today_older(self):
        print(len(self.done_items))
        if len(self.done_items) > 5:
            return self.done_older
        elif len(self.done_items) <= 5: 
            return self.done_today[0:5]
         