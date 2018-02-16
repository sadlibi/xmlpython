lista=["01","02","03","04","05","06"]
from lxml import etree
doc=etree.parse('provinciasypoblaciones.xml')
provincias=doc.findall("provincia")
for provincia in provincias:
    idprovincia=provincia.get("id")
    nombre=provincia.find("nombre")
    localidades=provincia.findall("localidades/localidad")
    for localidad in localidades:
        for ident in lista:
            if idprovincia==ident:
                print(idprovincia,nombre.text, localidad.text)
