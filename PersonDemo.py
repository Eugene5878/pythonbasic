class Person:

    def who_am_i(self, name, age, tel, address):    #self 자리에는 객체의 이름이 온다.
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person()
girl = Person()


boy.who_am_i('john',15,'123-4567','toronto')
girl.who_am_i('alice',13,'321-3212','new_york')

print(boy.name)
print(boy.age)
print(boy.tel)
print(boy.address)

print(girl.name)
print(girl.age)
print(girl.tel)
print(girl.address)


# 기본 예제

class Computer:

    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))

desktop = Computer()
desktop.set_spec('i7','16GB','GTX1060','512GB')
desktop.hardware_info()

desktop = Computer()
desktop.set_spec('i5','8GB','MX300','256GB')
desktop.hardware_info()