class Entry:
    
    def __init__(self, value, weight = 1):
        
        self.weight, self.value = weight, value
        
    def set_weight(self, weight):
        
        self.weight = weight
        
    def set_value(self, newValue):
        
        if self.value != "Bin": self.value = newValue
        
    def incr_weight(self, incr = 1):
        
        self.weight += incr
        
    def get_weight(self):
        
        return self.weight

class Sample:
    
    def __init__(self, size = 1):
        
        self.size = size
        
        self.nullEntry = Entry(value = "Bin")
        
        self.sample = [self.nullEntry]
        
        self.count = 0
        
    def new_draw(self, draw):
        
        if not self._is_full():
            
            self.sample.append(Entry(value = draw))
            
        else:
            
            self.choose_random_entry().set_value(draw)
            
            self.nullEntry.incr_weight()
            
    def choose_random_entry(self):
        
        totalWeight = sum([x.get_weight() for x in self.sample])
        
        return choice(self.sample, p = map(lambda x: x.get_weight()/totalWeight, self.sample))
    
    def _is_full(self):
        
        return len(self.sample) >= self.size + 1
