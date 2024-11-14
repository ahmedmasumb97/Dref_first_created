
from rest_framework import serializers
from.models import Task,Book,Author

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed']


class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'author']
    
    
    def validate_title(self,value):
        if len(value) < 3:
            raise serializers.ValidationError('the title must be at least 3 characters')
        return value
        
    def validate_price(self,value):
        if value < 1:
            raise serializers.ValidationError('the price must be at least 1')
        return value
    
        
        
        
        


class Authorserializer(serializers.ModelSerializer):
    # book = Bookserializer(many=True,read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']