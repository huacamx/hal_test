"""
API serializers.
"""

# Django REST Framework
from rest_framework import serializers

# Models
from api.models import (
    Answer,
    Question,
    Transition,
    Conversation
)


class AnswerSerializer(serializers.ModelSerializer):
    """
    Answer serializer.
    """

    class Meta:
        model = Answer
        fields = ['answer_text', 'has_transition']


class QuestionSerializer(serializers.ModelSerializer):
    """
    Question serializer.
    """

    class Meta:
        model = Question
        fields = ['question_text', 'answers']


class TransitionSerializer(serializers.ModelSerializer):
    """
    Transition serializer.
    """

    class Meta:
        model = Transition
        fields = ['previous_question', 'selected_answer', 'next_question']


class ConversationSerializer(serializers.ModelSerializer):
    """
    Conversation serializer.
    """

    class Meta:
        model = Conversation
        fields = ['conversation_name', 'start_question']
        depth = 2
