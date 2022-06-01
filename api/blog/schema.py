from statistics import mode
from unicodedata import category
import uuid
from graphene_django import DjangoObjectType
from graphql import GraphQLError
import graphene
from graphql_jwt.decorators import login_required
from django.db.models import Q

from .models import Blog, Category, Comment

class BlogType(DjangoObjectType):
    class Meta:
        model = Blog

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment 

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        title = graphene.String()
    
    def mutate(self, info, title):
        cat = Category(title=title)
        cat.save()
        return CreateCategory(category=cat)

class CreateBlog(graphene.Mutation):
    blog = graphene.Field(BlogType)

    class Arguments:
        title = graphene.String()
        content = graphene.String()
        category = graphene.String()
        published = graphene.Boolean()

    @login_required
    def mutate(self, info, title, content, category, published):
        if info.context.user.is_active == False:
            raise GraphQLError('Your id has been deactivated!')
        
        print("Is Author", info.context.user.author )
        if info.context.user.author == False:
            raise GraphQLError('You are not an author')

        author = info.context.user
        category = Category.objects.get(id=uuid.UUID(category))
        b = Blog(title=title, content=content, category=category, published=published, author=author)
        b.save()
        return CreateBlog(blog=b)

class EditBlog(graphene.Mutation):
    blog = graphene.Field(BlogType)

    class Arguments:
        id = graphene.String()
        title = graphene.String()
        content = graphene.String()
    
    @login_required
    def mutate(self, info, id, title, content):
        id = uuid.UUID(id)

        b = Blog.objects.get(id=id)
        if(b.author == info.context.user):
            b.title = title
            b.content = content
        b.save()

        return EditBlog(blog=b)

class PublishBlog(graphene.Mutation):
    blog = graphene.Field(BlogType)

    class Arguments:
        id = graphene.String()
        published = graphene.Boolean()

    @login_required
    def mutate(self, info, id, published):
        id = uuid.UUID(id)

        b = Blog.objects.get(id=id)

        # Publish only blog auther is the one wanting to publish
        if(b.author == info.context.user):
            b.published = published
            b.save()
            return PublishBlog(blog=b)
        else:
            raise GraphQLError('You are not author!')

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

class Approve(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        id = graphene.String()
        approved = graphene.Boolean()

    @login_required
    def mutate(self, info, id, approved):
        id = uuid.UUID(id)

        c = Comment.objects.get(id=id)

        # Publish only blog auther is the one wanting to publish
        if(c.blog.author == info.context.user):
            c.approved = approved
            c.save()
            return PublishBlog(comment=c)
        else:
            raise GraphQLError('You are not the blogs author!')

class Mutation(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    edit_blog = EditBlog.Field()
    publish_blog = PublishBlog.Field()
    create_comment = CreateComment.Field()
    create_category = CreateCategory.Field()

class Query(graphene.ObjectType):
    blogs = graphene.List(
        BlogType,
        search=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int(),
    )
    blog_by_id = graphene.List(BlogType, id=graphene.String())
    comments_by_blog = graphene.List(CommentType, blog=graphene.String())
    categories = graphene.List(CategoryType)

    # Returns published blogs
    def resolve_blogs(self, info, search=None, first=None, skip=None, **kwargs):
        blogToReturn = Blog.objects.filter(published = True)

        if search:
            filter = (
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )
            blogToReturn = blogToReturn.filter(filter)

        if skip:
            blogToReturn = blogToReturn[skip:]

        if first:
            blogToReturn = blogToReturn[:first]

        return blogToReturn
    
    def resolve_blog_by_id(self, info, id):
        b = Blog.objects.filter(id=uuid.UUID(id)).filter(published=True)
        b = b[:1]
        return b

    # Returns Approved Commens of a Blog
    def resolve_comments_by_blog(self, info, blog):
        return Comment.objects.filter(blog=uuid.UUID(blog)).filter(approved=True)

    def resolve_categories(self, info):
        categoriesToReturn = Category.objects.all()
        return categoriesToReturn

schema = graphene.Schema(query=Query, mutation=Mutation)