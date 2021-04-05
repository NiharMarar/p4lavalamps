
#1: setting up the class
class Books:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0 or series > 6:
            raise ValueError("Series must be between 0 and 6")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.book_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);


    #2 defining your series
    """Algorithm for building book series list, this id called from __init__"""
    def book_series(self):
        limit = self._series
        f = [(random.sample((booklist1), k=3))]
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -= 1


    #3: function to set data
    """Method/Function to set data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1


    #4: creating our getters
    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]



#5: creating our objects and values + testing
if __name__ == "__main__":
    '''Value for testing'''
    a = 3
    '''Constructor of Class object'''
    bookrecs = Books(a/a)
    print(f"Here are some book recomendations = {bookrecs.list}")





#class FibonacciSeries:
#def __init__(self, series):
#if series < 2 or series > 100:
#raise ValueError("Must be between 2 and 100")
#self._series = series
#self._list = []
#self._dict = {}
#self._dictID = 0
#self.calculate_series()

#def calculate_series(self):
#limit = self._series
#f = [0, 1]
#while limit > 0:
#self.set_data(f[0])
#f = [f[1], f[0] + f[1]]
#limit -= 1

#def set_data(self, num):
#self._list.append(num)
#self._dict[self._dictID] = self._list.copy()
#self._dictID += 1

#@property
#def series(self):
#return self._series

#@property
#def list(self):
#return self._list

#@property
#def number(self):
#return self._list[self._dictID - 1]

#def get_sequence(self, nth):
#return self._dict[nth]

#if __name__ == "__main__":
#n = 69
#fibonacci = FibonacciSeries(n)
#print(f"Fibonacci number for {n} = {fibonacci.number}")
#print(f"Fibonacci series for {n} = {fibonacci.list}")
#for i in range(n):
#print(f"Fibonacci sequence {i + 1} = {fibonacci.get_sequence(i)}")
