from django.core.mail import send_mail
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


def enviar_email_confirmacao(adocao):
    assunto = "Adocao realizada com sucesso!"
    conteudo = f"Parabéns por realizar a adocao do Pet {adocao.pet.nome} com o valor mensal de {adocao.valor}"
    remetente = env("EMAIL_HOST_USER")
    destinatario = [adocao.email]
    send_mail(assunto, conteudo, remetente, destinatario)
