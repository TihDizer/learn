from shutil import which
from playwright.sync_api import sync_playwright

def run():
    chromium_path = which("chromium")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="./.rutube_profile",
            headless=False,
            executable_path=chromium_path
        )

        page = context.new_page()
        page.goto("https://rutube.ru")
        input("Press Enter when logged in")
        context.close()

run()
