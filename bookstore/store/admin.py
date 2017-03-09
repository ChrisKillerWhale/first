from django.contrib import admin
from models import Book


# Register your models here.
# models must be regstierd to appear in admin
# from modles import model_name


class BookAdmin(admin.ModelAdmin):
    #chooses what columns to display on admin page
    list_display = ('title','author','price','stock')


admin.site.register(Book, BookAdmin)
