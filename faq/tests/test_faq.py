from django.test import TestCase
from faq.models import FAQ
from googletrans import Translator


class FAQModelTest(TestCase):

    def test_faq_creation(self):
        """Test if FAQ object is created correctly"""
        faq = FAQ.objects.create(question="What is Django?",
                                 answer="A Python web framework")
        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.answer, "A Python web framework")

    def test_faq_translation_hi(self):
        faq = FAQ.objects.create(
            question="What is Python?",
            answer="A programming language",
        )
        translated_text = faq.get_translated_text('hi')
        self.assertEqual(translated_text['question'], "पायथन क्या है?")
        self.assertEqual(translated_text['answer'], "एक प्रोग्रामिंग भाषा")

    def test_faq_translation_fr(self):
        faq = FAQ.objects.create(
            question="What is Python?",
            answer="A programming language",
        )
        translated_text = faq.get_translated_text('fr')
        self.assertEqual(translated_text['question'], "Qu'est-ce que Python?")
        self.assertEqual(translated_text['answer'],
                         "Un langage de programmation")

    def test_faq_translation_bn(self):
        faq = FAQ.objects.create(
            question="What is Python?",
            answer="A programming language",
        )
        translated_text = faq.get_translated_text('bn')
        self.assertEqual(translated_text['question'], "পাইথন কী?")
        self.assertEqual(translated_text['answer'], "একটি প্রোগ্রামিং ভাষা")

    def test_faq_translation_nl(self):
        faq = FAQ.objects.create(
            question="What is Python?",
            answer="A programming language",
        )
        translated_text = faq.get_translated_text('nl')
        self.assertEqual(translated_text['question'], "Wat is Python?")
        self.assertEqual(translated_text['answer'], "Een programmeertaal")

    def test_translation_cache(self):
        faq = FAQ.objects.create(
            question="What is Python?",
            answer="A programming language",
        )
        translated_text_1 = faq.get_translated_text('hi')
        translated_text_2 = faq.get_translated_text('hi')

        # Check that cache is being used
        self.assertEqual(translated_text_1, translated_text_2)

    def test_fallback_to_english_if_translation_unavailable(self):
        faq = FAQ.objects.create(
            question="What is Python?",
            answer="A programming language",
        )

        # Simulate no translation available for 'zz' (a non-supported language)
        translated_text = faq.get_translated_text('zz')
        self.assertEqual(translated_text['question'], faq.question)
        self.assertEqual(translated_text['answer'], faq.answer)
