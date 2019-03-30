def greeting(userid):
    return 'Привет, %s!' % name_for_userid.get(userid, 'всем')