from django.contrib import admin

from User.models import User, Bus, Bus_Position, User_Position, Route, Stop

admin.site.register(User)
admin.site.register(Bus)
admin.site.register(Bus_Position)
admin.site.register(User_Position)
admin.site.register(Route)
admin.site.register(Stop)
