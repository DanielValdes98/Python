from datetime import datetime

# Example 1:
my_time = datetime.now()
today = datetime.today()
print(my_time)
print(today)
print(today.year)
print(today.month)
print(today.day)

my_datetime = datetime.now()
print(my_datetime)


# Example 2:
# strtime --> Recibe en formato de String la fecha
my_str = my_datetime.strftime('%d/%m/%Y')
print(f'FORMATO LATAM: {my_str}')

my_str = my_datetime.strftime('%M/%D/%Y')
print(f'FORMATO USA: {my_str}')

my_str = my_datetime.strftime('Estamos en el año %Y')
print(f'FORMATO RAMDOM: {my_str}')