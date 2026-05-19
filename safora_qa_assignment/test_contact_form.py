import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
   
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    
    
    driver = webdriver.Chrome(options=options)
    
    yield driver
    
    driver.quit()



def test_contact_form_validation_on_blank_submission(driver):

    target_url = "https://safora.se/en/contact.html"
    driver.get(target_url)
    
   
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Get In Touch')]")))
    
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Send Message')]")))
    
    submit_button.click()
    

    name_field = driver.find_element(By.NAME, "name") or driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    
    is_required = name_field.get_attribute("required")
    assert is_required == "true" or is_required is not None, \
        "Security Alert!"


def test_contact_form_data_input_flow(driver):
    
    driver.get("https://safora.se/en/contact.html")
    wait = WebDriverWait(driver, 10)
    
    name_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder*='Name']")))
    email_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder*='Email']")
    message_input = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder*='Message']")
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Send Message')]")))
    
    
    test_name = "QA Intern Candidate"
    test_email = "candidate.qa@example.com"
    test_message = "This is an automated system validation evaluation execution."
    
    name_input.clear()
    name_input.send_keys(test_name)
    
    email_input.clear()
    email_input.send_keys(test_email)
    
    message_input.clear()
    message_input.send_keys(test_message)
    
    
    assert name_input.get_attribute("value") == test_name, "Data mismatch inside Name UI field!"
    assert email_input.get_attribute("value") == test_email, "Data mismatch inside Email UI field!"
    assert message_input.get_attribute("value") == test_message, "Data mismatch inside Message text box area!"
    
    
    print("\nForm data validation successfully processed and entered.")

