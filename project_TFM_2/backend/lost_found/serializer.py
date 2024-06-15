from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Lost, Found

class LostSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Lost
        fields = '__all__'

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('lost-edit', kwargs={'pk':obj.pk}, request=request)

class FoundSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Found
        fields = '__all__'

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('found-edit', kwargs={'pk':obj.pk}, request=request)