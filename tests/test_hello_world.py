def test_first(browser):
    browser.get("https://google.com")
    assert "Google" in browser.title


def test_second(browser):
    browser.get("https://ya.ru")
    assert "Яндекс" in browser.title

