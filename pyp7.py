from lxml import etree
doc=etree.parse('provinciasypoblaciones.xml')
provincias=doc.findall("provincia")
prov=input("Dime una provincia: ")
for provincia in provincias:
    nombre=provincia.find("nombre")
    if (nombre.text)==prov:
        localidades=provincia.findall("localidades/localidad")
        for localidad in localidades:
            idlocal=localidad.get("c")
            if idlocal==1:
                print (localidad.text)


