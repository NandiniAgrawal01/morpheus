from rest_framework import serializers
from .models import Form, Field, Submission

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['id', 'form', 'label', 'field_type', 'required', 'order']

class FormSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Form
        fields = ['id', 'title', 'description', 'created_at', 'fields']

    def create(self, validated_data):
        # Extract nested fields data
        fields_data = validated_data.pop('fields', [])
        # Create the form object
        form = Form.objects.create(**validated_data)
        
        # Create the related Field objects
        for field_data in fields_data:
            Field.objects.create(form=form, **field_data)
        
        return form

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['form', 'field', 'value']
