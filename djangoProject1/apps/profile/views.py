from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from djangoProject1.apps.profile.models import UserProfile
from djangoProject1.apps.utils import success_response, error_response


class UserProfileView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            data = {
                'first_name': user_profile.first_name,
                'last_name': user_profile.last_name,
                'phone_number': user_profile.phone_number,
                'gender': user_profile.gender,
                'username': user_profile.user.username
            }
            response = success_response(status_code, data, 'User profile retrieved successfully')

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = error_response(status_code, 'Request Failed', str(e))
        return Response(response, status=status_code)
