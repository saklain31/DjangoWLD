from django.shortcuts import render
from userData.models import * 
from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect


# Create your views here.

def saveTempOrder(request):
	if request.method == 'POST':    
		username = request.POST.get("username")
		email = request.POST.get("email")
		zipcode = request.POST.get("zipcode")
		order = tempOrder()
		order.name = username
		order.zipcode = zipcode
		order.gmail = email
		order.orderID = 'ord8181'
		order.userID = 'user89110'
		order.save()

		return HttpResponsePermanentRedirect("/firstpair/")

	return render(request, 'basicData.html')

def getJeans1(request):
	print(request.method)
	if request.method == 'POST':
		order = tempOrder.objects.filter(orderID='ord8181')
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
	if request.method == 'POST':
		order = tempOrder.objects.filter(orderID='ord8181')
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





