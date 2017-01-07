from django.db import models
from django.utils.translation import ugettext_lazy as _


class Topic(models.Model):
    text = models.CharField(max_length=200)
    number = models.IntegerField()

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')
        ordering = ['number']

    def __unicode__(self):
        return u'(%s) %s' % (self.number, self.text, )


class Question(models.Model):
    text = models.CharField(max_length=200)
    answer_text = models.TextField()
    topic = models.ForeignKey(Topic, related_name='questions')
    number = models.IntegerField()
    related_questions = models.ManyToManyField(
        'self',
        related_name='related_questions',
        blank=True,
    )

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ('number',)

    def __unicode__(self):
        return u'(%s) %s' % (self.number, self.text, )
