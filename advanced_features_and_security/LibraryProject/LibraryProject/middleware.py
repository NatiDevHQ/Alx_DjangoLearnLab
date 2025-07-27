from django.utils.deprecation import MiddlewareMixin
class ContentSecurityPolicyMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Content-Security-Policy'] = "default-src 'self'"
        return response
