from lxml import etree
doc=etree.parse('provinciasypoblaciones.xml')
provincias=doc.findall("provincia")
municipio=input("Dime un municipio: ")
for provincia in provincias:
    nombre=provincia.find("nombre")
    localidades=provincia.findall("localidades/localidad")
    for localidad in localidades:
        if localidad.text == municipio:
            print ("Es de la provincia:",nombre.text)
    
