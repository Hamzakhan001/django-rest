from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import WatchList,StreamPlatform,Review
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework import mixins

#concrete classes
class ReviewList(generics.ListCreateAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    

#mixins

# class ReviewDetail(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
        



#class based views
class WatchListAV(APIView):
    
    def get(self,request,pk):
        movies=WatchList.objects.all()
        serializer = WatchListSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request,pk):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchListDetailAV(APIView):
    
    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except:
            return Response({'Error':'Not found'})
        
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
    
    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


class StreamPlatformListAV(APIView):
    
    def get(self,request):
        movies=StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(movies,many=True,context={'request':request})
        return Response(serializer.data)
    
    def post(self,request,pk):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
  
class StreamPlatformDetailAV(APIView):
    def get(self,request,pk):
        try:
            platform=StreamPlatform.objects.get(pk=pk)
        except:
            return Response('Error:Not Found')
        serializer=StreamPlatformSerializer(platform)
        return Response(serializer.data)
        
# @api_view(['GET','POST'])
# def movie_list(request):
    
    
#     if request.method == 'GET':
#            movies=Movie.objects.all()
#            serializer = MovieSerializer(movies,many=True)
#            return Response(serializer.data)
#   # 
#     if request.method=='POST':
#            serializer=MovieSerializer(data=request.data)
#            if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.data)
#            else:
#                return Response(serializer.errors)
        

     
         


# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method== 'GET':
        
#         try:
#            movie=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error:Not found'},status=status.HTTP_403_FORBIDDEN)
            
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method== 'PUT':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method== 'DELETE':
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
        
    


    