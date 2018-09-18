from django import template

register = template.Library()

translation_dict = {
    'True': 'Sim',
    'False': 'Não',
    'Name': 'Nome',
    'Slug': 'Slug',
    'Description': 'Descrição',
    'Active': 'Ativa',
    'Color': 'Cor',
}


@register.filter(name='translation')
def translation(value):
    return translation_dict.get(str(value), '')
