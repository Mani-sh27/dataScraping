from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # headless = no GUI
    page = browser.new_page()
    page.goto("https://example.com")
    
    # Extract text from a specific element
    heading = page.locator("h1").text_content()
    print("Page Heading:", heading)

    browser.close()
