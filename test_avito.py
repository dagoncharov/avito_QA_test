import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.mark.parametrize("xpath, filename", [
    ("//*[@id='app']/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[2]", "1.Co2.Chrome.png"),
    ("//*[@id='app']/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[4]", "15.Water.Chrome.png"),
    ("//*[@id='app']/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[6]", "30.Energy.Chrome.png")
])
def test_take_screenshot(xpath, filename):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")
        element = page.locator(xpath)
        element.screenshot(path=f"output/{filename}")
        browser.close()

        
