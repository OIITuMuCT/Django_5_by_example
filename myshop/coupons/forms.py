from django import forms

class CouponApplyForm(forms.Form):
    """ Форма для ввода кода скидки """
    code = forms.CharField()
