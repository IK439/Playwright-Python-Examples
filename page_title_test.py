import asyncio
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

# Synchronous example with assertion
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()                         
    page.goto("https://www.google.com/")              
    assert "Google" in page.title() # Assert that "Google" is part of the page title  
    print(page.title())                               
    browser.close()                                   

# Asynchronous example with assertion
async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)
        page = await browser.new_page()                         
        await page.goto("https://www.youtube.com/")            

        # Get page title and assert it contains "YouTube"
        title = await page.title()
        assert "YouTube" in title
        print(title)                              
        await browser.close()                                  

# Run the asynchronous example
asyncio.run(main())