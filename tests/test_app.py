import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def app_runner():
    # Import the app
    return import_app("app")  

def test_header_is_present(dash_duo, app_runner):
    dash_duo.start_server(app_runner)
    header = dash_duo.find_element("h1")  # Finds the <h1> element
    assert header.text == "Interactive 3D Isosurface Visualization", "Header is incorrect or missing."

def test_visualization_is_present(dash_duo, app_runner):
    dash_duo.start_server(app_runner)

    try:
        # Attempt to find the graph by ID
        graph = dash_duo.find_element("#3d-graph")
        assert graph is not None, "Visualization is missing."
    except Exception as e:
        # Fallback to XPath if ID selector fails
        graph = dash_duo.driver.find_element_by_xpath("//*[contains(@id, '3d-graph')]")
        assert graph is not None, f"Visualization is missing. Error: {e}"



def test_region_picker_is_present(dash_duo, app_runner):
    dash_duo.start_server(app_runner)
    region_picker = dash_duo.find_element("#iso-slider")  # Finds the slider element
    assert region_picker is not None, "Region picker is missing."

