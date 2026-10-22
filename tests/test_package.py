def test_package_is_importable():
    import cvm_pipeline

    assert "src" in cvm_pipeline.__file__
