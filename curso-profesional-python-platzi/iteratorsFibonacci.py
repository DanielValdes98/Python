import time

class FiboIter():

    def __init__(self, max = 8):
        self.max = max

    #Define los metodos necesarios para que el iterador funcione
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max or self.counter <= self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.n1 = self.n2
                self.n2 = self.aux
                # self.n1, self.n2 = self.n2, self.aux #Esta linea es igual que las dos lineas de arriba
                self.counter += 1
                return self.aux
        else:
            raise StopIteration

if __name__ == "__main__":
    fibonacci = FiboIter() #Crea una instacia de la clase
    for element in fibonacci:
        print(element)
        time.sleep(.5) # Pausa 0.05s antes de seguir en la siguiente vuelta, porque el for es un bulce infinito


# Example simple or Iterator
## Creando un iterador
# my_list = [1,2,3,4,5]
# my_iter = iter(my_list)

## Interando in iterador
# while True:
#     try:
#         element = next(my_iter)
#         print(element)
#     except StopIteration:
#         break



