from django.contrib import admin
from .models import Wishlist, WishlistItem

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at') 
    search_fields = ('user__user__username',)  
    list_filter = ('created_at',)  

class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('wishlist', 'product', 'added_at')  
    search_fields = ('wishlist__user__user__username', 'product__name') 
    list_filter = ('added_at',) 

# Registering with the custom admin settings
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(WishlistItem, WishlistItemAdmin)
