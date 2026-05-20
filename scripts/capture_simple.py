#!/usr/bin/env python3
"""
Simple screenshot capture - just the main page
"""

from playwright.sync_api import sync_playwright
import time

def capture_main_page():
    print("🎬 Capturing main page screenshot...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()

        print("📸 Navigating to http://localhost:5000...")
        page.goto('http://localhost:5000')
        time.sleep(3)  # Wait for page to fully load

        print("📸 Capturing full page screenshot...")
        page.screenshot(path='screenshots/main-page.png', full_page=True)

        print("✅ Screenshot saved: screenshots/main-page.png")

        # Keep browser open for 5 seconds so you can see it
        print("⏳ Browser will close in 5 seconds...")
        time.sleep(5)

        browser.close()

    print("✅ Done!")

if __name__ == "__main__":
    capture_main_page()
