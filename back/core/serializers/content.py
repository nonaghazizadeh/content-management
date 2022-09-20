from core.models import Content

from rest_framework import serializers


class CreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('title', 'file_format', 'file', 'attach_file')

    def create(self, validated_data):
        title, file_format, file = validated_data['title'], validated_data['file_format'], validated_data['file']
        attach_file = validated_data.get('attach_file')
        content = Content.objects.create(
            title=title,
            file_format=file_format,
            file=file,
            attach_file=attach_file,
            extra={k: self.initial_data[k] for k in set(self.initial_data) - set(validated_data)}
        )
        user = self.context['request'].user

        content.users.add(user)

        return content


class RetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('id', 'title', 'file_format', 'file', 'attach_file', 'extra')


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('id', 'title', 'file_format')


class ShareSerializer(serializers.Serializer):

    user_id = serializers.IntegerField()
    content_id = serializers.IntegerField()

