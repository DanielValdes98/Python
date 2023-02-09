#  Es lo mismo que un iterador, pero más sencillo y practico. Se pueden guardar secuencias infinitas

# Example 1:

def my_gen():
    """Un ejemplo de generadores"""
    print ("Hello world!")
    n = 0
    yield n

    print("Hello heaven!")
    n = 1
    yield n

    print( "Hello hell!")
    n = 2
    yield n

a=  my_gen()
print(next(a)) #Hello world!
print(next(a)) #Hello heaven!
print(next(a)) #Hello hell!
print(next(a)) #StopIteration


# Example 2:

#Generator expressions
my_list = [0,1,4,7,9,10]

my_second_list = [x*2 for x in my_list] #List comprehesion: Problema es que guarda en memoria, si es una lista grande el programa seria muy pesado
my_second_gen = (x*2 for x in my_list) #Generator comprehesion

