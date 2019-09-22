from werkzeug.security import safe_str_cmp
from user import User


# does not need because now its being store in DB
# users =[
#     User(1,'bob', 'asdf')
# ]

# username_mapping = {u.username:u for u in users}
# userid_mapping = {u.id :u for u in users}


def authenticate(username, password):
    # user=username_mapping.get(username ,None) cause now it will connect to DB
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password ,password):
        return user

def identity(payload):
    user_id = payload['identity']
    # return userid_mapping.get(user_id,None)
    return User.find_by_user_id(user_id)
