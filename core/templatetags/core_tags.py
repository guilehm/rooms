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
    'Room': 'Sala',
    'Scheduled': 'Agendada',
    'Canceled': 'Cancelada',
    'Status': 'Status',
    'Date': 'Data',
    'Start': 'Início',
    'End': 'Fim',
}


@register.filter(name='translation')
def translation(value):
    return translation_dict.get(str(value), '')
