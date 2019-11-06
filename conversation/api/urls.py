"""
API urls
"""

# Django
from django.urls import path

# Views
from api.views import ConversationsList, ConversationsView


urlpatterns = [
    path(
        'conversations/',
        ConversationsList.as_view(),
        name="conversation_list"
    ),
    path(
        'conversations/<int:conversation_id>/',
        ConversationsView.as_view(),
        name="conversation"
    ),

]
