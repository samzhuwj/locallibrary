# import datetime
# 
# from django.test import TestCase
# from django.utils import timezone
# 
# from catalog.forms import RenewBookForm
# 
# 
# class RenewBookFormTest(TestCase):
#     def test_renew_form_date_in_past(self):
#         """
#         Test form is invalid if renewal_date is before today
#         """
#         date = datetime.date.today() - datetime.timedelta(days=1)
#         form_data = {'renewal_date': date}
#         form = RenewBookForm(data=form_data)
#         self.assertFalse(form.is_valid())
# 
#     def test_renew_form_date_too_far_in_future(self):
#         """
#         Test form is invalid if renewal_date more than 4 weeks from today
#         """
#         date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
#         form_data = {'renewal_date': date}
#         form = RenewBookForm(data=form_data)
#         self.assertFalse(form.is_valid())
# 
#     def test_renew_form_date_today(self):
#         """
#         Test form is valid if renewal_date is today
#         """
#         date = datetime.date.today()
#         form_data = {'renewal_date': date}
#         form = RenewBookForm(data=form_data)
#         self.assertTrue(form.is_valid())
# 
#     def test_renew_form_date_max(self):
#         """
#         Test form is valid if renewal_date is within 4 weeks
#         """
#         date = timezone.now() + datetime.timedelta(weeks=4)
#         form_data = {'renewal_date': date}
#         form = RenewBookForm(data=form_data)
#         self.assertTrue(form.is_valid())
# 
# 
#     def test_renew_form_date_field_label(self):
#         """
#         Test renewal_date label is "renewal date"
#         """
#         form = RenewBookForm()        
#         self.assertTrue(form.fields['renewal_date'].label == None or form.fields['renewal_date'].label == 'renewal date')
# 
# 
#     def test_renew_form_date_field_help_text(self):
#         """
#         Test renewal_date help_text is as expected.
#         """
#         form = RenewBookForm()
#         self.assertEqual(form.fields['renewal_date'].help_text,'Enter a date between now and 4 weeks (default 3).')

import datetime

from django.test import TestCase
from django.utils import timezone

from catalog.forms import RenewBookModelForm


class RenewBookFormTest(TestCase):
    def test_renew_form_date_in_past(self):
        """
        Test form is invalid if due_back is before today
        """
        date = datetime.date.today() - datetime.timedelta(days=1)
        form_data = {'due_back': date}
        form = RenewBookModelForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_too_far_in_future(self):
        """
        Test form is invalid if due_back more than 4 weeks from today
        """
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form_data = {'due_back': date}
        form = RenewBookModelForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        """
        Test form is valid if due_back is today
        """
        date = datetime.date.today()
        form_data = {'due_back': date}
        form = RenewBookModelForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        """
        Test form is valid if due_back is within 4 weeks
        """
        date = timezone.now() + datetime.timedelta(weeks=4)
        form_data = {'due_back': date}
        form = RenewBookModelForm(data=form_data)
        self.assertTrue(form.is_valid())


    def test_renew_form_date_field_label(self):
        """
        Test due_back label is "renewal date"
        """
        form = RenewBookModelForm()        
        self.assertTrue(form.fields['due_back'].label == None or form.fields['due_back'].label == 'Renewal date')


    def test_renew_form_date_field_help_text(self):
        """
        Test due_back help_text is as expected.
        """
        form = RenewBookModelForm()
        self.assertEqual(form.fields['due_back'].help_text,'Enter a date between now and 4 weeks (default 3).')
