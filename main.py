# Written by Levent Alahan Tekinalp. You may use freely for non-gambling, non-adultery promoting or any project that does not attack values of others.

import flet as ft
from date_time_clock import date_time_box
def main(page: ft.Page):
    """
    You can modify the weekdays and months without formatting the original format in your own language. I made this
    option to apply it for multilingual apps
    :param page:
    :return:
    """
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    months = ["01-Jan", "02-Feb", "03-Mar", "04-Apr", "05-May", "06-Jun", "07-Jul", "08-Aug", "09-Sep", "10-Oct",
              "11-Nov", "12-Dec"]

    def demonstrate(e):
        """
        this code triggers the date_time_box function in order it to work you need to write the import statement
        "from clock import date_time_box" after copying the code from this page and pasting it in the file named
        date_time_clock.py. You can modify the Text Field label Year in correspondence with your own language. You can do the
        same for select button, cancel button, error_txt for the year text fiel and dropdown to pick the month.
        :param e:
        :return:
        """
        if e.control.data == "demo":

            date_time_box(calendar_title="TIME & DATE PICKER",
                          year_label="YEAR",
                          cancel_btn_txt="CANCEL",
                          error_txt="Date >",
                          select_btn_txt="SELECT",
                          page=page,
                          weekdays=weekdays,
                          month_label="MONTH",
                          hour_txt = "hour",
                          minute_txt="min",
                          am_txt = "am",
                          pm_txt ="pm",
                          months=months)

    button = ft.ElevatedButton(text="Clock", on_click=demonstrate, data="demo")
    page.add(button)


ft.app(target=main)
