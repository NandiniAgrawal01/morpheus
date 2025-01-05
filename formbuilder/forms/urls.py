from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FormViewSet, FieldViewSet, FormListCreateView, create_field, get_fields_for_form, submit_form, get_submissions_for_form, index
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'forms', FormViewSet, basename='form')
router.register(r'fields', FieldViewSet, basename='field')

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/login/', views.obtain_auth_token),
    path('forms/', FormListCreateView.as_view(), name='form-list-create'),
    path('api/fields/', create_field, name='create_field'),
    path('api/forms/<int:form_id>/fields/', get_fields_for_form, name='get_fields_for_form'),
    path('api/forms/<int:form_id>/submit/', submit_form, name='submit_form'),
    path('api/forms/<int:form_id>/submissions/', get_submissions_for_form, name='get_submissions_for_form'),
    path('', index),
]
