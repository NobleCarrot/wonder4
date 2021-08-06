from django.contrib import admin
from library.models import Book, Borrowing, Reader, Movie, Like


class BookAdmin(admin.ModelAdmin):
    list_display = ('ISBN','title','author','press','description','price','category','cover','index','location','quantity')
class MovieAdmin(admin.ModelAdmin):
    list_display = ('rate','title','movie_url','image','info')


class ReaderAdmin(admin.ModelAdmin):
    list_display =('user','name','phone','max_borrowing','balance','photo')


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('reader','ISBN','date_issued','date_due_to_returned','date_returned','amount_of_fine')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('reader','ISBN')

admin.site.register(Book,BookAdmin)
admin.site.register(Borrowing,BorrowingAdmin)
admin.site.register(Reader,ReaderAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.name = 'B&M information system'
admin.site.site_header = 'B&M information system'
