from pages.third_pattern.sbis_download import SbisDownload


def test_download_complete():
    SbisDownload.download_plugin()
    assert 'Файл существует' == SbisDownload.check_complete_download()


def test_size_of_plugin():
    assert SbisDownload.find_size_plugin() == SbisDownload.get_web_size_plugin()

