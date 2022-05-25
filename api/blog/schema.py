import uuid
from graphene_django import DjangoObjectType
import graphene

from .models import Blog, Comment

class BlogType(DjangoObjectType):
    class Meta:
        model = Blog

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment 


class CreateBlog(graphene.Mutation):
    blog = graphene.Field(BlogType)

    class Arguments:
        title = graphene.String()
        content = graphene.String()
        published = graphene.Boolean()

    def mutate(self, info, title, content, published):
        author = info.context.user
        b = Blog(title=title, content=content, published=published, author=author)
        b.save()
        return CreateBlog(blog=b)

class EditBlog(graphene.Mutation):
    blog = graphene.Field(BlogType)

    class Arguments:
        id = graphene.String()
        title = graphene.String()
        content = graphene.String()
    
    def mutate(self, info, id, title, content):
        id = uuid.UUID(id)

        b = Blog.objects.get(id=id)
        b.title = title
        b.content = content
        b.save()

        return EditBlog(blog=b)

class PublishBlog(graphene.Mutation):
    blog = graphene.Field(BlogType)

    class Arguments:
        id = graphene.String()
        published = graphene.Boolean()

    def mutate(self, info, id, published):
        id = uuid.UUID(id)

        b = Blog.objects.get(id=id)
        b.published = published
        b.save()

        return PublishBlog(blog=b)

class CreateComment(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        content = graphene.String()
        blog = graphene.String()
    
    def mutate(self, info, content, blog):
        author = info.context.user
        blog = Blog.objects.get(id=uuid.UUID(blog))
        c = Comment(content=content, blog=blog, author=author)
        c.save()
        return CreateComment(comment=c)

# class Approve(graphene.Mutation):


class Mutation(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    edit_blog = EditBlog.Field()
    publish_blog = PublishBlog.Field()
    create_comment = CreateComment.Field()


class Query(graphene.ObjectType):
    blogs = graphene.List(BlogType)
    blog_by_id = graphene.List(BlogType, id=graphene.String())
    comments_by_blog = graphene.List(CommentType, blog=graphene.String())


    def resolve_blogs(self, info):
        return Blog.objects.all()
    
    def resolve_blog_by_id(self, info, id):
        b = Blog.objects.filter(id=uuid.UUID(id))
        return b
    
    def resolve_comments_by_blog(self, info, blog):
        return Comment.objects.filter(blog=uuid.UUID(blog))


schema = graphene.Schema(query=Query, mutation=Mutation)