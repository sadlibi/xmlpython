from lxml import etree
doc=etree.parse('provinciasypoblaciones.xml')
provincias= doc.findall("provincia")
for provincia in provincias:
    print(provincia[0].text)