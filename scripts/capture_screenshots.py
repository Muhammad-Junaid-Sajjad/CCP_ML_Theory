#!/usr/bin/env python3
"""
Screenshot capture script for CKD Prediction System
Captures professional screenshots of the web interface
"""

from playwright.sync_api import sync_playwright
import time

def capture_screenshots():
    print("🎬 Starting screenshot capture...")

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()

        print("📸 Navigating to application...")
        page.goto('http://localhost:5000')
        time.sleep(2)  # Wait for page to load

        # Screenshot 1: Main page with empty form
        print("📸 Capturing: Main page...")
        page.screenshot(path='screenshots/01-main-page.png', full_page=True)

        # Screenshot 2: Form with High Risk CKD sample data
        print("📸 Capturing: High Risk CKD sample...")
        page.click('button:has-text("High Risk CKD")')
        time.sleep(1)
        page.screenshot(path='screenshots/02-high-risk-sample.png', full_page=True)

        # Screenshot 3: Prediction result
        print("📸 Capturing: Prediction result...")
        page.click('button:has-text("Predict")')
        time.sleep(2)  # Wait for prediction
        page.screenshot(path='screenshots/03-prediction-result.png', full_page=True)

        # Screenshot 4: Healthy patient sample
        print("📸 Capturing: Healthy patient sample...")
        page.goto('http://localhost:5000')
        time.sleep(1)
        page.click('button:has-text("Healthy Patient")')
        time.sleep(1)
        page.screenshot(path='screenshots/04-healthy-sample.png', full_page=True)

        # Screenshot 5: Form with tooltip (hover over first field)
        print("📸 Capturing: Tooltip example...")
        page.goto('http://localhost:5000')
        time.sleep(1)
        page.hover('input[name="age"]')
        time.sleep(0.5)
        page.screenshot(path='screenshots/05-tooltip-example.png')

        browser.close()

    print("✅ All screenshots captured successfully!")
    print("📁 Screenshots saved in: screenshots/")

if __name__ == "__main__":
    capture_screenshots()
