#@api_view(['GET', 'POST'])
#def cat_list(request):
    #if request.method == 'POST':
        #serializer = CatSerializer(data=request.data, many=True)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #cats = Cat.objects.all()
    #serializer = CatSerializer(cats, many=True)
    #return Response(serializer.data)

#@api_view(['GET', 'PATCH'])
#def cat_detail(request, pk):
    #if request.method == 'PATCH':
        #cat= Cat.objects.get(id=pk)
        #serializer = CatSerializer(cat, data=request.data, partial=True)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #cat = Cat.objects.get(id=pk)
    #serializer = CatSerializer(cat)
    #return Response(serializer.data)

#@api_view(['GET', 'POST'])
#def hello(request):
    #if request.method == 'POST':
        #return Response({'message': 'Получены данные', 'data': request.data})
    #return Response({'message': 'Это был GET-запрос!'})
