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
        return [item for item in done if item.update_time == today]
         