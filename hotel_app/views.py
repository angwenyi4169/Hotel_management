from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.shortcuts import render
from django.db.models import Q
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
 
def get_queryset(request):
    model = Category
    template_name = 'search.html'
    querytype = request.GET['category']
    object_list = Category.objects.filter(Q(name__icontains=querytype))   
    return object_list   
