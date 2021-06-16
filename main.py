from icon_search.icon_search import IconSearch
from icon_search.consts import CATEGORYS


import time
th = []
if __name__ == '__main__':
    start_time = time.time()
    for category in CATEGORYS:
        t = IconSearch(category=category)
        t.start()
        th.append(t)

for x in th:
    x.join()
    
print("--- %s seconds --- of total" % (time.time() - start_time))

    