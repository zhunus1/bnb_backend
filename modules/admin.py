from django.contrib import admin
from .models import (
    StartUpStage,
    Industry,
    BussinessModel,
    Technology,
    SellingModel,
    Country,
    InnovationMethod,
    InvestRound,
)
# Register your models here.

admin.site.register(StartUpStage)
admin.site.register(Industry)
admin.site.register(BussinessModel)
admin.site.register(Technology)
admin.site.register(SellingModel)
admin.site.register(Country)
admin.site.register(InnovationMethod)
admin.site.register(InvestRound)