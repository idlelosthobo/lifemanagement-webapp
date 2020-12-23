def software_information(request):
    information = {
        'name': 'Life Management',
        'description': 'A place to manage everything',
        'version': '0.0.1a',
        'copyright': 'Epiphany Group',
    }
    return {'software': information}
