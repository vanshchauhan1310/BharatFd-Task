from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    question = serializers.CharField()
    answer = serializers.CharField()

    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'language']

    def to_representation(self, instance):
        # Retrieve the language from context (passed from the view)
        lang = self.context.get('lang', 'en')

        # If the FAQ's language is not the requested language, translate it
        translated_text = instance.get_translated_text(lang)

        # Return the translated question and answer
        return {
            'question': translated_text['question'],
            'answer': translated_text['answer'],
            'language': instance.language
        }
