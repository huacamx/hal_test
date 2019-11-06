"""
API admin

"""

# Django
from django.contrib import admin

# Models
from api.models import (
    Answer,
    Question,
    Transition,
    Conversation
)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """
    Answer admin.
    """
    list_display = ('answer_text', 'has_transition')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Question admin.
    """
    list_display = ('question_text',)


@admin.register(Transition)
class TransitionAdmin(admin.ModelAdmin):
    """
    Transition admin.
    """
    list_display = ('previous_question', 'selected_answer', 'next_question')


@admin.register(Conversation)
class ConversatioAdmin(admin.ModelAdmin):
    """
    Conversatio admin.
    """
    list_display = ('conversation_name', 'start_question')
