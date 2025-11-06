from rest_framework  import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
        def create(self,validated_data):
            password = validated_data.pop('password')
            user = User.objects.create_user(**validated_data,password=password)
            return user
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        user = authenticate(username=data['username'],password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        return user