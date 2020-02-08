from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator  ## For Pagination
from .choices import price_choices, bedroom_choices, state_choices   ## no need listings, because already imported Listing


# Create your views here.

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

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'listings/search.html', context)