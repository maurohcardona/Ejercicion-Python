import Cliente, Factura, Articulo, Linea

rosa_gonzalez = Cliente(34922207, "Rosa", "Gonzalez")

factura_1 = Factura(rosa_gonzalez)

televisor = Articulo("Televisor", 399)
tarjeta_grafica = Articulo("Tarjeta grafica", 239)

linea_1 = Linea(televisor, 2)
linea_2 = Linea(tarjeta_grafica, 1)

factura_1.añadir_linea(linea_1)
factura_1.añadir_linea(linea_2)

factura_1.imprimir_factura()
