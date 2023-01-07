from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform




#model serializer
class WatchListSerializer(serializers.ModelSerializer):
    #adding field directly in serializers
    len_names=serializers.SerializerMethodField()
    class Meta:
        model=WatchList
        # fields=['id','name','description']
        exclude=['active']
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    #Nested serializer
    # watchlist=WatchListSerializer(many=True, read_only=True)
    watchlist=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie-detail')
    
    class Meta:
        model=StreamPlatform
        fields="__all__"
    
        
    # def get_len_name(self,object):
    #     length=len(object.name)
    #     return length
    
    # #validate current object level
    # def validat(self,data):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError("Title and description cant be same")
    
    
    # #field level validation
    # def validat_name(self,value):
    #     if(len(value)<2):
    #         raise serializers.ValidationError("Name is too short")
    #     else:   
    #         return value
    

#  #field level validation in serializer
# def name_length(value):
#         if(len(value)<2):
#             raise serializers.ValidationError("Name is short")
#         else:
#             return value
       
# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     description=serializers.CharField()
#     active=serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     #validate current object level
#     def validat(self,data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Title and description cant be same")
    
    
    # #field level validation
    # def validat_name(self,value):
    #     if(len(value)<2):
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value