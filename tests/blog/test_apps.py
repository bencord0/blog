def test_app():
    from blog.apps import BlogConfig
    assert BlogConfig.name == 'blog'
