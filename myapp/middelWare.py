def simple_middleware(get_response):
    def middleware(request):
        # code
        print('before is exicuted in middleware')
        respose = get_response(request)
        # code
        print('after is executed in middleware')
        
        return respose
    return middleware