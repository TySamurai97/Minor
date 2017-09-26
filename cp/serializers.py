from rest_framework import serializers
from cp.models import UserData
from cp.models import CodeChef
from cp.models import UserHandler
from cp.models import Questions
from cp.models import Spoj
from cp.models import CodeForces

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model=UserData
      fields='__all__'

class CodeChefSerializer(serializers.ModelSerializer):
    class Meta:
        model=CodeChef
        fields='__all__'

class SpojSerializer(serializers.ModelSerializer):
    class Meta:
        model=Spoj
        fields='__all__'

class CodeForcesSerializer(serializers.ModelSerializer):
    class Meta:
        model=CodeForces
        fields='__all__'

class UserHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserHandler
        fields='__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Questions
        fields='__all__'

