from tqdm import tqdm

class StatusBar:
    
    def __init__(self):
        self.status_bar()
    
    def status_bar(self):
        loop = tqdm(total = 3000, position=0, leave=False)
        for k in range(3000):
            loop.set_description("Loading...".format(k))
            loop.update(1)
        loop.close()