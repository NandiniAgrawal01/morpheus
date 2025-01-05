from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Form,Field, Submission
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import FormSerializer,FieldSerializer, SubmissionSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

class FormListCreateView(APIView):
    def get(self, request):
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Create the form
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_field(request):
    if request.method == 'POST':
        # Validate if form exists
        form_id = request.data.get('form')
        try:
            form = Form.objects.get(id=form_id)
        except Form.DoesNotExist:
            return Response({"error": "Form not found."}, status=status.HTTP_400_BAD_REQUEST)

        # Add the form instance to the field data
        field_data = request.data
        field_data['form'] = form
        serializer = FieldSerializer(data=field_data)

        if serializer.is_valid():
            serializer.save()  # Save the new field
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_fields_for_form(request, form_id):
    try:
        form = Form.objects.get(id=form_id)
    except Form.DoesNotExist:
        return Response({"error": "Form not found."}, status=status.HTTP_404_NOT_FOUND)

    fields = form.fields.all()
    serializer = FieldSerializer(fields, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def submit_form(request, form_id):
    try:
        form = Form.objects.get(id=form_id)
    except Form.DoesNotExist:
        return Response({"error": "Form not found."}, status=status.HTTP_404_NOT_FOUND)

    responses = request.data.get('responses', [])
    for response in responses:
        field_id = response.get('field')
        try:
            field = form.fields.get(id=field_id)
        except Field.DoesNotExist:
            return Response({"error": f"Field with id {field_id} not found."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the submission
        Submission.objects.create(form=form, field=field, value=response.get('value'))

    return Response({"message": "Form submitted successfully."}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_submissions_for_form(request, form_id):
    try:
        form = Form.objects.get(id=form_id)
    except Form.DoesNotExist:
        return Response({"error": "Form not found."}, status=status.HTTP_404_NOT_FOUND)

    submissions = form.submission_set.all()  # Assuming Submission is related to Form
    serializer = SubmissionSerializer(submissions, many=True)
    return Response(serializer.data)


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [IsAuthenticated]

class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated]


def index(request):
    return render(request, 'index.html')