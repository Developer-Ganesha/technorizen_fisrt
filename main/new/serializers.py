from rest_framework import serializers
from new.models import User 
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode ,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator 
from rest_framework_simplejwt.tokens import RefreshToken ,TokenError
from.utils import Utils

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name' , 'email','mobile','password']
        extra_kwargs ={
            'password':{'write_only':True}
        }

    def vallidate(self ,attrs):
        password =attrs.get('password')    
       
        if password!=password:
            raise serializers.ValidationError("password  doesnot match")
        return attrs
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']

class LogOutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()  
    def validate(self, attrs):
        token = attrs["refresh_token"]
        return attrs
    def  save(self,**kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad token')
    
class SandPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields= ['email']
    def validate(self,attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID',uid)
            token = PasswordResetTokenGenerator().make_token(user)
            link = 'http://localhost8000/api/user/reset/'+uid+'/'+token
            body = 'Click following link to reset password'
            data ={
                'subject':'Reset your password',
                'body' :body,

            }
            Utils.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError('you are not a Register user')
        
class SandPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    class Meta:
        fields = ['password']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            uid= self.context.get('uid')                                                              
            token= self.context.get('token')
            if password != password:
                raise serializers.ValidationError("Wronge password")
            id =smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise serializers.ValidationError('Token is not valid or expired')
                                                                        
            user.set_password(password)
            user.save()
            return attrs 
 
        except DjangoUnicodeDecodeError  as identifier:
            user = User.objects.get(id=id)
            PasswordResetTokenGenerator().check_token(user,token)
            raise serializers.ValidationError('Token is not valid or expired')
        

            