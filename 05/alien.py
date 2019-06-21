alien_color=['green','yellow','red']
alien_color='red'
if alien_color == 'green':
    print("you get 5 point")
elif alien_color == 'blue':
    print("you get 2 point")
else:
    print("game over")
if alien_color:
    print("yes you did the right choice")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("add" + requested_topping)
    print("add finished")
else:
    print("you did not chooes any , do you like order a pizza?")
