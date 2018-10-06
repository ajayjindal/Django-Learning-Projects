from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import product
from django.utils import timezone

# Create your views here.
def home(request):
	products = product.objects
	return render(request,'products/home.html', {'products' : products})

@login_required(login_url='/accounts/signup')
def create(request):
	if request.method=='POST':
		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
			pro = product()
			pro.title=request.POST['title']
			pro.body=request.POST['body']
			pro.url=request.POST['url']
			pro.icon=request.FILES['icon']
			pro.image=request.FILES['image']
			pro.pub_date = timezone.datetime.now()
			pro.hunter = request.user
			pro.save()
			return redirect('/products/' + str(pro.id))
		else:
			return render(request,'products/create.html',{'error':'all fields are required!'})	
	else:
		return render(request,'products/create.html')

def detail(request,product_id):
	pro = get_object_or_404(product,pk=product_id)
	return render(request,'products/detail.html',{'product':pro})

@login_required(login_url="/accounts/signup")
def upvote(request,product_id):
	if request.method=='POST':
		pro = get_object_or_404(product,pk=product_id)
		pro.votes_total +=1
		pro.save()
		return redirect('/products/' + str(pro.id))
	