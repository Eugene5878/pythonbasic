# class Candy:
    
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color

class Candy:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

# satang = Candy()
# satang.set_info('circle','brown')

satang = Candy('circle','brown')

print(satang.shape)
print(satang.color)


class Sample:
    def __del__(self):
        print('인스턴스가 소멸됩니다.')

sample = Sample()
del sample

#제출

class Service:

    def __init__(self, service):
        self.service = service
        print('{} Service가 시작되었습니다'.format(self.service))

    def __del__(self):
        print('{} Service가 종료되었습니다'.format(self.service))

s = Service('길 안내')
del s