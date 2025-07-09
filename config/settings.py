import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta de segurança. MANTENHA ISSO SECRETO EM PRODUÇÃO!
# Para desenvolvimento, pode ser uma string fixa. Em produção, use uma variável de ambiente.
SECRET_KEY = 'django-insecure-sua_chave_secreta_aqui_substitua_por_algo_complexo' # **Importante: Altere isso!**

# Em produção, DEVE ser False por segurança e performance.
DEBUG = True

# Em desenvolvimento, geralmente '127.0.0.1' e 'localhost'.
# Em produção, adicione os domínios do seu site (ex: '.ecoride.com.br').
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# --- Definição dos Aplicativos (Apps) Instalados ---
# Adicione aqui todos os aplicativos Django que você criou ou instalou.

INSTALLED_APPS = [
    # Aplicativos padrão do Django
    'django.contrib.admin',        # Painel de administração
    'django.contrib.auth',         # Sistema de autenticação
    'django.contrib.contenttypes', # Tipos de conteúdo
    'django.contrib.sessions',     # Gerenciamento de sessões
    'django.contrib.messages',     # Mensagens flash
    'django.contrib.staticfiles',  # Gerenciamento de arquivos estáticos

    # Meus aplicativos locais
    'vehicles', # Seu app de veículos!

    # Aplicativos de terceiros (que você irá instalar)
    'rest_framework',              # Django REST Framework
    'corsheaders',                 # Para lidar com requisições CORS do frontend Angular
    # 'rest_framework_simplejwt',    # Para autenticação JWT (futuro)
]

# --- Middleware (Processamento de Requisições HTTP) ---
# Ordem é importante!

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Adicione CorsMiddleware ANTES de CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- Configuração de URLs ---

ROOT_URLCONF = 'core.urls' # Aponta para o arquivo de URLs principal do seu projeto

# --- Configuração de Templates ---

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Onde o Django vai procurar por templates HTML
        'APP_DIRS': True, # Permite que os apps forneçam seus próprios templates
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- Configuração WSGI (Web Server Gateway Interface) ---
# Usado para servir sua aplicação em produção.

WSGI_APPLICATION = 'config.wsgi.application'

# --- Configuração do Banco de Dados (PostgreSQL) ---
# Substitua 'seu_usuario', 'sua_senha', 'seu_banco' e 'seu_host' pelos seus dados reais.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecoride_db',     # Nome do seu banco de dados PostgreSQL
        'USER': 'ecoride_user',   # Seu usuário do PostgreSQL
        'PASSWORD': 'admin',      # Sua senha do PostgreSQL
        'HOST': 'localhost',      # Onde o banco de dados está rodando (pode ser um IP ou hostname)
        'PORT': '5432',           # Porta padrão do PostgreSQL
    }
}

# --- Validação de Senhas (Recomendado para Segurança) ---

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# --- Internacionalização ---

LANGUAGE_CODE = 'pt-br' # Altere para o idioma do seu projeto

TIME_ZONE = 'America/Sao_Paulo' # Fuso horário do seu projeto (Ex: 'UTC', 'America/New_York')

USE_I18N = True # Habilita suporte a internacionalização

USE_TZ = True # Habilita suporte a fusos horários

# --- Configuração de Arquivos Estáticos (CSS, JS, Imagens) ---

STATIC_URL = 'static/' # URL para servir arquivos estáticos

# Onde o Django vai coletar todos os arquivos estáticos para deploy (geralmente 'staticfiles/')
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Diretórios adicionais onde o Django pode encontrar arquivos estáticos
STATICFILES_DIRS = [
    # BASE_DIR / 'static_dev', # Exemplo: uma pasta 'static_dev' na raiz do projeto para arquivos estáticos globais
]

# --- Configuração de Arquivos de Mídia (Uploads de Usuários) ---
# Usado para arquivos como as imagens dos veículos que serão carregadas pelos usuários.

MEDIA_URL = '/media/' # URL para servir arquivos de mídia (uploads)
MEDIA_ROOT = BASE_DIR / 'media' # Diretório físico onde os arquivos de mídia serão armazenados

# --- Configuração do Django REST Framework (DRF) ---

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny', # Permite acesso a todos os endpoints por padrão
        # Altere isso para 'rest_framework.permissions.IsAuthenticated' para exigir login
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication', # Para autenticação JWT
        'rest_framework.authentication.SessionAuthentication', # Autenticação baseada em sessão (útil para o Admin)
        'rest_framework.authentication.BasicAuthentication',   # Autenticação básica
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10 # Número de itens por página nas suas APIs paginadas
}

# --- Configurações CORS (Cross-Origin Resource Sharing) ---
# Essencial para permitir que seu frontend Angular (rodando em uma porta diferente)
# se comunique com seu backend Django.

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",  # A porta padrão do Angular em desenvolvimento
    # "http://127.0.0.1:4200",
    # Adicione outras origens do seu frontend Angular (ex: ambiente de produção)
]

# Ou, se preferir permitir de todas as origens (MENOS SEGURO para produção!):
# CORS_ALLOW_ALL_ORIGINS = True

# Se você precisar permitir cookies, credenciais, etc., defina:
CORS_ALLOW_CREDENTIALS = True

# --- Endereço de Email (Exemplo) ---
# Útil para o Django enviar e-mails de erro ou de recuperação de senha.

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # Envia emails para o console (desenvolvimento)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # Para produção, configurar SMTP real
# EMAIL_HOST = 'smtp.seuservidor.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'seu_email@dominio.com'
# EMAIL_HOST_PASSWORD = 'sua_senha_email'