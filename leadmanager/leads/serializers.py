from dataclasses import fields
from rest_framework import serializers
from leads.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        #fields = ('name', 'email', 'create_at','message')