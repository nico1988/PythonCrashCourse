class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    def describe(self):
        print("the " + self.name.title() + " restaurant cusine_type is " + self.cuisine_type)
    def open_restaurant(self):
        print("the " + self.name.title() + " restaurant is opening")
kfc = Restaurant("kfc", "chinese")
mcdonald = Restaurant("mcdonald", "french")
xiangcai = Restaurant("liuyang", "xiangcai")
mcdonald.describe()
xiangcai.describe()
kfc.open_restaurant()
kfc.describe()
