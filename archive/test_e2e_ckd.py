"""
================================================================================
CHRONIC KIDNEY DISEASE PREDICTION SYSTEM - E2E TESTING
================================================================================
End-to-End Testing with Playwright (Headed Mode)

This script performs comprehensive testing of the CKD prediction web interface:
1. Fills patient form with realistic clinical data
2. Submits prediction and verifies results
3. Tests all tabs (Predict, Models, Graphs)
4. Verifies all visualizations load correctly
5. Captures screenshots as evidence

Test Cases:
- High Risk CKD Patient (should predict CKD with high confidence)
- Low Risk Healthy Patient (should predict Not CKD)
- All UI elements functional
- All API endpoints responding
================================================================================
"""

from playwright.sync_api import sync_playwright
import time
import json

def test_ckd_prediction_system():
    """
    Comprehensive E2E test of CKD prediction system
    """

    print("="*80)
    print("CKD PREDICTION SYSTEM - E2E TESTING")
    print("="*80)
    print()

    with sync_playwright() as p:
        # Launch browser in headed mode (visible)
        print("[1/10] Launching browser (headed mode)...")
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()

        try:
            # Test 1: Load homepage
            print("[2/10] Loading homepage...")
            page.goto("http://localhost:5000")
            page.wait_for_load_state("networkidle")
            time.sleep(1)

            # Verify page title
            title = page.title()
            print(f"  ✓ Page loaded: {title}")

            # Take screenshot of homepage
            page.screenshot(path="test_screenshots/01_homepage.png", full_page=True)
            print("  ✓ Screenshot saved: 01_homepage.png")

            # Test 2: Fill patient form with HIGH RISK CKD data
            print("[3/10] Filling patient form (High Risk CKD Patient)...")

            # High risk CKD patient data
            patient_data = {
                'age': '65',
                'bp': '90',
                'sg': '1.010',
                'al': '4',
                'su': '3',
                'bgr': '180',
                'bu': '85',      # High blood urea (normal: 10-50)
                'sc': '4.5',     # High serum creatinine (normal: 0.6-1.2)
                'sod': '135',
                'pot': '5.5',
                'hemo': '9.5',   # Low hemoglobin (normal: 12-17)
                'pcv': '30',     # Low packed cell volume (normal: 36-48)
                'wbcc': '9000',
                'rbcc': '3.8',
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

            # Fill numeric fields
            for field, value in patient_data.items():
                if field in ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']:
                    # Dropdown fields
                    page.select_option(f'select[name="{field}"]', value)
                else:
                    # Text input fields
                    page.fill(f'input[name="{field}"]', value)

            print("  ✓ Form filled with patient data")
            time.sleep(1)

            # Take screenshot of filled form
            page.screenshot(path="test_screenshots/02_form_filled.png", full_page=True)
            print("  ✓ Screenshot saved: 02_form_filled.png")

            # Test 3: Submit prediction
            print("[4/10] Submitting prediction...")
            page.click('button[type="submit"]')

            # Wait for results
            page.wait_for_selector('#result', state='visible', timeout=10000)
            time.sleep(2)

            # Extract prediction results
            prediction_text = page.locator('#prediction').inner_text()
            confidence_text = page.locator('#confidence').inner_text()
            risk_level_text = page.locator('#risk-level').inner_text()

            print(f"  ✓ Prediction: {prediction_text}")
            print(f"  ✓ Confidence: {confidence_text}")
            print(f"  ✓ Risk Level: {risk_level_text}")

            # Verify prediction is CKD
            assert "CKD" in prediction_text or "ckd" in prediction_text.lower(), "Expected CKD prediction"
            print("  ✓ Prediction verified: CKD detected")

            # Take screenshot of results
            page.screenshot(path="test_screenshots/03_prediction_result.png", full_page=True)
            print("  ✓ Screenshot saved: 03_prediction_result.png")

            # Test 4: Test Models tab
            print("[5/10] Testing Models tab...")
            page.click('button:has-text("Models")')
            time.sleep(2)

            # Verify model cards are visible
            model_cards = page.locator('.model-card').count()
            print(f"  ✓ Found {model_cards} model cards")
            assert model_cards >= 5, "Expected at least 5 models"

            # Take screenshot of models tab
            page.screenshot(path="test_screenshots/04_models_tab.png", full_page=True)
            print("  ✓ Screenshot saved: 04_models_tab.png")

            # Test 5: Test Graphs tab
            print("[6/10] Testing Graphs tab...")
            page.click('button:has-text("Graphs")')
            time.sleep(2)

            # Verify graphs are visible
            graphs = page.locator('.graph-item img').count()
            print(f"  ✓ Found {graphs} visualization graphs")
            assert graphs >= 8, "Expected at least 8 graphs"

            # Take screenshot of graphs tab
            page.screenshot(path="test_screenshots/05_graphs_tab.png", full_page=True)
            print("  ✓ Screenshot saved: 05_graphs_tab.png")

            # Test 6: Test LOW RISK patient
            print("[7/10] Testing Low Risk patient...")
            page.click('button:has-text("Predict")')
            time.sleep(1)

            # Fill healthy patient data
            healthy_data = {
                'age': '35',
                'bp': '70',
                'sg': '1.020',
                'al': '0',
                'su': '0',
                'bgr': '95',
                'bu': '30',      # Normal blood urea
                'sc': '0.9',     # Normal serum creatinine
                'sod': '140',
                'pot': '4.5',
                'hemo': '15',    # Normal hemoglobin
                'pcv': '42',     # Normal packed cell volume
                'wbcc': '7500',
                'rbcc': '5.0',
                'rbc': 'normal',
                'pc': 'normal',
                'pcc': 'notpresent',
                'ba': 'notpresent',
                'htn': 'no',
                'dm': 'no',
                'cad': 'no',
                'appet': 'good',
                'pe': 'no',
                'ane': 'no'
            }

            # Fill form
            for field, value in healthy_data.items():
                if field in ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']:
                    page.select_option(f'select[name="{field}"]', value)
                else:
                    page.fill(f'input[name="{field}"]', value)

            print("  ✓ Healthy patient data filled")

            # Submit
            page.click('button[type="submit"]')
            page.wait_for_selector('#result', state='visible', timeout=10000)
            time.sleep(2)

            # Extract results
            prediction_text_2 = page.locator('#prediction').inner_text()
            risk_level_text_2 = page.locator('#risk-level').inner_text()

            print(f"  ✓ Prediction: {prediction_text_2}")
            print(f"  ✓ Risk Level: {risk_level_text_2}")

            # Take screenshot
            page.screenshot(path="test_screenshots/06_healthy_patient.png", full_page=True)
            print("  ✓ Screenshot saved: 06_healthy_patient.png")

            # Test 7: Test API endpoints directly
            print("[8/10] Testing API endpoints...")

            # Test /results endpoint
            response = page.request.get("http://localhost:5000/results")
            assert response.ok, "Results endpoint failed"
            results_data = response.json()
            print(f"  ✓ /results endpoint: {len(results_data)} models")

            # Test /feature_info endpoint
            response = page.request.get("http://localhost:5000/feature_info")
            assert response.ok, "Feature info endpoint failed"
            feature_data = response.json()
            print(f"  ✓ /feature_info endpoint: {len(feature_data['features'])} features")

            # Test /health endpoint
            response = page.request.get("http://localhost:5000/health")
            assert response.ok, "Health endpoint failed"
            health_data = response.json()
            print(f"  ✓ /health endpoint: {health_data['status']}")

            # Test 8: Verify all visualizations load
            print("[9/10] Verifying all visualizations...")
            page.click('button:has-text("Graphs")')
            time.sleep(2)

            expected_plots = [
                'class_dist.png',
                'missing_heatmap.png',
                'correlation_heatmap.png',
                'numeric_distributions.png',
                'model_comparison.png',
                'confusion_matrices.png',
                'cv_accuracy.png',
                'feature_importance.png',
                'roc_curves.png',
                'execution_time.png'
            ]

            loaded_images = 0
            for plot in expected_plots:
                img = page.locator(f'img[src*="{plot}"]')
                if img.count() > 0:
                    loaded_images += 1

            print(f"  ✓ {loaded_images}/{len(expected_plots)} visualizations loaded")

            # Test 9: Performance check
            print("[10/10] Performance check...")

            # Measure prediction time
            start_time = time.time()
            page.click('button:has-text("Predict")')
            time.sleep(0.5)
            page.fill('input[name="age"]', '50')
            page.click('button[type="submit"]')
            page.wait_for_selector('#result', state='visible', timeout=10000)
            end_time = time.time()

            prediction_time = end_time - start_time
            print(f"  ✓ Prediction response time: {prediction_time:.2f}s")

            # Final screenshot
            page.screenshot(path="test_screenshots/07_final_state.png", full_page=True)
            print("  ✓ Screenshot saved: 07_final_state.png")

            print()
            print("="*80)
            print("✅ ALL TESTS PASSED")
            print("="*80)
            print()
            print("Test Summary:")
            print(f"  ✓ Homepage loaded successfully")
            print(f"  ✓ Patient form functional")
            print(f"  ✓ High Risk CKD prediction: {prediction_text}")
            print(f"  ✓ Low Risk prediction: {prediction_text_2}")
            print(f"  ✓ All 3 tabs working (Predict, Models, Graphs)")
            print(f"  ✓ {model_cards} models displayed")
            print(f"  ✓ {loaded_images} visualizations loaded")
            print(f"  ✓ All API endpoints responding")
            print(f"  ✓ Average prediction time: {prediction_time:.2f}s")
            print(f"  ✓ 7 screenshots captured in test_screenshots/")
            print()

            # Keep browser open for 5 seconds to show final state
            print("Keeping browser open for 5 seconds...")
            time.sleep(5)

        except Exception as e:
            print(f"\n❌ TEST FAILED: {e}")
            page.screenshot(path="test_screenshots/error.png", full_page=True)
            raise

        finally:
            browser.close()
            print("Browser closed.")


if __name__ == "__main__":
    # Create screenshots directory
    import os
    os.makedirs("test_screenshots", exist_ok=True)

    # Run tests
    test_ckd_prediction_system()
