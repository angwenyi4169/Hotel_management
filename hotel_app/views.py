from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q
from .models import Category, Room, Booking
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, 'Your Account has been created! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

def book(request):
    if request.method == 'POST':
        query = request.POST.get('room')
        print(query)
    elif request.method == 'GET':
        #room, customer
        room_number = request.GET.get('room_number')
        user_name = request.user.get_username()
        if request.user.is_authenticated:
            customer = request.user
            room = Room.objects.get(room_number=room_number)
            if room.available:
                print('Room is available')
                booking = Booking(customer=customer, room=room)
                booking.save()
            else:
                print("Room Not available")

    return render(request, 'book.html')



# Create your views here.
# def search(request):
# 	template ='******'

# 	query = request.GET.get('q')
# 	if query:
# 		results = Post.object.filter(Q(it__contains=query) | Q(body__icontains=query))
# 	else:
# 		results = Post.object.filter(status = "Published")

# 	page = pagination(requests, results, num=1)

# 	context = {
# 		'items': = pages[0],
# 		'page_range': =pages[1],
# 		'query': query, 

# 	}
# 	return render(request, template, context)

	#in urls 
		#from .views import search
		#in urlpatters
			#url(r'^results/$', search, name = "search"),
 
# def get_queryset(request):
#     model = Category
#     template_name = 'search.html'
#     querytype = request.GET['category']
#     print(querytype)
#     object_list = Category.objects.filter(name=querytype) 
#     return object_list   

class SearchResultsView(ListView):
    model = Room
    template_name = 'search.html'
     
 
    def get_queryset(self):
      
       query = self.request.GET.get('category')
       object_list = Room.objects.filter(category__name=query).values('room_number', 'category__name', 'category__description', 'category__number_of_beds', 'category__price')
      # object_list = Category.objects.filter(Q(name__icontains=query))
       
       return object_list	
