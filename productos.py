tabla=["tabla", "1", 1000, 2]
soporte=["soporte", "2", 3000, 1]
materiales_mesa=[tabla,soporte]
mesa = ["mesa", "3", materiales_mesa]
cojin=["cojin", "12", 2000, 1]
soporte_silla=["soporte_silla", "223", 4000, 1]
materiales_silla=[cojin,soporte_silla]
mesa = ["mesa", "3", materiales_mesa]
silla = ["silla", "23", materiales_silla]
products = [mesa, silla]

def main():
    try:
        opcion = int(input("Ingrese el numero de la opcion que quiere ejecutar(1: Agregar producto, 2: Editar producto, 3: Ver producto)"))

        if opcion == 1:
            new_product = []
            name = str(input("Ingrese el nombre: "))
            code = str(input("Ingrese el codigo: "))
            
            new_product.append(name)
            new_product.append(code)
            materials_product = []
            materials_product_array = []
            
            quantity_products = int(input("Cuantos materiales tiene el producto: "))
            for i in range(quantity_products):
                name_material = str(input("Ingrese el nombre del material: "))
                code_material = str(input("Ingrese el codigo del material: "))
                valor_material = int(input("Ingrese el valor del material: "))
                quantity_material = int(input("Ingrese la cantidad del material: "))
                #materials_product[name_material, code_material, valor_material, quantity_material]
                materials_product.append(name_material)
                materials_product.append(code_material)
                materials_product.append(valor_material)
                materials_product.append(quantity_material)
                materials_product_array.append(materials_product)
                new_product.append(materials_product_array)
                
            
            products.append(new_product)
            main()
        elif opcion == 2:
            number = 1
            for x in products:
                
                print(number)
                number = number + 1
                print(x[0])
                #number_str = {number}
                #product_str = {x[x][0]}
                #result = f'{number_str}{product_str}'
                #print(result)
                
            opcion2 = int(input("Ingrese el numero del producto que quiere editar: "))
            print("Nombre: " + products[opcion2-1][0])
            print("Codigo: " + products[opcion2-1][1])
            print("Materiales: ")
            number_for = 0
            valor_producto_actual = 0
            print("--------------------------------------------------")
            
            for x in products[opcion2-1][2]:
                
                print("Nombre: " + products[opcion2-1][2][number_for][0])
                print("Codigo: " + products[opcion2-1][2][number_for][1])
                print("Valor por pieza: " + str(products[opcion2-1][2][number_for][2]))
                print("Cantidad: " + str(products[opcion2-1][2][number_for][3]))
                valor_producto_actual = valor_producto_actual + products[opcion2-1][2][number_for][2] * products[opcion2-1][2][number_for][3]
                print("--------------------------------------------------")
                number_for = number_for + 1
            print("Valor total del producto: " + str(valor_producto_actual))
            opcion3 = int(input("Ingrese 1 para editar el nombre, Ingrese 2 para editar el codigo, Ingrese 3 para editar un material: "))
            if opcion3 == 1:
                new_name = input("Ingrese el nuevo nombre: ")
                products[opcion2-1][0] = new_name
                print("Nombre cambiado satisfactoriamente")
                main()
            elif opcion3 == 2:
                new_code = input("Ingrese el nuevo codigo: ")
                products[opcion2-1][0] = new_code
                print("Codigo cambiado satisfactoriamente")
                main()
            elif opcion3 == 3:
                number_for = 0
                material_edit = str(input("Que material quiere editar? ingrese el nombre: "))
                #for x in products[opcion2-1][2][number_for]:
                    #print(number_for+1)
                    #print(products[opcion2-1][2][number_for][0])
                   # number_for = number_for+1
               # number_for = 0
                print(products[opcion2-1][2][number_for])
                for x in products[opcion2-1][2][number_for]:
                    if material_edit == products[opcion2-1][2][number_for][0]:
                        what_to_change = int(input("Ingrese 1 para cambiar el nombre, ingrese 2 para cambiar el codigo, ingrese 3 para cambiar el valor, ingrese 4 para cambiar la cantidad: "))
                        if what_to_change == 1:
                            new_name = str(input("Ingrese el nuevo nombre: "))
                            products[opcion2-1][2][number_for][0] = new_name
                            print("Nombre cambiado satisfactoriamente")
                            main()
                        elif what_to_change == 2:
                            new_code = str(input("Ingrese el nuevo codigo: "))
                            products[opcion2-1][2][number_for][1] = new_code
                            print("Code cambiado satisfactoriamente")
                            main()
                        elif what_to_change == 3:
                            new_price = int(input("Ingrese el nuevo valor: "))
                            products[opcion2-1][2][number_for][2] = new_price
                            print("Valor cambiado satisfactoriamente")
                            main()
                        elif what_to_change == 4:
                            new_quantity = int(input("Ingrese la nueva cantidad: "))
                            products[opcion2-1][2][number_for][3] = new_quantity
                            print("Cantidad cambiada satisfactoriamente")
                            main()
                    number_for = number_for + 1
                print("No hay materiales con ese nombre")
                main()
        elif opcion == 3:
            number = 1
            for x in products:
                
                print(number)
                number = number + 1
                print(x[0])
                #number_str = {number}
                #product_str = {x[x][0]}
                #result = f'{number_str}{product_str}'
                #print(result)
                
            opcion2 = int(input("Ingrese el numero del producto que quiere revisar: "))
            print("Nombre: " + products[opcion2-1][0])
            print("Codigo: " + products[opcion2-1][1])
            print("Materiales: ")
            number_for = 0
            valor_producto_actual = 0
            print("--------------------------------------------------")
            
            for x in products[opcion2-1][2]:
                
                print("Nombre: " + products[opcion2-1][2][number_for][0])
                print("Codigo: " + products[opcion2-1][2][number_for][1])
                print("Valor por pieza: " + str(products[opcion2-1][2][number_for][2]))
                print("Cantidad: " + str(products[opcion2-1][2][number_for][3]))
                valor_producto_actual = valor_producto_actual + products[opcion2-1][2][number_for][2] * products[opcion2-1][2][number_for][3]
                print("--------------------------------------------------")
                number_for = number_for + 1
            print("Valor total del producto: " + str(valor_producto_actual))
            main()
        else:
            print("Opción no válida.")
            main()
        
    except ValueError:
        print("Debe ingresar un numero")
        main()
main()