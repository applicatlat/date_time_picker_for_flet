# Written and created by Levent Alahan Tekinalp. You may use freely for non-gambling, non-adultery promoting or any project that does not attack values of others.

import calendar
import datetime
import re

import flet as ft

today = datetime.date.today()
month_number = today.month
year = today.year


def keyboard_event(g: ft.KeyboardEvent):
    """
    basan tuşları takip eden fonksiyon
    :param g:
    :return:
    """
    global keys
    keys = g.key


def date_time_box(calendar_title, year_label, month_label, cancel_btn_txt, select_btn_txt, page, weekdays, months,
                  error_txt, hour_txt, minute_txt, am_txt, pm_txt):

    def am_pm_repeater(e, h):
        """
        am pm saat düzenleyicisi
        :param e: control value
        :param h: a-m,pm ... 2 4 ... dakika
        :return:
        """
        e.control.value = re.sub(r"\D", "", e.control.value)
        e.control.update()
        if h == "a":
            if e.control.value is None or e.control.value == "":
                return
            elif int(e.control.value[0]) > 1:
                e.control.value = ""
                e.control.update()
                return
            elif int(e.control.value[0]) == 1:
                if not keys[-1].isdigit():
                    return
                elif int(keys[-1]) > 2:
                    e.control.value = e.control.value[0]
                    e.control.update()
                    return
        elif h == "2":
            if e.control.value is None or e.control.value == "":
                return
            elif int(e.control.value[0]) > 2:
                e.control.value = ""
                e.control.update()
                return
            elif int(e.control.value[0]) == 1:
                if not keys[-1].isdigit():
                    return
            elif int(e.control.value[0]) == 2:
                if not keys[-1].isdigit():
                    return
                elif int(keys[-1]) > 3:
                    e.control.value = e.control.value[0]
                    e.control.update()
                    return
        elif h == "da":
            if e.control.value is None or e.control.value == "":
                return
            elif int(e.control.value[0]) > 5:
                e.control.value = ""
                e.control.update()
                return
    def button_hour_minute_controller():
        if len(str(widget_tf_saat.value)) == 2 and len(str(widget_tf_dakika.value)) == 2:
            select_btn.disabled = False
            select_btn.update()
        else:
            select_btn.disabled = True
            select_btn.update()

    def saat_minute(e):
        """
        saat ve dakika düzenleyicisi
        :param e:
        :return:
        """
        if e.control.data == "am_pm":
            if e.control.value is None:
                widget_tf_saat.disabled = True
                widget_tf_saat.update()
                widget_tf_dakika.disabled = True
                widget_tf_dakika.update()
            else:
                widget_tf_saat.disabled = False
                widget_tf_saat.value = ""
                widget_tf_saat.update()
                widget_tf_dakika.disabled = False
                widget_tf_dakika.value = ""
                widget_tf_dakika.update()

        elif e.control.data == "saat" and widget_dd_am_pm.value == am_txt:
            am_pm_repeater(e, h="a")
            button_hour_minute_controller()
        elif e.control.data == "saat" and widget_dd_am_pm.value == pm_txt:
            am_pm_repeater(e, h="a")
            button_hour_minute_controller()

        elif e.control.data == "saat" and widget_dd_am_pm.value == "24":
            am_pm_repeater(e, h="2")
            button_hour_minute_controller()

        elif e.control.data == "dakika":
            am_pm_repeater(e, h="da")
            button_hour_minute_controller()

    def close_dlg(e):
        """
        closes dialog box without making any selection
        :param e:
        :return:
        """
        dialog_box.open = False
        page.update()

    def print_result(e):
        """
        returns you the result as dictionary:
        :param e:
        :return:
        """

        try:
            week_day = datetime.datetime(int(year_input.value), int(widget_start_month.value[:2]), int(final_day)).weekday()
        except:
            if widget_tf_saat.value is not None and widget_tf_dakika.value is not None and widget_dd_am_pm.value is not None:
                result_dict = {"hour_am_pm_hour": f"{widget_dd_am_pm.value}", "hour": f"{widget_tf_saat.value}",
                                   "minute": f"{widget_tf_dakika.value}"}
                print(result_dict)
                dialog_box.open = False
                page.update()
                return result_dict
            else:
                pass
        if widget_tf_saat.value =="" and widget_tf_dakika.value =="" or widget_dd_am_pm.value is None:
            result_dict = {"year": f"{year_input.value}", "month_number": f"{int(widget_start_month.value[:2])}",
                           "month_txt": f"{widget_start_month.value[3:]}",
                           "week_day_number": f"{week_day + 1}", "day_number": f"{final_day}",
                           "day_txt": f"{weekdays[week_day]}"}
            dialog_box.open = False
            page.update()
            print(result_dict)
            return result_dict
        else:
            result_dict = {"year": f"{year_input.value}", "month_number": f"{int(widget_start_month.value[:2])}",
                               "month_txt": f"{widget_start_month.value[3:]}",
                               "week_day_number": f"{week_day + 1}", "day_number": f"{final_day}",
                               "day_txt": f"{weekdays[week_day]}", "hour_am_pm_hour": f"{widget_dd_am_pm.value}",
                               "hour": f"{widget_tf_saat.value}", "minute": f"{widget_tf_dakika.value}"}
            dialog_box.open = False
            page.update()
            print(result_dict)

            return result_dict





    def calendar_setter(year, month, result, list_days):
        date_2_controls = [ft.Text("  1 ", weight=ft.FontWeight.BOLD),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True)]
        date_3_controls = [ft.Text("  2 ", weight=ft.FontWeight.BOLD),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True)]
        date_4_controls = [ft.Text("  3 ", weight=ft.FontWeight.BOLD),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True)]
        date_5_controls = [ft.Text("  4 ", weight=ft.FontWeight.BOLD),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True)]
        date_6_controls = [ft.Text("  5 ", weight=ft.FontWeight.BOLD),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True)]
        date_7_controls = [ft.Text("  6 ", weight=ft.FontWeight.BOLD),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True),
                           ft.TextButton("x", width=33, height=33, disabled=True)]

        def day_selector(e):
            global all_controls
            all_controls = date_2_controls[1:] + date_3_controls[1:] + date_4_controls[1:] + date_5_controls[
                                                                                             1:] + date_6_controls[
                                                                                                   1:] + date_6_controls[
                                                                                                         1:]
            for ctrl in all_controls:
                if ctrl.text == "x":
                    ctrl.disabled = True
                    ctrl.update()
                if int(year_input.value) <= year and int(
                        widget_start_month.value[:2]) <= month_number and ctrl.text.isdigit():
                    if int(ctrl.text) < today.day:
                        ctrl.disabled = True
                        ctrl.update()
                    else:
                        ctrl.disabled = False
                        ctrl.update()
                if int(year_input.value) >= year and int(
                        widget_start_month.value[:2]) > month_number and ctrl.text.isdigit():
                    ctrl.disabled = False
                    ctrl.update()
            global final_day
            final_day = e.control.text
            e.control.disabled = True
            e.control.update()
            select_btn.disabled = False
            select_btn.update()
            return final_day

        first_day = datetime.date(year, month, 1)
        first_day_of_week = first_day.weekday()

        if result != None:
            for days in result:
                day_of_month = datetime.date(year, month, days).day
                week_day = datetime.datetime(year, month, days).weekday()
                week_number = (day_of_month + first_day_of_week - 1) // 7 + 1

                if week_number == 1:
                    date_2_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, disabled=True)

                if week_number == 2:
                    date_3_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, disabled=True)

                if week_number == 3:
                    date_4_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, disabled=True)

                if week_number == 4:
                    date_5_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, disabled=True)

                if week_number == 5:
                    date_6_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, disabled=True)

                if week_number == 6:
                    date_7_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, disabled=True)

            for days in list_days:
                day_of_month = datetime.date(year, month, days).day
                week_day = datetime.datetime(year, month, days).weekday()
                week_number = (day_of_month + first_day_of_week - 1) // 7 + 1
                if week_number == 1:
                    date_2_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

                if week_number == 2:
                    date_3_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

                if week_number == 3:
                    date_4_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

                if week_number == 4:
                    date_5_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

                if week_number == 5:
                    date_6_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

                if week_number == 6:
                    date_7_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

        if result is None:
            for days in list_days:
                day_of_month = datetime.date(year, month, days).day
                week_day = datetime.datetime(year, month, days).weekday()
                week_number = (day_of_month + first_day_of_week - 1) // 7 + 1
                if week_number == 1:
                    date_2_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

                if week_number == 2:
                    date_3_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

                if week_number == 3:
                    date_4_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

                if week_number == 4:
                    date_5_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

                if week_number == 5:
                    date_6_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

                if week_number == 6:
                    date_7_controls[week_day + 1] = ft.TextButton(text=str(days), width=33, height=33, data=str(days),
                                                                  disabled=False, on_click=day_selector)

        date_2_row.controls = date_2_controls
        date_2_row.update()
        date_3_row.controls = date_3_controls
        date_3_row.update()
        date_4_row.controls = date_4_controls
        date_4_row.update()
        date_5_row.controls = date_5_controls
        date_5_row.update()
        date_6_row.controls = date_6_controls
        date_6_row.update()
        date_7_row.controls = date_7_controls
        date_7_row.update()
        column_dates.update()
        date_container.update()

    def date_fixer(e):
        """
        tarihi gün bazında aylara bakarak düzenler
        :param e:
        :return:
        """
        month = int(e.control.value[:2])

        if calendar.isleap(int(year_input.value)):
            day_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            if len(e.control.options) < 12 and datetime.datetime.now().month == month:
                list_days = list(range(1, day_month[month - 1] + 1))[
                            datetime.datetime.now().day - 1:]
                list_days_full = list(range(1, day_month[month - 1] + 1))
                result = list(set(list_days_full) - set(list_days))

                calendar_setter(year=int(year_input.value), month=month, result=result, list_days=list_days)

            else:
                list_days = list(range(1, day_month[month - 1] + 1))
                calendar_setter(year=int(year_input.value), month=month, result=None, list_days=list_days)

        else:
            day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            if len(e.control.options) < 12 and datetime.datetime.now().month == month:
                list_days = list(range(1, day_month[month - 1] + 1))[
                            datetime.datetime.now().day - 1:]
                list_days_full = list(range(1, day_month[month - 1] + 1))
                result = list(set(list_days_full) - set(list_days))

                calendar_setter(year=int(year_input.value), month=month, result=result, list_days=list_days)

            else:
                list_days = list(range(1, day_month[month - 1] + 1))
                calendar_setter(year=int(year_input.value), month=month, result=None, list_days=list_days)

    def year_tf_arranger(e):
        """
        year'a değer girince uygun sayı giriliyor mu kontrolünü yapıyor ve diğer widgetları aktive ediyor.
        :param e:
        :return:
        """
        e.control.value = re.sub(r"\D", "", e.control.value)
        e.control.update()
        if len(e.control.value) == 4 and int(e.control.value) > year - 1:
            year_input.error_text = ""

            if e.control.value == str(datetime.datetime.now().year):
                list_months = months[int(month_number) - 1:]
                widget_start_month.options = [ft.dropdown.Option(x) for x in list_months]

            else:
                widget_start_month.options = [ft.dropdown.Option(x) for x in months]

            widget_start_month.disabled = False
            widget_start_month.update()
            e.control.update()

        else:
            year_input.error_text = error_txt
            widget_start_month.disabled = True
            widget_start_month.value = ""
            widget_start_month.update()
            e.control.update()

    day_row_ctrl = [ft.Text("  w", weight=ft.FontWeight.BOLD)]
    for day in weekdays:
        day_row_ctrl.append(ft.Text(day, weight=ft.FontWeight.BOLD, size=12))
    day_row_ctrl.append(ft.Text("  "))

    date_1_row = ft.Row(controls=day_row_ctrl, alignment=ft.alignment.center_left)
    date_2_row = ft.Row(alignment=ft.alignment.center_left, spacing=0)
    date_3_row = ft.Row(alignment=ft.alignment.center_left, spacing=0)
    date_4_row = ft.Row(alignment=ft.alignment.center_left, spacing=0)
    date_5_row = ft.Row(alignment=ft.alignment.center_left, spacing=0)
    date_6_row = ft.Row(alignment=ft.alignment.center_left, spacing=0)
    date_7_row = ft.Row(alignment=ft.alignment.center_left, spacing=0)
    calendar_title_text = ft.Text(value=calendar_title, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, size=20)
    year_input = ft.TextField(label=year_label, border=ft.InputBorder.UNDERLINE, max_length=4, width=50, height=85,
                              counter_text=" ", on_change=year_tf_arranger, text_align=ft.TextAlign.CENTER)
    widget_start_month = ft.Dropdown(width=80, disabled=True, height=85, on_change=date_fixer, counter_text=" ",
                                     label=month_label, data="start_month", border=ft.InputBorder.UNDERLINE)
    cancel_btn = ft.ElevatedButton(cancel_btn_txt, on_click=close_dlg, width=90)
    select_btn = ft.ElevatedButton(select_btn_txt, on_click=print_result, width=90, disabled=True)
    widget_tf_saat = ft.TextField(label=hour_txt, width=65, data="saat", max_length=2, counter_text=" ",
                                  on_change=saat_minute, disabled=True)
    widget_tf_dakika = ft.TextField(label=minute_txt, width=65, data="dakika", max_length=2, counter_text=" ",
                                    on_change=saat_minute, disabled=True)
    widget_dd_am_pm = ft.Dropdown(label="type", width=80, data="am_pm", counter_text=" ", height=87,
                                  on_change=saat_minute,
                                  options=[ft.dropdown.Option(am_txt),
                                           ft.dropdown.Option(pm_txt),
                                           ft.dropdown.Option("24")])

    def delete_all(e):
        widget_tf_saat.value = ""
        widget_tf_dakika.value = ""
        widget_dd_am_pm.value = ""
        widget_start_month.value = ""
        year_input.value = ""
        widget_tf_saat.disabled = True
        widget_tf_dakika.disabled = True
        widget_start_month.disabled = True

        date_2_row.controls = []
        date_2_row.update()
        date_3_row.controls = []
        date_3_row.update()
        date_4_row.controls = []
        date_4_row.update()
        date_5_row.controls = []
        date_5_row.update()
        date_6_row.controls = []
        date_6_row.update()
        date_7_row.controls = []
        date_7_row.update()

        widget_tf_saat.update()
        widget_tf_dakika.update()
        widget_dd_am_pm.update()
        widget_start_month.update()
        year_input.update()

    delete_all_icon = ft.IconButton(icon=ft.icons.DELETE, on_click=delete_all)


    column_dates = ft.Column(
        controls=[date_1_row, date_2_row, date_3_row, date_4_row, date_5_row, date_6_row, date_7_row], spacing=0,
        alignment=ft.alignment.center, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    second_column = ft.Column(controls=[select_btn, cancel_btn], spacing=3, alignment=ft.MainAxisAlignment.END,
                              horizontal_alignment=ft.CrossAxisAlignment.END)

    first_row = ft.Row(controls=[year_input, widget_start_month, second_column], alignment=ft.MainAxisAlignment.END,
                       vertical_alignment=ft.CrossAxisAlignment.END)
    second_row = ft.Row(controls=[widget_dd_am_pm, widget_tf_saat,
                                  ft.Text(width=5, weight=ft.FontWeight.BOLD, size=20, height=60, value=":"),
                                  widget_tf_dakika], alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER)
    first_column = ft.Column(controls=[first_row, second_row])

    first_container = ft.Container(content=first_column, border_radius=20, border=ft.border.all(2, ft.colors.BLUE),
                                   width=270, alignment=ft.alignment.center, padding=5, height=200)

    date_container = ft.Container(content=column_dates, border=ft.border.all(2, ft.colors.BLUE), border_radius=20,
                                  alignment=ft.alignment.top_center, padding=2, height=230, width=270)
    final_column = ft.Column(controls=[first_container, date_container], height=430)

    final_row = ft.Row(controls=[first_container, date_container])

    def page_resize(e):
        """
        checks page size and recreates the dialog box without disrupting whats within.
        :param e:
        :return:
        """
        global final_view
        dialog_box.open = False
        page.update()
        if page.width <= 650:
            final_view = final_column
        if page.width > 650:
            final_view = final_row
        dialog_box.open = True
        dialog_box.content = final_view
        page.update()

    if page.width < 649:
        final_view = final_column
    if page.width > 650:
        final_view = final_row

    row_ = ft.Row(controls=[calendar_title_text,delete_all_icon],alignment=ft.MainAxisAlignment.SPACE_EVENLY,vertical_alignment=ft.alignment.center)
    dialog_box = ft.AlertDialog(modal=True, title=row_, content=final_view,
                                actions_alignment=ft.MainAxisAlignment.END, content_padding=10)

    page.on_keyboard_event = keyboard_event
    page.on_resize = page_resize
    page.dialog = dialog_box
    dialog_box.open = True
    page.update()

    return
