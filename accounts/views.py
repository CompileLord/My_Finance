from django.urls import reverse_lazy
import random
from django.views.generic import CreateView, FormView
from django.core.mail import send_mail
from .models import User, VerificationCode
from .forms import RegisterForm, VerifyCodeForm


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('confirm_email')
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        code = str(random.randint(100000,999999))
        VerificationCode.objects.create(user=user, code=code)
        send_mail(f'Your code {code}', 'arendaovosej639@gmail.com', [user.email])
        self.request.session['pending_user_id'] = user.id
        return super().form_valid(form)

class VerificationCode(FormView):
    form_class = VerifyCodeForm
    template_name = 'verify.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        user_code = form.cleaned_data['code']
        user_id = self.request.session.get('pending_user_id')
        try:
            db_record = VerificationCode.objects.get(user_id=user_id, code=user_code)
            user = db_record.user
            user.is_active = True
            user.save()
            db_record.delete() 
            return super().form_valid(form)
        except VerificationCode.DoesNotExist:
            form.add_error('code', 'Incorrect code!')
            return self.form_invalid(form)

