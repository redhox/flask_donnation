import mysql.connector 
from connexion import connexion,deconnexion
def get_donateur():
    bdd , cursor = connexion()
    query = "SELECT * FROM donateur"
    cursor.execute(query)
    resulta_bdd=cursor.fetchall()
    donateurs = []
    for enregistrement in resulta_bdd :
        liste=[]
        liste.append(enregistrement[1])
        liste.append(enregistrement[2])
        liste.append(enregistrement[3])
        liste.append(enregistrement[4])
        donateurs.append(liste)
    deconnexion()
    return donateurs

def set_donateur(nom, prenom,don,message):
    bdd , cursor = connexion()
    
    print(f'bdd={bdd}')
    if bdd is not None:
        
        query = 'INSERT INTO donateur(nom, prenom, don, message) VALUES (%s, %s, %s, %s);'
        data = (nom, prenom, don, message)
        cursor.execute(query, data)
        bdd.commit()
        deconnexion()
        return
    else:
        print("ereur de conection")
"""
# un element par son ID
def get_element(id):
    global cursor
    connexion()
    query = "SELECT * FROM elemement WHERE id=" + str(id)
    cursor.execute(query)
    element = {}
    for enregistrement in cursor :
        element['id'] = enregistrement[0]
        element['created'] = enregistrement[1]
        element['title'] = enregistrement[2]
        element['content'] = enregistrement[3]
        element['mail'] = enregistrement[4]
        element['note'] = enregistrement[5]
    deconnexion()
    return element
# tout les element d'une table
def lire_elements():
    global cursor
    connexion()
    query = "SELECT * FROM element"
    cursor.execute(query)
    elements = []
    for enregistrement in cursor :
        element = {}
        element['id'] = enregistrement[0]
        element['created'] = enregistrement[1]
        element['title'] = enregistrement[2]
        element['content'] = enregistrement[3]
        element['note'] = enregistrement[5]
        elements.append(element)
    deconnexion()
    return elements
# integré un element dans une table
def set_element(title, content, mail, note):
    global cursor
    global bdd
    connexion()
    query = 'INSERT INTO elements(title, content, mail, note) VALUES (%s, %s, %s, %s);'
    data = (title, content, mail, note)
    cursor.execute(query, data)
    bdd.commit()
    deconnexion()"""