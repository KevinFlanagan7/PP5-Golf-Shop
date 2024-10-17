from django.contrib import admin
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken


admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)
