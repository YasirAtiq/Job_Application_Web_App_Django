from .models import Blogs, BlogContentImages
from django.contrib import admin


class BlogImageInline(admin.TabularInline):
    model = BlogContentImages


class BlogsAdmin(admin.ModelAdmin):
    search_fields = ("title", "description")
    list_filter = ("title", )
    inlines = [BlogImageInline]
    prepopulated_fields = {"thumbnail_img": ("title", )}
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'content', 'thumbnail_img', 'date_created')
        }),
    )
    readonly_fields = ("date_created", )

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'thumbnail_img':
            formfield.required = True
        return formfield


admin.site.register(Blogs, BlogsAdmin)