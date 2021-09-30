print("Hello my world")
#using try except and exception to handle errors

def boxPrint(symbol,width,height):
    if len(symbol)!=1:
        raise Exception('Length of symbol should be exactly equal to 1')
    if height<2:
        raise Exception('Height should be greater than 2')
    if width<2:
        raise Exception('width should be greater than 2')

    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' '*(width-2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym,w,h)
    except Exception as err:      #err = exception   as object
        print('An exception happened:' + str(err))