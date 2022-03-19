import json
from datetime import datetime

from peewee import *


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now, verbose_name="创建时间")
    updated_at = DateTimeField(default=datetime.now, verbose_name="更新时间")


class DeletedModel(Model):
    deleted_at = DateTimeField(default=None, verbose_name="删除时间", null=True)

    def save(self, *args, **kwargs):
        if self._pk is None:
            self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    @classmethod
    def delete(cls, permanently=False):
        if permanently:
            return super().delete()
        else:
            return super().update(deleted_at=datetime.now())

    def delete_instance(self, permanently=False, recursive=False, delete_nullable=False):
        if permanently:
            return self.delete().where(self._pk_expr()).execute()
        else:
            self.deleted_at = datetime.now()
            return self.save()

    @classmethod
    def select(cls, *fields):
        return super().select().where(cls.deleted_at == None)


class JSONField(TextField):
    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return json.loads(value)


class EnumField(Field):
    field_type = 'tinyint'

    def adapt(self, value):
        try:
            return int(value)
        except ValueError:
            return value
