d = {'Hamburguesa': 12000, 'Coca cola': 2500}
it = d.items()
print(it)             #dict_items([('Hamburguesa', 12000), ('Coca cola', 2500)])
print(list(it))       #[('Hamburguesa', 12000), ('Coca cola', 2500)]
print(list(it)[0][0]) #Hamburguesa