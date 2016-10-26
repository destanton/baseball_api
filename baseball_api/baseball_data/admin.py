from django.contrib import admin
from baseball_data.models import Master, Batting, Pitching, Fielding


admin.site.register([Master, Batting, Pitching, Fielding])
