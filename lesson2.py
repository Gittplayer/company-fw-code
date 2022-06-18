class Car:
    def __init__(self, name, length, width, high):
        self.name = name
        self.length = length
        self.width = width
        self.high = high

    def car_info(self):
        print(f"车名：{self.name}，长：{self.length}，宽：{self.width}，高：{self.high}")


class VW371(Car):
    def _color(self, s):
        return s

    def _rice(self):
        if self._color == "gold" or "white":
            print(150000)
        else:
            print(120000)


# class Car_info_output:
#     def __init__(self):
#         self.cars = []
#
#     def add(self, car):
#         self.cars.append(car)
#
#     def info_output(self):
#         for car in self.cars:
#             car.car_info()


if __name__ == '__main__':
    car1 = Car('速腾', '5', '2', '2')
    car2 = Car('捷达', '5', '2', '2')
    carlist = []
    carlist.append(car1)
    carlist.append(car2)
    for i in carlist:
        i.car_info()
    # car1.car_info()
    # car2.car_info()
    # car_info_output = Car_info_output()
    # car_info_output.add(car1)
    # car_info_output.add(car2)
    # car_info_output.info_output()
    vw371 = VW371('速腾', '5', '2', '2')
    vw371.car_info()
    vw371._color("white")
    vw371._rice()
