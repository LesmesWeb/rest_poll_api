from rest_framework.routers import DefaultRouter

from django.urls import path
from .apiviews import PollViewSet,PollList, PollDetail,ChoiceList, CreateVote
from .views import polls_list, polls_detail

router = DefaultRouter()
router.register(r'polls', PollViewSet)

urlpatterns = [
	path("polls/", polls_list, name="polls_list"),
	path("polls/<int:pk>/", polls_detail, name="polls_detail"),
	path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
	path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

]

urlpatterns += router.urls