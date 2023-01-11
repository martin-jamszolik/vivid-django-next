from rest_framework import serializers

from estimations.models import Project, Proposal


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'name', 'status']


class ProposalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proposal
        fields = ['url', 'name','date','prop_type','project']