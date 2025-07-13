from selenium.webdriver.common.by import By


class RestorePasswordPageLocators:


    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PSSWRD_RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    NEW_PSSWRD_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    PSSWRD_SHOW_TOGGLE = (By.XPATH, '//div[contains(@class,"icon-action")]')
    PSSORD_FIELD_IS_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")
