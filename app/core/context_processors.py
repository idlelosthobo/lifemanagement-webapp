def software_information(request):
    information = {
        'name': 'Dandy',
        'description': 'An organizer to manage everything in your life',
        'version': '0.0.1a',
        'copyright': 'Epiphany Group',
        'author': 'Nathan Johnson',
    }
    return {'software': information}
