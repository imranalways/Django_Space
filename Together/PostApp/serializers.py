from rest_framework import serializers
from PostApp.models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id',
                  'PostId',
                  'UserId',
                  'PostBody',
                  'PostDate',
                  'PostBy',
                  'PostUpdatedBy',
                  'PostUpdatedDate',
                  'PostPrivacy',
                  'IsDeleted')