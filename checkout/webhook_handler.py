from django.http import HttpResponse


class StripWH_Handler:
    """
    Handle Strip Webhooks
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        handle generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)