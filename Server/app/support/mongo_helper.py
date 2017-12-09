from mongoengine import *


def mongo_to_dict(obj, exclude_fields=list()):
    return_data = {}

    if obj is None:
        return None

    if isinstance(obj, Document):
        fields_ = obj._fields

        if 'id' in fields_:
            # EmbeddedDocument doesn't have _id
            return_data['id'] = str(obj.id)

        for field_name in fields_:
            if field_name in exclude_fields:
                continue

            data = obj._data[field_name]

            if data is None:
                return_data[field_name] = None
            elif isinstance(fields_[field_name], ListField):
                return_data[field_name] = list_field_to_dict(data)
            elif isinstance(fields_[field_name], EmbeddedDocumentField):
                return_data[field_name] = mongo_to_dict(data, [])
            elif isinstance(fields_[field_name], DictField):
                return_data[field_name] = data
            else:
                return_data[field_name] = mongo_to_python_type(fields_[field_name], data)

        return return_data


def list_field_to_dict(list_field):
    return_data = []

    for item in list_field:
        if isinstance(item, EmbeddedDocument):
            return_data.append(mongo_to_dict(item, []))
        else:
            return_data.append(mongo_to_python_type(item, item))

    return return_data


def mongo_to_python_type(field, data):
    if isinstance(field, DateTimeField):
        return str(data.isoformat())
    elif isinstance(field, ComplexDateTimeField):
        return field.to_python(data).isoformat()
    elif isinstance(field, StringField):
        return str(data)
    elif isinstance(field, FloatField):
        return float(data)
    elif isinstance(field, IntField):
        return int(data)
    elif isinstance(field, BooleanField):
        return bool(data)
    elif isinstance(field, ObjectIdField):
        return str(data)
    elif isinstance(field, DecimalField):
        return data
    else:
        return str(data)
