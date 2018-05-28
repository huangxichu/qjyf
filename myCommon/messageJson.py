from rest_framework import serializers
class MessageJson:
    status = 'SUCCESS'#FAILED
    data = {}

    def success(self):
        self.status = 'SUCCESS'

    def failed(self):
        self.status = 'FAILED'