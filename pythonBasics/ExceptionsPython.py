

ItemsInCart = 0
# 2 items will be added in cart

if ItemsInCart != 2:
    # raise Exception('Products in the cart is not matched')
    pass

assert(ItemsInCart == 0)

# try, catch --> except

try:
    with open('test.txt', 'r') as reader:
        reader.read()
except:
    print('Some how we reach this block because there is failure in try block')


try:
    with open('test.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print('Cleaning up resources')
