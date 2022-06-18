class Car:
    def __init__(self, type, length, width, high, color, production_date):
        self.type = type
        self.length = length
        self.width = width
        self.high = high
        self.color = color
        self.production_date = production_date
    
    def car_info(self):
        print(
            f"车型：{self.type}，长：{self.length}，宽：{self.width}，高：{self.high}，颜色：{self.color}，生产日期：{self.production_date}")

class Car_info_output:
    def __init__(self):
        self.cars = []
      
    def add(self, car):
        self.cars.append(car)

    def info_output(self):
        for car in self.cars:
            car.car_info()


vw371 = Car('速腾', '5', '2', '2', '红色', '202220618')
vw311 = Car('捷达', '5', '2', '2', '黑色', '202220618')
vw471 = Car('迈腾', '5', '2', '2', '白色', '202220618')
car_info_output = Car_info_output()
car_info_output.add(vw371)
car_info_output.add(vw311)
car_info_output.add(vw471)
car_info_output.info_output()
