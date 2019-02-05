from django_elasticsearch_dsl import DocType, Index
from blog.models import Post

posts=Index('posts')

@posts.doc_type
class PostDocument(DocType):
    class Meta:
        model = Post

        fields=[
            'title',
            'id',
            'img',
            'content',
        ]
