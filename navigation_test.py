import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as playwright:

        browser = await playwright.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://playwright.dev")

        # Click Docs link
        await page.locator("text=Docs").click()

        # Wait for Docs page to load
        await page.wait_for_url("**/docs/**")
        await page.wait_for_load_state("networkidle")

        # Open search using keyboard shortcut (reliable)
        await page.keyboard.press("Control+K")

        # Wait for search input to appear
        search_box = page.locator("input[placeholder*='Search']")
        await search_box.wait_for(state="visible")

        # Type search query
        await search_box.fill("async")
        await search_box.press("Enter")

        await browser.close()

asyncio.run(run())
