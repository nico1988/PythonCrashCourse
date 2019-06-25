users = {
    'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton', },
     'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris', },
}
for username,userinfo in users.items():
    print('username'+username)
    print(userinfo.items())