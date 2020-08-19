from django.urls import path
from django.contrib import admin
from forum.views import dashboard,questions,discussion,upvote,delete_ques,delete_ans
urlpatterns = [
path('admin/', admin.site.urls),
	path('dashboard/',dashboard),
	path('questions/',questions),
	path('discussion/<int:question_id>/',discussion),
	path('upvote/<int:answer_id>/',upvote),
	path('delete_ques/<int:question_id>/', delete_ques),
    path('delete_ans/<int:answer_id>/', delete_ans),
]