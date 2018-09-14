from django import template

register = template.Library()

translation_dict = {
    'True': 'Sim',
    'False': 'Não'
}


@register.filter(name='translation')
def translation(value):
    return translation_dict.get(str(value), '')
