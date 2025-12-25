import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.google.com/")
        
        # Take a screenshot and save it as Google.png
        await page.screenshot(path="Google.png")
        await browser.close()

# Run the async Playwright script
asyncio.run(main())