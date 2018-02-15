from lxml import etree
doc=etree.parse('provinciasypoblaciones.xml')
provincias=doc.findall("provincia")
for provincia in provincias:
    idprovincia=provincia.get("id")
    nombre=provincia.find("nombre")
    localidades=provincia.findall("localidades/localidad")
    for localidad in localidades:
        print(idprovincia,nombre.text, localidad.text)
