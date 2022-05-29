> Blogs

```graphql
query {
  blogs(first: 2, skip: 0, search: "content") {
    id
    title
    content
    published
  }
}
```

> Blog By Id

```graphql
query {
  blogById(id: "f66135da-0b87-4420-9a48-1fbd6ae316f9") {
    id
    content
    created
  }
}
```

> Blog By Id with all comments of it

```graphql
query {
  blogById(id: "f66135da-0b87-4420-9a48-1fbd6ae316f9") {
    id
    content
    created
    commentSet {
      id
      content
    }
  }
}
```

> Comments of a blog

```graphql
query {
  commentsByBlog(blog: "f66135da-0b87-4420-9a48-1fbd6ae316f9") {
    id
    content
  }
}
```

> Create Blog

```graphql
mutation {
  createBlog(title: "Another Blog", content: "Blog Content", published: false) {
    blog {
      id
      content
    }
  }
}
```

> Update Blog

```graphql
mutation {
  editBlog(
    id: "f66135da-0b87-4420-9a48-1fbd6ae316f9"
    title: "New title"
    content: "New blog content"
  ) {
    blog {
      id
      title
      content
      created
      updated
    }
  }
}
```

> Publish Blog

```graphql
mutation {
  publishBlog(id: "f66135da-0b87-4420-9a48-1fbd6ae316f9", published: true) {
    blog {
      id
      published
    }
  }
}
```

> Create Comment

```graphql
mutation {
  createComment(
    content: " Commenting for a blog"
    blog: "f66135da-0b87-4420-9a48-1fbd6ae316f9"
  ) {
    comment {
      id
      content
      approved
      blog {
        id
        content
      }
    }
  }
}
```
