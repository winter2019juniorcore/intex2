from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return request.dmp.render('newuser.html', {
        'form': form,
    })

class MyForm(forms.Form):
    '''An example form'''
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError('invalid username or password.')
        return self.cleaned_data