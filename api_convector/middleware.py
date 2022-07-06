import traceback
from datetime import datetime


class LogsMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        response = self._get_response(request)
        return response

    def process_exception(self, request, exception):
        print(f'ERROR: Exception is {exception}!')
        with open(f"logs/{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.log", "w") as file:
            file.write(traceback.format_exc())
