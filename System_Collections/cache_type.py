import time


class BackingStore:
    def __init__(self):
        self.data = []

    def write(self, datum):
        print('Started writing to backing store.')
        time.sleep(2)  # Writing to disk is slow
        self.data.append(datum)
        print('Finished writing to backing store.')

    def read(self, index):
        print('Started reading from backing store.')
        time.sleep(2)  # Reading from disk is slow
        print('Finished reading from backing store.')
        return self.data[index]


class Cache:
    def __init__(self):
        self.data = []

    def write(self, datum):
        print('Started writing to cache.')
        self.data.append(datum)
        print('Finished writing to cache.')

    def read(self, index):
        print('Started reading from backing store.')
        print('Finished reading from backing store.')
        return self.data[index]




def write_through(cache, backing_store, datum):
    cache.write(datum)
    backing_store.write(datum)


def write_around(backing_store, datum):
    backing_store.write(datum)


def write_back(cache, datum):
    cache.write(datum)




if __name__ == '__main__':
    backing_store = BackingStore()
    cache = Cache()
    datum = 'Yutong'


    write_through(cache=cache, backing_store=backing_store, datum=datum)
    write_around(backing_store=backing_store, datum=datum)
    write_back(cache=cache, datum=datum)