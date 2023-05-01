def hi_decorator(func):
    #warper
    def iner():
        print('after')
        func()
        print('next')
    return iner

# @hi_decorator
def hi_word():
     print('hi word')
print('-----------------')

#hi_word()
new = hi_decorator(hi_word)

new() 