basket = []

def add_product(name):
    if name not in basket:
        basket.append(name)

def remove_product(name):
    if name in basket:
        basket.remove(name)

def show_basket():
    print("კალათაშია:",basket)

add_product("ვაშლი")
add_product("ბანანი")
add_product("რძე")
add_product("შოკოლადი")
add_product("კოკაკოლა")
show_basket()

remove_product("ვაშლი")
show_basket()

