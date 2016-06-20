import vk
from time import sleep

def create_userslist():
    query = api.users.search(hometown = 'Тарко-Сале', count = 500)
    query.remove(query[0])
    for f in query:
        userslist.append(f['uid'])
        
def get_wall():
    for user in userslist:
        try:
            wall = ''
            data = api.wall.get(owner_id = user, filter = 'owner', count = 100)
            data.remove(data[0])
            for d in data:
                if d['post_type'] == 'post':
                    wall = wall + d['text']+'\n\n'
                if 'copy_text' in d:
                    wall = wall + d['text']+'\n\n'
            f = open('id' + str(user)+'.txt', 'w', encoding = 'utf-8')
            f.write(wall)
            f.close
        except:
            sleep(0.20)

def metadata():
    data = ''
    for user in userslist:
        try:
            check = api.users.get(user_id=user, fields = 'sex, bdate, city, home_town, personal')
            uid = str(check[0]['uid'])
            first_name = check[0]['first_name']
            last_name = check[0]['last_name']
            if 'bdate' in check[0]:
                bdate = check[0]['bdate']
            else: bdate = ' '
            if check[0]['sex'] == 1:
                sex = 'female'
            elif check[0]['sex'] == 2:
                sex = 'male'
            else:
                sex = ' '
            city = check[0]['city']
            if city != 0:
                city = api.database.getCitiesById(city_ids = city)[0]['name']
            else: 
                city = ' '
            if 'home_town' in check[0]:
                home_town = check[0]['home_town']
            else: home_town = ' '
            data = data + uid + '\t' + first_name + '\t' + last_name + '\t' + bdate + '\t' + sex + '\t' + city + '\t' + home_town + '\n'
        except:
            sleep(0.20)
        f = open('data.tsv', 'w', encoding = 'utf-8')     
        f.write(data)
        f.close

session = vk.AuthSession(app_id='', user_login='', user_password='')
api = vk.API(session)
userslist = []

create_userslist()
get_wall()
metadata()
