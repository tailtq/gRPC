from post_pb2 import Post, Author

simple_post = Post(
    title="The Imitation Game",
    tags=["War", "Science"],
    content="Scientists took on a challenge to decrypt the code sending by German",
    author=Author(first_name="Morten", last_name="Tyldum"),
    is_approved=False,
    categories=[
        Post.Category(title="Test"),
        Post.Category(title="Test 2"),
    ]
    # test="OKE"  # invalid key => exception
)

# save protocol buffer file
with open("sample_post.bin", "wb") as f:
    byte_as_string = simple_post.SerializeToString()
    f.write(byte_as_string)

# read protocol buffer file
with open("sample_post.bin", "rb") as f:
    simple_post_read = Post().FromString(f.read())

# print will not render default value (like False, empty string, empty list, etc)
print(simple_post_read)
