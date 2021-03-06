class Korean: 
    country = 'korea'

    @staticmethod
    def slogan():
        print('Imagine your Korea')

Korean.slogan()
print(Korean.country)    # 변수이므로 print를 넣어줘야함.


# 282p.

class Bag:

    count = 0

    def __init__(self):
        Bag.count += 1

    @classmethod
    def sell(cls):
        cls.count -= 1

    @classmethod
    def remain_bag(cls):
        return cls.count

print('현재 가방: {}개'.format(Bag.remain_bag()))
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print('현재 가방: {}개'.format(Bag.remain_bag()))
bag1.sell()
bag2.sell()
print('현재 가방: {}개'.format(Bag.remain_bag()))