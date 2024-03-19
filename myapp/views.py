import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
 logger.info('Index page accessed')
 return HttpResponse("Hello, world!")


def about(request):
 try:
  # some code that might gaise an excepsion
  result = 1 / 0
 except Exception as e:
  logger.exception(f'Error in about page: {e}')
  return HttpResponse("Dops, something went wrong.")
 else:
  logger.debug('About page accessed')
  return HttpResponse("this is the about page.")

