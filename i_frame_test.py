import asyncio
from playwright.async_api import async_playwright

async def test_frame():
    
    async with async_playwright() as p:
        
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Go to the W3Schools "Try it" textarea example
        await page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_textarea")

        # Select the iframe that contains the textarea
        frame = page.frame_locator("#iframeResult")

        # Fill the textarea inside the iframe with text
        await frame.locator("textarea").fill("My favorite tool is Playwright")

        await page.screenshot(path="Frame.png")
        await browser.close()

asyncio.run(test_frame())