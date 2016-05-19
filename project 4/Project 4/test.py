def test(a):
    while True:
        print('Yes.')
        if a == 5:
            for i in range(a):
                if i == 4:
                    break
            break
                else:
                    print('not 4')


        else:
            break
    print('5')
test(4)
            
