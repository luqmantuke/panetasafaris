from django.shortcuts import render
from .forms import *
from .models import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from panetasafaris import settings
from .filters import *
from django.views.generic.list import ListView
from django.db.models import Q


def destination_list(request):
    tours = Destination.objects.all()
    template_name = 'destinations/destination_list.html'
    myFilter = TourFilter(request.GET, queryset=tours)
    dest = myFilter.qs
    subject = "Someone just requested a tour which you don't have."

    if request.method == "POST":

        form = BookingForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            tour_name = form.cleaned_data['tour_name']
            quantity = form.cleaned_data['quantity']
            message = form.cleaned_data['message']
            user_message = f'Customer "{full_name}" with the email "{email}" just booked a tour to  "{tour_name}" with quantity of {quantity} person/people and left a message "{message}" please contact him as soon as possible.'
            form.save()
            try:
                send_mail(subject, user_message, settings.EMAIL_HOST_USER, ['panetasafari@gmail.com'],
                          settings.FAIL_SILENTLY)

            except BadHeaderError:
                return HttpResponse('Invalid Header.')
            messages.success(request, f'Tour submission was successfully we shall contact you {full_name} shortly!')

            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
    else:
        form = BookingForm()

    return render(request, template_name, {'dests': dest,
                                           'myfilter': myFilter, 'bkform': form})


def destination_details(request, slug):
    query = Destination.objects.filter(slug__iexact=slug)
    book_subject = "Someone just booked a tour!!"
    if query.exists():
        query = query.first()
    else:
        return render(request, 'tkadventure/404.html', status=404)

    if request.method == "POST":

        form = BookingForm(request.POST)
        if form.is_valid():
            book_full_name = form.cleaned_data['full_name']
            book_email = form.cleaned_data['email']
            book_tour_name = form.cleaned_data['tour_name']
            book_quantity = form.cleaned_data['quantity']
            book_message = form.cleaned_data['message']
            book_user_message = f'Customer "{book_full_name}" with the email "{book_email}" just booked a tour to " " "{book_tour_name}" with quantity of " "  {book_quantity} person/people and left a message " " "{book_message}" please contact him as soon as possible'
            form.save()
            try:
                send_mail(book_subject, book_user_message, settings.EMAIL_HOST_USER, ['panetasafari@gmail.com'],
                          settings.FAIL_SILENTLY)

            except BadHeaderError:
                return HttpResponse('Invalid Header.')
            form.save()
            messages.success(request, f'Booking  was successfully we shall contact you shortly {book_full_name} thank you!')
            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
    else:
        form = BookingForm()

    context = {
        'destform': form,
        'dest': query
    }

    return render(request, 'destinations/destination_details.html', context)



