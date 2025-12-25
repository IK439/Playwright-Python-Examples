import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://playwright.dev")

    # Assert homepage title contains "Playwright" or raise an error
    homepage_title = await page.title()
    assert "Playwright" in homepage_title, f"Unexpected homepage title: {homepage_title}"

    await page.locator('text=Get started').first.click()

    await page.wait_for_url("https://playwright.dev/docs/intro")

    # Assert URL contains "docs/intro" or raise an error
    current_url = page.url
    assert "docs/intro" in current_url, f"Unexpected URL after click: {current_url}"

    # Assert title contains "Installation" or "Playwright" or raise an error
    page_title = await page.title()
    assert "Installation" in page_title or "Playwright" in page_title, f"Unexpected page title: {page_title}"

    await page.screenshot(path="playwright_getstarted.png")
    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())