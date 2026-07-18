import argparse
from shutil import which
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError


def run(headless: bool, query: str):
    chromium_path = which("chromium")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="./.rutube_profile",
            headless=headless,
            executable_path=chromium_path
        )

        page = context.new_page()
        page.goto("https://rutube.ru")

        try:
            page.locator("button[aria-label='Закрыть попап']").click(timeout=3000)
        except TimeoutError:
            pass

        search = page.locator("input[aria-label='Поиск']")
        search.fill(query)
        page.keyboard.press("Enter")

        page.wait_for_selector("a[href^='/video/']")
        page.locator("a[href^='/video/'][title]").first.click()

        if not headless:
            like = page.locator("button[title='Нравится']")

            if like.get_attribute("aria-pressed") == "true":
                like.click()

            page.reload()
            page.wait_for_selector("button[title='Нравится']")

            page.locator("button[title='Нравится']").click()

            page.screenshot(path="artifacts/rutube.png")
            Path("artifacts/rutube.html").write_text(page.content(), encoding="utf-8")
        else:
            page.wait_for_timeout(5000)
            page.screenshot(path="artifacts/rutube-headless.png")
            Path("artifacts/rutube-headless.html").write_text(page.content(), encoding="utf-8")

        page.wait_for_timeout(2000)
        context.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--query", required=True)

    args = parser.parse_args()

    run(headless=args.headless, query=args.query)
