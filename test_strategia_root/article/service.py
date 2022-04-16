from rest_framework.response import Response


def checking_primary_key(model, pk: int):
    if not pk:
        return Response({'Ошибка': f'{model.__name__} с id={pk} не существует'})
    model_list_id = list(model.objects.values('id'))
    new_id_list = [element['id'] for element in model_list_id]
    if pk not in new_id_list:
        return Response({'Ошибка': f'{model.__name__}  с id={pk} не существует'})
    else:
        return None
