import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestEBaySearch(unittest.TestCase):

    def setUp(self):
        # สร้าง instance ของเบราว์เซอร์
        self.driver = webdriver.Chrome()  # ต้องมี Chrome WebDriver ใน PATH

        # เปิดหน้าเว็บ eBay
        self.driver.get("https://th.jobsdb.com/th/th")

        # ขยายหน้าต่างเบราว์เซอร์ให้เต็มจอ
        self.driver.maximize_window()

    def test_search_for_software(self):
        # ค้นหา element ด้วย ID
        search_box = self.driver.find_element("id", "searchKeywordsField")

        # ส่งคีย์เวิร์ด "Software"
        search_box.send_keys("Software")

        # กด Enter
        search_box.send_keys(Keys.RETURN)

        # รอให้ผลการค้นหาปรากฏขึ้น
        self.driver.implicitly_wait(10)  # รอไม่เกิน 10 วินาที

        page_content = self.driver.page_source
        self.assertIn("Software", page_content, "Keyword 'Software' not found in page content.")

    def tearDown(self):
        # หยุดทำงานเป็นเวลา 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(2)

        # ปิด WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
