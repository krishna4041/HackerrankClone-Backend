from rest_framework import serializers
from restLearning.models import *

class ProblemSerializers(serializers.ModelSerializer):
    class Meta():
        model = Problem
        fields = '__all__'


class TextBox(serializers.ModelSerializer):
    class Meta():
        model = Text
        fields = '__all__'


