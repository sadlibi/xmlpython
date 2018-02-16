from lxml import etree
doc=etree.parse('provinciasypoblaciones.xml')
provincias=doc.findall("provincia")
local= input("Dime una localidad: ")
for provincia in provincias:
    nombre=provincia.find("nombre")
    localidades=provincia.findall("localidades/localidad")
    for localidad in localidades:
        if (localidad.text)==local:
            idlocal=localidad.get("c")
            if idlocal=="1":
                print (localidad.text, "es una ciudad grande de la provincia", nombre.text)
            else:
                print ("Es una ciudad pequeña de", nombre.text)