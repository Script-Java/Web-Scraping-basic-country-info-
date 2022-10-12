from bs4 import BeautifulSoup
import requests
import streamlit as st


class ScrapeData:

  def __init__(self):
    self.scrape_this = "https://www.scrapethissite.com/pages/simple/"
    self.site = requests.get(self.scrape_this)
    self.soup = BeautifulSoup(self.site.text, "html.parser")

    #streamlit code starts here | Introduction to site
    st.title("Basic Information about Countries")
    st.write(
      "This is a basic personal project I did in order to practice web scraping"
    )
    st.write(
      f"I used -streamlit, -BeautifulSoup, -requests | website {self.scrape_this}"
    )

  def get_data_from_page(self):
    country_div = self.soup.findAll("div", attrs={"class": "country"})
    for data in country_div:

      # accessing child of each element in country_div
      self.country_name = data.find("h3", attrs={"class": "country-name"})
      self.country_info = data.find("div", attrs={"class": "country-info"})
      self.country_capital = self.country_info.findAll(
        "span", {"class": "country-capital"})
      self.country_population = self.country_info.findAll(
        "span", {"class": "country-population"})
      self.country_area = self.country_info.findAll("span",
                                                    {"class": "country-area"})

      st.write(f"{self.country_name}")

      #created columns to display data
      col1, col2, col3 = st.columns(3)
      col1.metric("Capital", f"{self.country_capital[0].string}", "")
      col2.metric("Population", f"{self.country_population[0].string}", "")
      col3.metric("Area", f"{self.country_area[0].string} km2", "")


ScrapeData().get_data_from_page()