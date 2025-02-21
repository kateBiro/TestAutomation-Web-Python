from seleniumbase import BaseCase

class BadmintonTest(BaseCase):
    url = "https://www.cambridgebadmintonclub.com/"

    def test_home_page(self):
        # comment
        self.open(self.url)
        self.assert_title("Cambridge Badminton Club")

    def test_about_us_page(self):
        self.open(self.url)
        self.click("#menu-item-21")
        self.assert_title("About Us – Cambridge Badminton Club")
        print(self.get_page_title())

    def test_FAQ_page(self):
        self.open(self.url)
        self.click("#menu-item-1198")
        self.assert_title("FAQ – Cambridge Badminton Club")
        self.click("#at-820")
        self.assert_element_visible("#ac-820 > ol:nth-child(1)")
        self.click("#at-820")
        self.assert_element_not_visible("#ac-820 > ol:nth-child(1) > li:nth-child(2)")
