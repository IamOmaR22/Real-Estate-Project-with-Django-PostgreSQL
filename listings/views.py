from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator  ## For Pagination
from .choices import price_choices, bedroom_choices, state_choices   ## no need listings, because already imported Listing



def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)  ## Check or uncheck in admin area

    ### Pagination Start ###
    paginator = Paginator(listings, 6)   ## how much item i want to show in each page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    ### Pagination End ###

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


##----## This is for single listing (More Info Button) ##----##
def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)   ## if page doesn't exist, it will show page not found(error message)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)



def search(request):

    queryset_list = Listing.objects.order_by('-list_date')  ## Get all of the listings

    #### Keywords (Search/Filtering by using keyword of search box) ####
    if 'keywords' in request.GET:   ## Check keyword exist
        keywords = request.GET['keywords']  ## Get the actual form value

        if keywords: ## To make sure it's not an empty string
            ##--## Keywords for descriptions(description__icontains, it will take the whole paragraph) ##--##
            queryset_list = queryset_list.filter(description__icontains=keywords) ##icontains, it takes whole paragraph


    #### City (Search/Filtering by using City of search box) ####
    if 'city' in request.GET:   ## Check city exist
        city = request.GET['city']
        if city:   ## iexact is case insensitive and exact is case sensitive
            queryset_list = queryset_list.filter(city__iexact=city) ##iexact, it takes only the exact name of city

    #### State ####
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    #### Bedrooms ####
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) ## Suppose, 4 bedrooms(Upto). lte means less then or equalto. if greater then it won't show

    #### Price ####
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

### keywords, city, state, bedrooms, price all they are the name( name = keywords etc ) in select tags in html

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET     ### Preserving form input
    }

    return render(request, 'listings/search.html', context)
