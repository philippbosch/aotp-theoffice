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



@login_required
def dashboard(request):
    if request.method == 'POST':
        post = request.POST.copy()
        form = init_form(request.user, post)
        if form.is_valid():
            if OfficeDay.objects.filter(user=request.user, day=request.POST['day']).count():
                request.user.message_set.create(message=_("Hey, you already stamped for %s!" % request.POST['day']))
            else:
                form.save()
                request.user.message_set.create(message=_("You've been at The Office on %s. Thanks for your visit!" % request.POST['day']))
            return HttpResponseRedirect(reverse('attendance_dashboard'))
    else:
        form = init_form(request.user)
        form.fields['day'].initial = datetime.now()
    office_days = OfficeDay.objects.filter(user=request.user)
    return render_to_response('attendance/dashboard.html', {
        'form': form,
        'days': office_days,
    }, context_instance=RequestContext(request))



def init_form(user, data=None):
    form = OfficeDayForm(data)
    form.fields['user'].initial = user.id
    return form