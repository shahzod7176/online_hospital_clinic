REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 1
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Online Clinic Hospital",
    "DESCRIPTION": """\
    Hospital 103🏥
""",
    "VERSION": "1.0.0",
}
