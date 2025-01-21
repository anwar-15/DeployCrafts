from django.core.mail import send_mail
from django.urls import reverse
from django.core.signing import TimestampSigner
#from .views import verify_email
signer = TimestampSigner()

class VerificationEmail():

    def send_verification_email(self, user):
        token = signer.sign(user.email)
        verification_url = reverse('authenticate:verify_email', args=[token])
        full_url = f"http://127.0.0.1:8000{verification_url}"
        send_mail(
            'Verify your email',
            f'Click the link to verify your email: {full_url}',
            'anwar15sayed@gmail.com',
            [user.email],
            fail_silently=False,
        )