from rest_framework.views import exception_handler

def mycustomErrorHandler(exc,contex):
    print(exc,contex)
    response = exception_handler(exc, contex)
    if response:
        data = {
            "status_code": response.status_code,
            "description": response.data.get('detail'),
            'message': response.data.get('message'),
            'watermark': 'error find'
        }
        
        response.data = data


    return response