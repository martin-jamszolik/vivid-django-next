from django.shortcuts import render
from django.http import HttpResponse
from estimations.models import Project, Proposal
from rest_framework import viewsets
from rest_framework import permissions
from estimations.serializers import ProjectSerializer,ProposalSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


class ProposalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Proposals to be viewed or edited.
    """
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    permission_classes = [permissions.AllowAny]
