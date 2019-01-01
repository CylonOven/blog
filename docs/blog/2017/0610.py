import random

random.seed("lel")

class table(object):

    changes= {
        '1':"@",
        '0':" "
    }

    def __init__(self, lists):
        self.data = lists
    @classmethod
    def gen_matix(cls, x, y):
        return cls(
            [
        [random.choice((1,0)) for y in range(y)] for x in range(x)
            ])


    def __str__(self):
        output = []
        width = len(self.data[0])
        output.append("+" + "-"* width + "+\n")
        for row in self.data:
            output.append("|")
            for e in row:
                output.append(self.changes[e])
            output.append("|\n")
        output.append("+" + "-" * width + "+\n")


t = table.gen_matix(10,10)
print(t)