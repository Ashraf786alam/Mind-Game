from django import template
import random
register=template.Library()

@register.filter(name="AddNumber")
def AddNumber(number1,number2):
    return number1+number2

@register.filter(name="SubNumber")
def SubNumber(number1,number2):
    return number1-number2

@register.filter(name="MultiplyNumber")
def MultiplyNumber(number1,number2):
    return number1*number2
