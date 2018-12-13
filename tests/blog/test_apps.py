def test_app():
    from blog.apps import CoreConfig
    assert CoreConfig.name == 'core'
