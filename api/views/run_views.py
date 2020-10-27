from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.run import Run
from ..serializers import RunSerializer, UserSerializer

# Create your views here.
class Runs(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = RunSerializer
    def get(self, request):
        """Index request"""
        # Get all the runs:
        # runs = Run.objects.all()
        # Filter the runs by owner, so you can only see your owned runs
        runs = Run.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = RunSerializer(runs, many=True).data
        return Response({ 'runs': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['run']['owner'] = request.user.id
        # Serialize/create run
        run = RunSerializer(data=request.data['run'])
        # If the run data is valid according to our serializer...
        if run.is_valid():
            # Save the created run & send a response
            run.save()
            return Response({ 'run': run.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(run.errors, status=status.HTTP_400_BAD_REQUEST)

class RunDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the run to show
        run = get_object_or_404(Run, pk=pk)
        # Only want to show owned runs?
        if not request.user.id == run.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this run')

        # Run the data through the serializer so it's formatted
        data = RunSerializer(run).data
        return Response({ 'run': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate run to delete
        run = get_object_or_404(Run, pk=pk)
        # Check the run's owner agains the user making this request
        if not request.user.id == run.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this run')
        # Only delete if the user owns the run
        run.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['run'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['run'].get('owner', False):
            del request.data['run']['owner']

        # Locate Run
        # get_object_or_404 returns a object representation of our Run
        run = get_object_or_404(Run, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == run.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this run')

        # Add owner to data object now that we know this user owns the resource
        request.data['run']['owner'] = request.user.id
        # Validate updates with serializer
        data = RunSerializer(run, data=request.data['run'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
