def greet_user(msg):
    print(msg)
greet_user("hello, this is nico")
# 缺省参数
def test(flag, *args):
    print("flag:" + flag)
    for value in args:
        print("value: " + value)
test("f11", "f2","f3","f4")
def describe_cats(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    return "nico"
describe_cats(animal_type='hamster', pet_name='harry')
describe_cats(pet_name='harry',animal_type='hamster')
return_value = describe_cats(pet_name='harry',animal_type='hamster')
print("函数返回值: " + return_value)

# 关键字实参
def cheeseshop(kind, *arguments, **keywords):
    print(cheeseshop.__annotations__)
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 100)  # 原来可以这么打印一条横线
    for kw in keywords:
        print(kw, ":", keywords[kw])
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def concat(*args, seq="/"):
    return seq.join(args)
path = concat("earch","sun","mars")
print(path)