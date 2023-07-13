import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

st.set_page_config(page_title="home",  page_icon="🧭")
st.sidebar.header("Home")

st.title("Scooty-Tor")






def main():
    # Set Streamlit app title and layout
    st.title("Screenshot Spider")

    # Get the URL from the user
    url = st.text_input("Enter the URL to take a screenshot:", "")

    if st.button("Take Screenshot"):
        PROXY = "http://127.0.0.1:8118"
        # Create a Chrome WebDriver
        webdriver_service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

        try:
            # Open the URL and take a screenshot
            driver.get(url)
            screenshot = driver.get_screenshot_as_png()

            # Save the screenshot to a file
            with open("screenshot.png", "wb") as f:
                f.write(screenshot)

            # Display the screenshot in the Streamlit app
            st.image("screenshot.png", caption="Screenshot")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

        finally:
            # Close the WebDriver
            driver.quit()

# Run the Streamlit app
if __name__ == "__main__":
    main()
