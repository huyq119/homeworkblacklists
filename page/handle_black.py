import yaml
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def handle_black(fun):
    def run(*args, **kwargs):
        instance = args[0]
        with open("../page/black_lists.yml", 'r', encoding='utf-8') as f:
            _black_list = yaml.safe_load(f)
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            for black in _black_list:
                ele = WebDriverWait(instance._driver, 10). \
                    until(expected_conditions.presence_of_all_elements_located(tuple(black)))
                if len(ele) > 0:
                    ele[0].click()
                    return fun(*args, **kwargs)

    return run
