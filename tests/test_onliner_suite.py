import pytest

from model.group import Group


@pytest.mark.onliner
class TestOnlinerSuite(object):

    @pytest.mark.test
    @pytest.mark.tcid1
    def test_log_in(self, app):
        app.navigate_to_home_page()
        app.main_page_actions.click_login()

        app.login_actions.type_credentials(Group(
            username=app.config['login']['username'],
            password=app.config['login']['password']))
        app.login_actions.submit_credentials()

        app.main_page_actions.verify_authorization()

    @pytest.mark.tcid2
    def test_search(self, app):
        app.navigate_to_home_page()
        app.main_page_actions.switch_to_search_frame()

        app.search_actions.search_item(name=app.config['search']['prod_name'])

        app.search_actions.verify_search_results(name=app.config['search']['prod_name'])

    @pytest.mark.tcid3
    def test_menu_navigate(self, app):
        app.navigate_to_home_page()
        app.main_page_actions.navigate_to_section(name=app.config['navigation']['section_name'])
        app.catalog_actions.verify_url(url=app.config['navigation']['section_url'])

    @pytest.mark.tcid4
    def test_compare(self, app):
        app.navigate_to_home_page()
        app.main_page_actions.navigate_to_section(name=app.config['navigation']['section_name'])
        app.catalog_actions.navigate_to_subsection(name=app.config['navigation']['subsection_name'])

        product_names = []
        for i in range(0, 2):
            app.catalog_actions.scroll_down()
            app.catalog_actions.navigate_to_product(index=i)
            product_names.append(app.product_actions.get_product_name())
            app.product_actions.set_compare_checkbox()
            app.product_actions.navigate_to_subsection()

        app.catalog_actions.navigate_to_compare_page()

        app.compare_actions.verify_url(url=app.config['compare']['url'])
        for i in range(0, 2):
            app.compare_actions.verify_product_name(index=i, name=product_names[i])

        app.navigate_to_home_page()
        app.main_page_actions.navigate_to_section(name=app.config['navigation']['section_name'])
        app.catalog_actions.navigate_to_subsection(name=app.config['navigation']['subsection_name'])
        app.catalog_actions.remove_compare_icon()

    @pytest.mark.test
    @pytest.mark.tcid5
    def test_order(self, app):
        app.navigate_to_home_page()
        app.main_page_actions.navigate_to_section(name=app.config['navigation']['section_name'])
        app.catalog_actions.navigate_to_subsection(name=app.config['navigation']['subsection_name'])

        app.catalog_actions.navigate_to_product()
        app.product_actions.navigate_to_product_traders()
        app.product_actions.click_buy()

        app.main_page_actions.navigate_to_cart_page()
        app.cart_actions.navigate_to_order_page()
        app.cart_actions.verify_url(url=app.config['order']['order_menu_url'])

        app.navigate_to_home_page()
        app.main_page_actions.navigate_to_cart_page()
        app.cart_actions.display_remove_field()
        app.cart_actions.click_remove()
