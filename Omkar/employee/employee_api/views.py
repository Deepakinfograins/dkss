from rest_framework.views import APIView

from employee.employee_api.serializers import (
    EmployeeSerializer
)

class EmployeeRegisterAPI(APIView):
    def post(self, request,*args, **kwargs):
        try:
            get_employee_data = request.data
            serializer = EmployeeSerializer(data = get_employee_data)
            if serializer.is_valid():
                serializer.save()
                context = {
                    'status':status.HTTP_200_OK,
                    'success':True,
                    'response':'hello world!'
                }
                return Response(context,status=status.HTTP_200_OK)

        except Exception as exception:
            context = {
                'status':status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)