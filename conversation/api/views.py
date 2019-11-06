"""
API Serializers

"""

# django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from api.models import Conversation

# Serializers
from api.serializers import ConversationSerializer


# Create your views here.


class ConversationsView(APIView):
    """
    Conversation view.
    """
    def get(self, request, conversation_id, format=None):
        """Hangles GET method"""
        conversation = Conversation.objects.get(id=conversation_id)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)


class ConversationsList(APIView):
    """
    Conversations list view.

    Creates a conversation
    Starts a conversation
    """
    def get(self, request, format=None):
        """Handles GET method"""

        conversations = Conversation.objects.all()
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)
