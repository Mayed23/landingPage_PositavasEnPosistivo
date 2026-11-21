
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    contexto = {}

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        correo = request.POST.get('correo', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        pais = request.POST.get('pais', '').strip()
        mensaje = request.POST.get('mensaje', '').strip()
        consentimiento = request.POST.get('consentimiento')

        if not all([nombre, correo, telefono, pais, consentimiento]):
            contexto['error_formulario'] = (
                'Por favor, completa todos los campos obligatorios '
                'y acepta las condiciones de privacidad.'
            )
        else:
            asunto = 'Nueva solicitud para unirse a Positivas en Positivo'

            contenido = f"""
Has recibido una nueva solicitud de incorporación a la comunidad.

Nombre: {nombre}
Correo electrónico: {correo}
WhatsApp: {telefono}
País: {pais}

Mensaje:
{mensaje if mensaje else 'No se ha incluido ningún mensaje.'}
"""

            try:
                send_mail(
                    asunto,
                    contenido,
                    settings.DEFAULT_FROM_EMAIL,
                    ['positivasenpositivo@gmail.com'],
                    fail_silently=False,
                )

                contexto['solicitud_enviada'] = True

            except Exception:
                contexto['error_formulario'] = (
                    'No pudimos enviar tu solicitud en este momento. '
                    'Por favor, inténtalo más tarde.'
                )


    return render(request, 'landing/home.html', contexto)

def comunidad(request):
    contexto = {}

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        correo = request.POST.get('correo', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        pais = request.POST.get('pais', '').strip()
        mensaje = request.POST.get('mensaje', '').strip()
        consentimiento = request.POST.get('consentimiento')

        if not all([nombre, correo, telefono, pais, consentimiento]):
            contexto['error_formulario'] = (
                'Por favor, completa los campos obligatorios.'
            )
        else:
            asunto = f'Nueva solicitud de comunidad: {nombre}'

            contenido = f"""
Nueva solicitud recibida desde Positivas en Positivo.

Nombre: {nombre}
Correo: {correo}
WhatsApp: {telefono}
País: {pais}

Mensaje:
{mensaje}
"""

            try:
                send_mail(
                    asunto,
                    contenido,
                    settings.DEFAULT_FROM_EMAIL,
                    ['positivasenpositivo@gmail.com'],
                    fail_silently=False,
                )
                contexto['solicitud_enviada'] = True

            except Exception:
                contexto['error_formulario'] = (
                    'No pudimos enviar tu solicitud en este momento. '
                    'Por favor, inténtalo más tarde.'
                )

    return render(request, 'landing/comunidad.html', contexto)