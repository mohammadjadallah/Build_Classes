class Indexer(str):
    """
        string properity: any string
        myFind: method behave as find method of the string class.
          It takes 3 parameter (sub, start "optional", end "optional")
          sub: a sub string that user want to find the index to.
          start: the start index that should the find method begin from.
          end: the end index that should the find method stop in. "Not Included"


    """
    def __init__(self, string):
        self.string = string

    def myFind(self, sub: str, start=None, end=None):
        try:
            if start is not None and end is not None:
                self.string = self.string[start:end]
                idx = 0
                for i in self.string:
                    if i == sub:
                        return idx
                    elif i == self.string[-1] and i != sub:
                        return -1

                    idx += 1
            else:
                idx = 0
                for i in self.string:
                    if i == sub:
                        return idx
                    elif i == self.string[-1] and i != sub:
                        return -1

                    idx += 1

        except Exception as e:
            return e

    def __repr__(self):
        return "myFind method of the Indexer class: A simple method that behave as find method of the string class in Python." \
               "\nif the substring that user want not found it return a -1 else it will return the index of the substring."


obj = Indexer("Hello")
print(repr(obj))
print(obj.__doc__)

# Testing myFind method
print(obj.myFind('e', start=0, end=3))
print(obj.myFind('o', start=0, end=3))
print(obj.myFind('q'))
