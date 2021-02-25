import os
BAS_DIR=os.path.dirname(os.path.dirname(__file__))

DATABASE={
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME':os.path.join(BAS_DIR,'db.sqlite3')
    }
}