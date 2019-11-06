from django.db import models

# Create your models here.


class Answer(models.Model):
    """
    Answer model.

    An answer is a transition.
    """
    answer_text = models.CharField(
        'The answer',
        max_length=80,
        blank=False,
        null=True
    )

    has_transition = models.BooleanField(default=False)

    def __str__(self):
        """Return answer text"""
        return self.answer_text


class Question(models.Model):
    """
    Questión model

    Is a state

    """

    question_text = models.CharField(
        'What do you want to ask?',
        max_length=600,
        blank=False,
        null=False
    )
    answers = models.ManyToManyField(Answer, related_name='question_asked')

    def __str__(self):
        """Return question_text"""
        return self.question_text


class Transition(models.Model):
    """
    Handles next question when its answered.

    """

    previous_question = models.ForeignKey(
        Question,
        related_name='transition_prev',
        on_delete=models.PROTECT
    )

    selected_answer = models.ForeignKey(
        Answer,
        related_name='transition_ans',
        on_delete=models.PROTECT
    )

    next_question = models.ForeignKey(
        Question,
        related_name='transition_next',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )


class ConversationPath():
    """
    Conversation path model.

    Saves path of Questions & Answers
    """


class Conversation(models.Model):
    """
    Conversation model.
    """

    conversation_name = models.CharField(
        'Conversation objective',
        max_length=350,
    )

    start_question = models.ForeignKey(
        Question,
        related_name='conversation',
        blank=True,
        null=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """Return Conversation name"""
        return self.conversation_name
