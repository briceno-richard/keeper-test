from rest_framework import serializers
from .models import WebBookmark

class BookmarkItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    url = serializers.CharField(max_length=200)

    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = WebBookmark
        #fields = ('id', 'title', 'url', 'owner', 'date_created', 'date_modified') # ADD 'owner'
        #read_only_fields = ('date_created', 'date_modified')
        fields = ('__all__')