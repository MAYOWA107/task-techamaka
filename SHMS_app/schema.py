import graphene
from graphene_django import DjangoObjectType

from SHMS_app.models import Hospital_Info



class Hospital_InfoType(DjangoObjectType):
    class Meta:
        model = Hospital_Info
        fields = '__all__'



class Query(graphene.ObjectType):
    all_info = graphene.List(Hospital_InfoType)

    def resolve_all_info(self, info):
        return Hospital_Info.objects.all()
    


class Create_one(graphene.Mutation):
    one = graphene.Field(Hospital_InfoType)

    class Arguments:
        name = graphene.String()
        email = graphene.String()

    def mutate(self, info, name, email):
        one = Hospital_Info(name= name, email= email)
        one.save()
        return Create_one()
    

class Mutation(graphene.ObjectType):
    create_one = Create_one.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)