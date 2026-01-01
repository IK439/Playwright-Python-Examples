import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    chromium = playwright.chromium

    browser = await chromium.launch()

    page = await browser.new_page()

    # Log every outgoing network request
    page.on(
        "request",
        lambda request: print("-->", request.method, request.url)
    )

    # Log every incoming network response
    page.on(
        "response",
        lambda response: print("<--", response.status, response.url)
    )

    # Navigate to the Playwright website
    await page.goto("https://playwright.dev/")

    await page.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())