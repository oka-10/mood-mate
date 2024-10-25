INSTALLED_APPS = [
    # ... other apps ...
    'rest_framework',
    'rest_framework.authtoken',
    'moodmate_app',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
