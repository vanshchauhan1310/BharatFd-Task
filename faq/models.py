from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    language = models.CharField(max_length=10, default='en')

    # Additional fields for language-specific translations
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    question_fr = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)
    answer_fr = RichTextField(blank=True, null=True)

    def get_translated_text(self, lang, queryset=None):
        """Fetches dynamically translated text using cache and queryset."""

        # If no queryset is provided, fallback to the current FAQ object
        if not queryset:
            queryset = FAQ.objects.filter(id=self.id)

        faq = queryset.first()

        if faq:
            translated_question = getattr(faq, f"question_{lang}", None)
            translated_answer = getattr(faq, f"answer_{lang}", None)

            # If translations are available in the queryset, return them
            if translated_question and translated_answer:
                return {'question': translated_question,
                        'answer': translated_answer}

        # If translations are not available,fall back to Google Translate
        cache_key = f"faq_{self.id}_{lang}"
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        # If no cached translation, use Google Translate
        translator = Translator()
        try:
            translated_question = (translator.translate
                                   (self.question, src=self.language,
                                    dest=lang).text)
            translated_answer = (translator.translate
                                 (self.answer, src=self.language,
                                  dest=lang).text)
        except Exception:
            translated_question = self.question
            translated_answer = self.answer

        # Caching translation for 1 day
        translation_data = {'question': translated_question,
                            'answer': translated_answer}
        cache.set(cache_key, translation_data, timeout=86400)
        return translation_data

    def save(self, *args, **kwargs):
        """Override save to automatically generate translations."""
        translator = Translator()

        if self.language == "en":
            self.question_hi = (translator.translate
                                (self.question, src='en', dest='hi').text)
            self.question_bn = (translator.translate
                                (self.question, src='en', dest='bn').text)
            self.question_fr = (translator.translate
                                (self.question, src='en', dest='fr').text)
            self.answer_hi = (translator.translate
                              (self.answer, src='en', dest='hi').text)
            self.answer_bn = (translator.translate
                              (self.answer, src='en', dest='bn').text)
            self.answer_fr = (translator.translate
                              (self.answer, src='en', dest='fr').text)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.question[:50]} ({self.language})"
