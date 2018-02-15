from lxml import etree
doc=etree.parse('provinciasypoblaciones.xml')
provincias= doc.findall("provincia")
for provincia in provincias:
    localidades=provincia[1].findall("localidad")
    for localidad in localidades:
        print (localidad.text)
