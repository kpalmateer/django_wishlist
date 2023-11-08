from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

# Create your views here.
def place_list(request):

    # if the request type is a POST request (the add button is pushed), execute the code to add the location, then reload the list
    if request.method == 'POST':
        # create new place
        form = NewPlaceForm(request.POST)
        place = form.save() # create model object from form
        if form.is_valid(): # validation against DB constraints
            place.save() # save place to database
            return redirect('place_list') # reload homepage

    places = Place.objects.filter(visited = False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

def about(request):
    author = 'Kyle Palmateer'
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})

def places_visited(request):
    visited = Place.objects.filter(visited = True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

def place_was_visited(request, place_pk):
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk) # request the place from the dictionary using the pk, return 404 if not found
        place.visited = True # set visited to True
        place.save() 

    return redirect('place_list')