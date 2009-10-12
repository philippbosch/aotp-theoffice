from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.translation import ugettext as _

from attendance.models import OfficeDay



class OfficeDayForm(forms.ModelForm):
    paid = forms.BooleanField(required=False)
    user = forms.ModelChoiceField(User.objects, required=False, widget=forms.HiddenInput)
    class Meta:
        model = OfficeDay



class PaymentForm(forms.Form):
    amount = forms.IntegerField(help_text=_("Please pay only amounts that are dividable by 5."))



@login_required
def dashboard(request):
    if request.method == 'POST':
        form = OfficeDayForm(request.POST)
        form.fields['user'].initial = request.user.id
        if form.is_valid():
            if OfficeDay.objects.filter(user=request.user, day=request.POST['day']).count():
                request.user.message_set.create(message=_("Hey, you already stamped for %s!" % request.POST['day']))
            else:
                form.save()
                request.user.message_set.create(message=_("You've been at The Office on %s. Thanks for your visit!" % request.POST['day']))
            return HttpResponseRedirect(reverse('attendance_dashboard'))
    else:
        form = OfficeDayForm()
        form.fields['user'].initial = request.user.id
        form.fields['day'].initial = datetime.now()
    office_days = OfficeDay.objects.filter(user=request.user)
    to_pay = OfficeDay.objects.filter(user=request.user, paid=False).count() * 5
    payment_form = PaymentForm()
    return render_to_response('attendance/dashboard.html', {
        'form': form,
        'days': office_days,
        'to_pay': to_pay,
        'payment_form': payment_form,
    }, context_instance=RequestContext(request))


@login_required
def pay(request):
    form = PaymentForm(request.POST)
    if form.is_valid():
        amount = form.cleaned_data['amount']
        to_pay = OfficeDay.objects.filter(user=request.user, paid=False).count() * 5
        if amount > to_pay:
            request.user.message_set.create(message=_("That's more money than you have to pay. Paying in advance is not possible yet."))
            return HttpResponseRedirect(reverse('attendance_dashboard'))
        office_days = OfficeDay.objects.filter(user=request.user, paid=False).order_by('id')
        for day in office_days:
            if amount < 5:
                break
            day.paid = True
            day.save()
            amount = amount - 5
        return HttpResponseRedirect(reverse('attendance_dashboard'))
    else:
        request.user.message_set.create(message=_("Invalid amount!"))
        return HttpResponseRedirect(reverse('attendance_dashboard'))
