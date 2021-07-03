from time import sleep
from selenium_work_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        assert add_member.get_member('test152')

    def test_split(self):
        a = '1/3'
        print(a.split('/', 1))