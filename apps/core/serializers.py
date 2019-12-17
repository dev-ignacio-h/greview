from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['creation_date','name', 'last_name', 'email', 'description', 'web', 'facebook', 'twitter', 'instagram']

