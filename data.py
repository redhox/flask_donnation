from connexion import *



"""
def get_post(id):
    global cursor
    connexion()
    query = "SELECT * FROM posts WHERE id=" + str(id)
    cursor.execute(query)
    post = {}
    for enregistrement in cursor :
        post['id'] = enregistrement[0]
        post['created'] = enregistrement[1]
        post['title'] = enregistrement[2]
        post['content'] = enregistrement[3]
        post['mail'] = enregistrement[4]
        post['note'] = enregistrement[5]
    deconnexion()
    return post

def lire_posts():
    global cursor
    connexion()
    query = "SELECT * FROM posts"
    cursor.execute(query)
    posts = []
    for enregistrement in cursor :
        post = {}
        post['id'] = enregistrement[0]
        post['created'] = enregistrement[1]
        post['title'] = enregistrement[2]
        post['content'] = enregistrement[3]
        post['note'] = enregistrement[5]
        posts.append(post)
    deconnexion()
    return posts

def set_post(title, content, mail, note):
    global cursor
    global bdd
    connexion()
    query = 'INSERT INTO posts(title, content, mail, note) VALUES (%s, %s, %s, %s);'
    data = (title, content, mail, note)
    cursor.execute(query, data)
    bdd.commit()
    deconnexion()"""