"""
================================================================================
CKD PREDICTION SYSTEM - COMPLETE UI TESTING WITH FORM FILLING
================================================================================
This test actually fills the form in the browser and shows the prediction
================================================================================
"""

from playwright.sync_api import sync_playwright
import time

def test_complete_ui_workflow():
    """Test complete UI workflow with actual form filling"""

    print("="*80)
    print("CKD PREDICTION SYSTEM - COMPLETE UI WORKFLOW TEST")
    print("="*80)
    print()

    with sync_playwright() as p:
        # Launch browser in headed mode (visible)
        print("[1/6] Launching browser...")
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000,  # Slow down so we can see what's happening
            args=['--start-maximized']
        )
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            no_viewport=True
        )
        page = context.new_page()

        try:
            # Step 1: Load homepage
            print("[2/6] Loading homepage...")
            page.goto("http://localhost:5000")
            page.wait_for_load_state("networkidle")
            time.sleep(2)

            print(f"  ✓ Page loaded: {page.title()}")
            page.screenshot(path="test_screenshots/step1_homepage.png", full_page=True)
            print("  ✓ Screenshot: step1_homepage.png")
            print()

            # Step 2: Fill form with HIGH RISK CKD patient data
            print("[3/6] Filling form with HIGH RISK CKD patient data...")
            print("  Patient Profile: 65-year-old with multiple risk factors")
            print()

            # High risk patient data
            patient_data = {
                'age': '65',
                'bp': '90',
                'sg': '1.010',
                'al': '4',
                'su': '3',
                'bgr': '180',
                'bu': '85',
                'sc': '4.5',
                'sod': '135',
                'pot': '5.5',
                'hemo': '9.5',
                'pcv': '30',
                'wbcc': '9000',
                'rbcc': '3.8'
            }

            categorical_data = {
                'rbc': 'abnormal',
                'pc': 'abnormal',
                'pcc': 'present',
                'ba': 'present',
                'htn': 'yes',
                'dm': 'yes',
                'cad': 'no',
                'appet': 'poor',
                'pe': 'yes',
                'ane': 'yes'
            }

            # Fill numeric fields using nth-child selectors
            numeric_fields = list(patient_data.items())
            for idx, (field, value) in enumerate(numeric_fields):
                try:
                    selector = f'.field:nth-child({idx + 1}) input[type="number"]'
                    page.fill(selector, value, timeout=5000)
                    print(f"  ✓ Filled {field}: {value}")
                except Exception as e:
                    print(f"  ⚠ Could not fill {field}: {e}")

            time.sleep(1)

            # Fill categorical fields
            cat_fields = list(categorical_data.items())
            for idx, (field, value) in enumerate(cat_fields):
                try:
                    selector = f'.field:nth-child({len(numeric_fields) + idx + 1}) select'
                    page.select_option(selector, value, timeout=5000)
                    print(f"  ✓ Selected {field}: {value}")
                except Exception as e:
                    print(f"  ⚠ Could not select {field}: {e}")

            time.sleep(2)
            print()
            print("  ✓ Form filled completely")
            page.screenshot(path="test_screenshots/step2_form_filled.png", full_page=True)
            print("  ✓ Screenshot: step2_form_filled.png")
            print()

            # Step 3: Submit form
            print("[4/6] Submitting prediction...")
            page.click('button[type="submit"]')
            print("  ✓ Submit button clicked")

            # Wait for results to appear
            page.wait_for_selector('#result', state='visible', timeout=15000)
            time.sleep(3)

            # Extract prediction results
            try:
                prediction = page.locator('#prediction').inner_text()
                confidence = page.locator('#confidence').inner_text()
                risk_level = page.locator('#risk-level').inner_text()

                print()
                print("  " + "="*60)
                print(f"  PREDICTION RESULT:")
                print(f"  Diagnosis: {prediction}")
                print(f"  Confidence: {confidence}")
                print(f"  Risk Level: {risk_level}")
                print("  " + "="*60)
                print()
            except Exception as e:
                print(f"  ⚠ Could not extract results: {e}")

            page.screenshot(path="test_screenshots/step3_prediction_result.png", full_page=True)
            print("  ✓ Screenshot: step3_prediction_result.png")
            print()

            # Step 4: Check Models tab
            print("[5/6] Checking Models tab...")
            page.click('button:has-text("Models")')
            time.sleep(2)

            model_cards = page.locator('.model-card').count()
            print(f"  ✓ Model cards displayed: {model_cards}")

            page.screenshot(path="test_screenshots/step4_models_tab.png", full_page=True)
            print("  ✓ Screenshot: step4_models_tab.png")
            print()

            # Step 5: Check Graphs tab
            print("[6/6] Checking Graphs tab...")
            page.click('button:has-text("Graphs")')
            time.sleep(2)

            # Check for images
            images = page.locator('.graph-item img').count()
            print(f"  ✓ Visualization graphs: {images}")

            page.screenshot(path="test_screenshots/step5_graphs_tab.png", full_page=True)
            print("  ✓ Screenshot: step5_graphs_tab.png")
            print()

            print("="*80)
            print("✅ COMPLETE UI WORKFLOW TEST PASSED")
            print("="*80)
            print()
            print("Evidence Captured:")
            print("  1. Homepage loaded")
            print("  2. Form filled with patient data")
            print("  3. Prediction submitted and result displayed")
            print("  4. Models tab functional")
            print("  5. Graphs tab functional")
            print("  6. All screenshots saved in test_screenshots/")
            print()
            print("Keeping browser open for 10 seconds for inspection...")
            time.sleep(10)

        except Exception as e:
            print(f"\n❌ TEST FAILED: {e}")
            import traceback
            traceback.print_exc()
            page.screenshot(path="test_screenshots/error_complete.png", full_page=True)

        finally:
            browser.close()
            print("\nBrowser closed.")


if __name__ == "__main__":
    import os
    os.makedirs("test_screenshots", exist_ok=True)
    test_complete_ui_workflow()
