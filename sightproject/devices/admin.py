from django.contrib import admin

from .models import Switch, Terminal, SwitchTerminal

admin.site.register(Switch)
admin.site.register(Terminal)
admin.site.register(SwitchTerminal)

# Register your models here.
