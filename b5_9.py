import time

class LeadTimeFunc:
    '''Вычисляет среднее время выполнения функции
        input: LeadTimeFunc(функция)
        output: среднее время выполнения функции'''
    
    def __init__(self, func):
        self.number_of_launches = 1000
        self.func = func
        
    def __call__(self,*args, **kwargs):
        total_time = 0
        for i in range(1, self.number_of_launches):
            start = time.time()
            self.func(*args, **kwargs)
            end = time.time()
            total_time+=(end-start)
        average_time = total_time/self.number_of_launches
        print(f'среднее время выполнения функции за {self.number_of_launches} запусков: {average_time}')
        return self.func(*args, **kwargs)
@LeadTimeFunc
def fib(n):
    num = []
    a, b = 1, 2
    while b < n:
        c = a + b 
        a = b
        b = c
        num.append(a)
    return num
print(fib(1000))