from rest_framework import serializers
from articles.models import Article
from django.contrib.auth.models import User
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class ArticleSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'subtitle', 'image_url', 'author', 'content', 'tags']
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.subtitle = validated_data.get('subtitle', instance.subtitle)
        instance.image_url = validated_data.get('image_url', instance.imague_url)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'articles']