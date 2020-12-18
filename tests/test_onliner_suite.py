import time
from model.group import Group
import pytest


@pytest.mark.onliner
class TestOnlinerSuite(object):

    @pytest.mark.tcid1
    def test_log_in(self, app):
        app.navigate_to_home_page()
        app.login.get_log_in_page()
        app.login.type_credentials(Group(
            username=app.config['login']['username'],
            password=app.config['login']['password']))
        app.login.submit_credentials()
        app.login.verify_authorization()

    @pytest.mark.tcid2
    def test_search(self, app):
        app.navigate_to_home_page()
        app.search.switch_to_search_frame()
        app.search.type_search_option(name=app.config['search']['prod_name'])
        app.search.verify_search_results(name=app.config['search']['prod_name'])

    @pytest.mark.tcid3
    def test_menu_navigate(self, app):
        app.navigate_to_home_page()
        app.navigate_menu.navigate_to_tab()
        app.navigate_menu.verify_url(url=app.config['navigation']['tab_url'])

    @pytest.mark.tcid4
    def test_compare(self, app):
        app.navigate_to_home_page()
        app.compare.navigate_to_tab()
        app.compare.navigate_to_section()
        app.compare.get_product(id=0)
        app.compare.set_compare_checkbox()
        app.compare.navigate_to_section2()
        app.compare.get_product(id=1)
        app.compare.set_compare_checkbox()
        app.compare.navigate_to_compare_page()
        app.compare.verify_comparison(url=app.config['compare']['url'])

    @pytest.mark.tcid5
    def test_order(self, app):
        app.navigate_to_home_page()
        app.order.navigate_to_tab()
        app.order.navigate_to_section()
        app.order.get_product()
        app.order.get_product_traders()
        app.order.add_product_to_cart()
        app.order.navigate_to_cart()
        app.order.navigate_to_order_menu()
        app.order.verify_order_menu(url=app.config['order']['order_menu_url'])
