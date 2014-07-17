from django.contrib import admin

from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		("Poll Question", 	 {"fields": ["question"]}),
		("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]}),
		("Poll Information", {"fields": ["body"]}),
		]
	list_display = ("question", "pub_date", "was_published_recently")
	# filtering admin/polls/poll by question and pub date
	list_filter = [("question"), ("pub_date"),]
	inlines = [ChoiceInline]






admin.site.register(Poll, PollAdmin)



# Register your models here.
