from django.contrib import admin
from vapp.models import Candidate
from vapp.models import Voter
# Register your models here.
admin.site.register(Candidate)
admin.site.register(Voter)
