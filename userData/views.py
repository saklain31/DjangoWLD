from django.shortcuts import render
from userData.models import * 
from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect


# from rest_framework import generics
# from .serializers import tempOrderSerializer
# from rest_framework import viewsets

from rest_framework.views import APIView


import uuid
# Create your views here.


# class tempOrderViewSet(viewsets.ModelViewSet):
# 	queryset = tempOrder.objects.all()
# 	serializer_class = tempOrderSerializer

class Test(APIView):
	def saveTempOrder(request):
		if request.method == 'POST':    
			username = request.POST.get("username")
			email = request.POST.get("email")
			zipcode = request.POST.get("zipcode")
			order = tempOrder()
			order.firstname = username
			order.zipcode = zipcode
			order.email = email


			#uniqueId = uuid.uuid4()
			#order.orderID = uniqueId
			order.save()
			orderID = order.id+10000
			print("row index ",orderID," Timestamp of creation ",order.created_at)
			
			order.orderID = orderID

			order.save()

			#response = HttpResponse("utiutuiutuitui")#HttpResponsePermanentRedirect("/firstpair/")
			#response.set_cookie('orderID', 'wkkdshkashkjdahskdjha')
			return render(request,"instruction.html",{'orderID': orderID})

		return render(request, 'formFirstName.html')


def instructionURL(request):
	return render(request,'instruction.html')

def chooseDenim(request):
	return render(request,'ChooseDenim.html')

def chooseThread(request,denimID):
	print("DENIM ID ",denimID)
	return render(request,'ChooseThread.html')

def chooseCut(request,threadID):
	print("THREAD ID",threadID)
	return render(request,'ChooseCut.html')



# def chooseDenim2(request):
# 	return render(request,'ChooseDenim2.html')

# def chooseThread2(request,denimID):
# 	#save denim
# 	return render(request,'ChooseThread2.html')

# def chooseCut2(request,threadID):
# 	#save denim
# 	return render(request,'ChooseCut2.html')




# def selectedThread(request,ThreadID):
# 	return render(request,'SelectedThread.html',{'ThreadID': ThreadID})

def getJeans1(request):
	print(request.method)
	value=""
	if request.method == 'POST':
		if 'orderID' in request.COOKIES:
			value = request.COOKIES['orderID']
			print("orderId=",value)

		order = tempOrder.objects.filter(orderID = value)
		print("hhhhh",order[0].zipcode,order[0].name)

		order0 = order[0]

		temp1 = request.POST.get("cloth")
		order0.jeans1_1 = temp1
		print("llll",order0.jeans1_1)
		
		temp2 = request.POST.get("cut")
		order0.jeans1_2 = temp2
		print("kkkk",order0.jeans1_2)
		
		temp3 = request.POST.get("thread")
		order0.jeans1_3 = temp3
		print("laslas",order0.jeans1_3 )

		
		order0.save(update_fields=['jeans1_1','jeans1_2','jeans1_3'])
		
		return HttpResponsePermanentRedirect("/secondpair/")
	
	return render(request, 'jeans1.html')



def getJeans2(request):
	print(request.method)
	value=""
	if request.method == 'POST':
		if 'orderID' in request.COOKIES:
			value = request.COOKIES['orderID']
			print("orderId=",value)

		order = tempOrder.objects.filter(orderID = value)

		print("hhhhh",order[0].zipcode,order[0].name)

		order0 = order[0]

		temp1 = request.POST.get("cloth")
		order0.jeans2_1 = temp1
		print("llll",order0.jeans2_1)
		
		temp2 = request.POST.get("cut")
		order0.jeans2_2 = temp2
		print("kkkk",order0.jeans2_2)
		
		temp3 = request.POST.get("thread")
		order0.jeans2_3 = temp3
		print("laslas",order0.jeans2_3 )

		
		order0.save(update_fields=['jeans2_1','jeans2_2','jeans2_3'])
		
		return HttpResponse("save hoise may be")
	
	return render(request, 'jeans2.html')





