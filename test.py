class myTools:
    def __init__(self):
        self.a = 0

    def parse(self, str):
        list = str.split('|')
        result = []
        for e in list:
            x = e.split(',')[0]
            y = e.split(',')[1]
            result.append((int(x), int(y)))
        return result


