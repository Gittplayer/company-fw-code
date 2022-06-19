class Car:
    def __init__(self, name, length, width, high):
        self.name = name
        self.length = length
        self.width = width
        self.high = high

    def car_info(self):
        print(f"车名：{self.name}，长：{self.length}，宽：{self.width}，高：{self.high}")


class VW371(Car):
    def get_color(self, s):
        print(s)

    def _rice(self):
        if self.get_color == "gold" or "white":
            print(f"150000 元")
        else:
            print(f"120000 元")


if __name__ == '__main__':

    vw371 = VW371('速腾', '5', '2', '2')
    vw371.car_info()
    vw371.get_color("white")
    vw371._rice()
