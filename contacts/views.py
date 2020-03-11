from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check user already query
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this listing")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id,
                          name=name, phone=phone, email=email, user_id=user_id)
        contact.save()
        # email sending
        send_mail(
            'Property Listing Inquery',
            'There has been an inquery for '+listing,
            'tecnicasol999@gmail.com',
            [realtor_email,'manjeetkr2017@gmail.com'],
            fail_silently=False
        )

        messages.success(
            request, 'Your request has been submmited, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)

    return
