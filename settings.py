import decouple

decouple.config.encoding = 'cp1251'
TOKEN = decouple.config('TOKEN')
OWNER_USERID = decouple.config('OWNER_USERID')
