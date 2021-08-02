class Korean:
    country = "korea"    # 클래스변수를 객체가 공유한다.

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

man = Korean('Hong', 35, 'seoul')
woman = Korean('park', 16, 'daegu')
# korean.name
print(man.name)    # 객체 변수
print(Korean.country)    # 클래스 변수
print(woman.country)


class Korean:
    country = "korea"

    @classmethod
    def trip(cls, country):
        if cls.country == country:
            print('domestic')
        else:
            print('abroad')

Korean.trip('korea')
Korean.trip('USA')

