from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
		#fields = ('user_id', 'first_name', 'last_name', 'company_name', 'city' , 'state' , 'zipcode' , 'email', 'web', 'age')
