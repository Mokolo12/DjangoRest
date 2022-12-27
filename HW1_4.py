from rest_framework.serializers import HyperlinkedModelSerializer
from author import models as author_models

class PersoneModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = author_models.PersoneModel
        fields = ["username", "first_name", "surname", "email"]