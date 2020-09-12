from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from user.models import User
from .models import *
from cart.models import *
from .forms import ImageForm
# Create your views here.

def index(request): 
    if request.user.is_authenticated:
        user = User.objects.get(email = request.user).user_type
        if user == 2:
            context = {
                "name": request.user.first_name,
                "restaurant": Seller.objects.get(user=request.user).restaurant.name
            }
            return render(request, "seller/index.html", context)
        else:
            logout(request)
    return HttpResponseRedirect(reverse('register_seller'))

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email).user_type
            print(user)
            if user == 2:
                user = authenticate(request, email=email, password=password)
                
                if user is not None:
                    login(request, user)
                    restaurant = Seller.objects.get(user=user).restaurant
                    return  HttpResponseRedirect(reverse('seller_index'))
                else:
                    messages.warning(request, "Please provide correct email and password.")
                    return render(request, 'seller/login.html')
            else:
                messages.warning(request, "This email may belong to someone else.")  
                return render(request, 'seller/login.html')
        except User.DoesNotExist:
            messages.warning(request, "Please register your restaurant first")
            return render(request, 'seller/login.html')
    else:
        return render(request, 'seller/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("register_seller"))

def register(request):

    if request.method == 'POST':

        name = request.POST.get('restaurant_name')
        address = request.POST.get('address')

        
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        category = request.POST.get("category_restaurant")

        form = ImageForm(request.FILES)
 
        if form.is_valid():
            picture = request.FILES.get('picture')


        if password == confirm_password:
            try:
                if  User.objects.get(email=email):
                    messages.error(request, "Username or email already exists.")
                    context = {
                        "category": Restaurant_category, 
                        "form": ImageForm
                    }
                    return render(request, 'seller/signup.html', context)
            except User.DoesNotExist:
                user = User.objects.create_user(user_type=2, email=email, first_name=first_name, last_name=last_name, password=password)
                restaurant = Restaurant.objects.create(name=name, address=address, category=category, picture=picture)
                seller = Seller.objects.create(user=user,phone_number=phone_number, restaurant=restaurant)
                messages.success(request, "Account created")

                return HttpResponseRedirect(reverse('login_seller'))
        else:
            messages.error(request, "Passwords do not match")
            context = {
                "category": Restaurant_category, 
                "form": ImageForm
            }
            return render(request, 'seller/signup.html', context)
    else:
        if not request.user.is_authenticated:
            context = {
                "category": Restaurant_category,
                "form": ImageForm
            }
            return render(request, 'seller/signup.html', context)
        else:
            return HttpResponseRedirect(reverse('seller_index'))

def additem(request):
    glutten_freeornot = False
    customizableornot = False 
    context={
        "form" : ImageForm,
        "nationality": Restaurant_category,
        "dish_category": Dish_category
    }

    if request.method == 'POST':
        dish_name = request.POST.get('dish_name')
        summary = request.POST.get('dish_summary')
        nationality = request.POST.get('dish_nationality')
        no_of_serving = request.POST.get('dish_no_of_serving')
        picture = request.POST.get('dish_picture')
        category = request.POST.get('dish_category')
        glutten_free = request.POST.get('dish_glutten_free')
        customizable = request.POST.get('dish_customizable')
        price = request.POST.get('dish_price')

        if glutten_free == True:
            glutten_freeornot = True

        if customizable == True:
            customizableornot = True
        
        form = ImageForm(request.FILES)
        
        if form.is_valid():
            picture = request.FILES.get('picture')
            
        user = Seller.objects.get(user=request.user)
        restaurant = Seller.objects.get(user=user).restaurant
        print(restaurant)

        currentDish = Dish.objects.create(restaurant=restaurant, name= dish_name, summary=summary, nationality=nationality, category=category, no_of_serving=no_of_serving, picture=picture, glutten_free=glutten_freeornot, customizable=customizableornot, seller=user, price=price)
        context = {
            "message" : "Item added!", 
        }
        dish_id = currentDish.id
        return HttpResponseRedirect(reverse("redirectitem", args=(dish_id,)))

    else:
        return render(request, 'seller/additem.html', context)
    
def getlist(request):
    itemlist = []
    seller = Seller.objects.get(user=request.user)
    dishes = seller.cooks.all()
    count = str(dishes.count())

    for i in range(0, int(count)):
        itemlist.append({"dish_id": int(dishes[i].id), "dish_name": str(dishes[i].name)})
        print(itemlist)
    return JsonResponse({
        "itemlist": itemlist})

def getitem(request, dish_id):
    seller = Seller.objects.get(user=request.user)
    dish = seller.cooks.get(pk=dish_id)
    glutten_free = "No"
    customizable = "No"
    if dish.glutten_free == True:
        glutten_free = "Yes" 
    
    if dish.customizable == True:
        customizable = "Yes" 

    item = {"name" : str(dish.name), "summary" : str(dish.summary), "nationality" : str(dish.nationality), "no_of_serving" : dish.no_of_serving,"picture" : str(dish.picture), "category" : str(dish.category) , "glutten_free" : glutten_free, "customizable" : customizable, "price":float(dish.price)}
    return JsonResponse({
        "item": item
    })

def redirectitem(request, dish_id):
    if request.method == 'GET':    
        glutten_freeornot = "No"
        customizableornot = "No" 
        seller = Seller.objects.get(user=request.user)
        dish = seller.cooks.get(pk=dish_id)
            
        if dish.glutten_free == True:
            glutten_freeornot = "Yes"

        if dish.customizable == True:
            customizableornot = "Yes"
        
        context = {
            "dish_id": int(dish.id),
            "name" : str(dish.name), 
            "summary" : str(dish.summary), 
            "nationality" : str(dish.get_nationality_display()), 
            "no_of_serving" : dish.no_of_serving,
            "picture" : str(dish.picture), 
            "dish_category" : str(dish.get_category_display()) , 
            "glutten_free" : str(glutten_freeornot), 
            "customizable" : str(customizableornot),
            "price":float(dish.price),
            "dish": dish
        }
    return render(request, 'seller/item.html', context)

def updateitem(request, dish_id):
    seller = Seller.objects.get(user=request.user)
    dish = seller.cooks.get(pk=dish_id)
    
    form = ImageForm

    if request.method == 'GET':    
        glutten_freeornot = "No"
        customizableornot = "No" 
        seller = Seller.objects.get(user=request.user)
        dish = seller.cooks.get(pk=dish_id)
    
            
        if dish.glutten_free == True:
            glutten_freeornot = "Yes"

        if dish.customizable == True:
            customizableornot = "Yes"

        
        context = {
            "dish_id": int(dish.id),
            "name" : str(dish.name), 
            "summary" : str(dish.summary), 
            "nationality" : str(dish.nationality), 
            "no_of_serving" : dish.no_of_serving,
            "picture" : str(dish.picture), 
            "category" : str(dish.category) , 
            "glutten_free" : str(glutten_freeornot), 
            "customizable" : str(customizableornot),
            "dish" : dish,
            "price":float(dish.price),
            "form" : form,
            "nationality": Restaurant_category,
            "dish_category": Dish_category
        }
    return render(request, 'seller/updateitem.html', context)

def itemupdated(request, dish_id):
    glutten_freeornot = False
    customizableornot = False 
    
    if request.method == 'POST':
        name = request.POST.get('dish_name')
        summary = request.POST.get('dish_summary')
        nationality = request.POST.get('dish_nationality')
        no_of_serving = request.POST.get('dish_no_of_serving')
        #picture = request.POST.get('dish_picture')
        category = request.POST.get('dish_category')
        glutten_free = request.POST.get('dish_glutten_free')
        customizable = request.POST.get('dish_customizable')

        if glutten_free == "Yes":
            glutten_freeornot = True

        if customizable == "Yes":
            customizableornot = True

        form = ImageForm(request.FILES)
 
        if form.is_valid():
            picture = request.FILES.get('picture')

        seller = Seller.objects.get(user=request.user)
        dish = seller.cooks.get(pk=dish_id)
        

        dish.name = name 
        dish.summary = summary
        dish.nationality = nationality 
        dish.no_of_serving = no_of_serving
        dish.picture = picture 
        dish.category =  category 
        dish.glutten_free = glutten_freeornot
        dish.customizable = customizableornot
        dish.picture = picture


        dish.save()



    return HttpResponseRedirect(reverse("redirectitem", args=(dish_id,)))

def deleteitem(request, dish_id):
    seller = Seller.objects.get(user=request.user)
    dish = seller.cooks.get(pk=dish_id)    
    dish.delete()

    return HttpResponseRedirect(reverse("seller_index"))

def display_orders(request):
    orders = Order.objects.filter(order_items__product__dish__seller__user = request.user)
    delivered = orders.filter(status=True).count()
    pending = orders.filter(status=False).count()
    context = {
        "orders": orders,
        "delivered": delivered, 
        "pending": pending
    }
    return render(request, "seller/dashboard.html", context)


'''
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})  
'''                                                                                                                                                                                                                                                                       




