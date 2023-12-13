from rest_framework import serializers
from customer.models import Customer, User, Vendor, MultipleAddress
 
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class CustomerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'email', 'birth_date', 'phone_number',
            'address', "city", 'state', 'zip_code' ,'password','password2',]
    
    def validate(self,attrs):
        pass1 = attrs.get('password',None)
        if pass1:
            if attrs['password']==attrs['password2']:
                return attrs
            else:
                raise serializers.ValidationError("password does not match")
        else:
            return attrs
    
    
    def create(self, validated_data):
        password = validated_data.get('password',None)
        password2 = validated_data.get('password2', None)
        if password and password2 and password==password2:
            customer = Customer.objects.create(
                username=validated_data.get('username',None),
                first_name=validated_data.get('first_name',None),
                last_name=validated_data.get('last_name',None),
                email=validated_data.get('email',None),
                birth_date=validated_data.get('birth_date',None),
                phone_number = validated_data.get('phone_number',None),
                address = validated_data.get('address',None),
                city = validated_data.get('city',None),
                state = validated_data.get('state',None),
                zip_code = validated_data.get('zip_code',None),
            )
            customer.set_password(validated_data['password'])
            customer.save()

            return customer
        else:
            raise serializers.ValidationError('password did not match')
        
        

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields  = ['id','user','aadhar_number', 'ac_number', 'gst_invoice' ]
        
    # we can also create data in serializer
    # def create(self, validated_data):
    #     user = validated_data.get('user')
    #     customer  = User.objects.get(username = user) 
    #     aadhar_number = validated_data.get('aadhar_number')
    #     ac_number = validated_data.get('aadhar_number')
    #     gst_invoice = validated_data.get('gst_invoice')
        
    #     vendor=Vendor.objects.create(aadhar_number=aadhar_number, 
    #                     ac_number=ac_number, 
    #                     gst_invoice=gst_invoice,
    #                     user = user
                        
    #                     )
        
    #     customer.is_vendor = True
    #     customer.save()
    #     return vendor
            
    
class VendorSerializerForAnnon(serializers.ModelSerializer):
    user = CustomerSerializer()
    class Meta:
        model = Vendor
        fields  = ['user','aadhar_number', 'ac_number', 'gst_invoice' ]
        
        
class MultipleAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultipleAddress
        fields = ['id', 'name','phone_number', 'locality', 'pincode', 'address', 'city', 'state', 'landmark']

