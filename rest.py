#!/usr/bin/env python

import web
import xml.etree.ElementTree as ET

tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user'
)

app = web.application(urls, globals())

class list_users:        
    def GET(self):
	output = 'users:[';
	for child in root:
                print 'child', child.tag, child.attrib
                output += str(child.attrib) + ','
	output += ']';
        return output

class get_user:
    def GET(self, user):
	for child in root:
		if child.attrib['id'] == user:
		    return str(child.attrib)

if __name__ == "__main__":
    app.run()

#Install web.py
#Criar xml user_data.xml com o seguinte conteudo
	#<users>
	#    <user id="1" name="Rocky" age="38"/>
	#    <user id="2" name="Steve" age="50"/>
	#    <user id="3" name="Melinda" age="38"/>
	#</users>
#Usar o codigo python acima
#Executar => python rest.py(nome do programa) 3030(porta do sv)
#Exemplos de URL
#http://localhost:8080/users
#http://localhost:8080/users/1
#http://localhost:8080/users/2
#http://localhost:8080/users/3
