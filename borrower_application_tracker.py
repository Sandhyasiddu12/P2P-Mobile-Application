from anvil.tables import app_tables
from kivy import platform
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.lang import Builder

from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Ellipse, StencilPush, StencilUse, StencilUnUse, StencilPop

from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton, MDFillRoundFlatButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
import sqlite3
from kivy.factory import Factory
from kivymd.uix.label import MDLabel
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget
import anvil.server
from kivy.uix.label import Label
import base64
from kivy.core.image import Image as CoreImage
from io import BytesIO

application_tracker = """

<WindowManager>:
    ApplicationTrackerScreen:

<ALLLoansAPT>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Application Tracker "
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:
            MDBoxLayout:
                id: container
                orientation: 'vertical'
                padding: dp(15)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height
                width: self.minimum_width
                adaptive_size: True

                pos_hint: {"center_x": 0, "center_y":  0}

<ApplicationTrackerScreen>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


        MDTopAppBar:
            title: "Application status"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.borrower_dashboard()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Application Received'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 5

            MDLabel:
                text: "Congratulations! Your loan application with P2P has been received. Please wait while we process the loan. You can check the status here"
                size_hint_y: None
                height: 50

            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                    canvas.before:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12), self.x + dp(24), self.y - dp(34)

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: 50

                    MDLabel:
                        id: label1
                        text: "Application for #product_name Product Loan sent"
                        theme_text_color: "Custom"
                        text_color: 86/255, 94/255, 97/255, 1
                        size_hint_y: None
                        height: 50

                    MDLabel:
                        id: sub_label1
                        text: "Pending..."
                        theme_text_color: "Custom"
                        text_color: 0, 0, 1, 1
                        size_hint_y: None
                        height: 15  # Adjust height as needed
                        font_style: "Caption"

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas.before:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12), self.x + dp(24), self.y - dp(34)

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: 50
                    MDLabel:
                        id: label3
                        text: "Loan is approved "
                        theme_text_color: "Custom"
                        text_color: 86/255, 94/255, 97/255, 1
                        size_hint_y: None
                        height: 50

                    MDLabel:
                        id: sub_label2
                        text: "Pending..."
                        theme_text_color: "Custom"
                        text_color: 0, 0, 1, 1
                        size_hint_y: None
                        height: 15  # Adjust height as needed
                        font_style: "Caption"

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50
                    canvas.before:
                        Color:
                            rgba: 0.043, 0.145, 0.278, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12), self.x + dp(24), self.y - dp(34)

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: 50
                    MDLabel:
                        id: label4
                        text: "Loan has been disbursed"
                        theme_text_color: "Custom"
                        text_color: 86/255, 94/255, 97/255, 1
                        size_hint_y: None
                        height: 50

                    MDLabel:
                        id: sub_label3
                        text: "Pending..."
                        theme_text_color: "Custom"
                        text_color: 0, 0, 1, 1
                        size_hint_y: None
                        height: 15  # Adjust height as needed
                        font_style: "Caption"

                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 0.043, 0.145, 0.278, 1
                    size_hint_y: None
                    height: 50

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: 50
                    MDLabel:
                        id: label5
                        text: "Loan is credited to a/c: xxxxxxxxxxx"
                        theme_text_color: "Custom"
                        text_color: 86/255, 94/255, 97/255, 1
                        size_hint_y: None
                        height:50

                    MDLabel:
                        id: sub_label4
                        text: "Pending..."
                        theme_text_color: "Custom"
                        text_color: 0, 0, 1, 1
                        size_hint_y: None
                        height: 15  # Adjust height as needed
                        font_style: "Caption"


"""
Builder.load_string(application_tracker)


class ApplicationTrackerScreen(Screen):
    def initialize_with_value(self, value, data):
        email = self.get_table()
        profile = app_tables.fin_user_profile.search()
        print(value)
        loan_id = []
        loan_amount = []
        loan_status = []
        product_name = []
        sub_date = []
        lender_accepted_date = []
        lender_disbursed_date = []

        for i in data:
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])
            sub_date.append(i['borrower_loan_created_timestamp'])
            lender_accepted_date.append(i['lender_accepted_timestamp'])
            lender_disbursed_date.append(i['loan_disbursed_timestamp'])
        profile_email_id = []
        profile_account_number = []

        for i in profile:
            profile_email_id.append(i['email_user'])
            profile_account_number.append(i['account_number'])

        index1 = -1  # Initialize index1 to a default value

        if email in profile_email_id:
            index1 = profile_email_id.index(email)

        if value in loan_id:
            index = loan_id.index(value)
            print(f"Loan Status: {loan_status[index]}")
            print(f"Processing loan with ID {value}")
            if loan_status[index] == 'under process':  # label1
                print('under process')
                self.ids.icon1.icon = 'circle-slice-8'
                self.ids.icon1.theme_text_color = "Custom"
                self.ids.icon1.text_color = 0, 1, 0, 1
                if self.ids.icon1.canvas.before.children:
                    for instruction in self.ids.icon1.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0, 1, 0, 1  # Green color
                self.ids.label1.text = f"Application for {product_name[index]} product loan sent"
                self.ids.label1.theme_text_color = "Custom"
                self.ids.label1.text_color = 0, 0, 0, 1
                self.ids.label1.bold = True
                self.ids.sub_label1.text = f"{sub_date[index].strftime('%Y-%m-%d')}"
                self.ids.sub_label1.text_color = 0, 0, 0, 1
                self.ids.sub_label1.bold = True
                self.ids.icon3.icon = 'checkbox-blank-circle-outline'
                self.ids.icon3.theme_text_color = "Custom"
                self.ids.icon3.text_color = 0, 0, 0, 1
                if self.ids.icon3.canvas.before.children:
                    for instruction in self.ids.icon3.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0, 0, 0, 1  # Green color
                self.ids.label3.text = f"Loan Approval status"
                self.ids.label3.theme_text_color = "Custom"
                self.ids.label3.text_color = 0, 0, 0, 1
                self.ids.label3.bold = False
                self.ids.sub_label2.text = f"Pending..."
                self.ids.sub_label2.text_color = 0, 0, 0, 1
                self.ids.sub_label2.bold = False
                self.ids.icon4.icon = 'checkbox-blank-circle-outline'
                self.ids.icon4.theme_text_color = "Custom"
                self.ids.icon4.text_color = 0, 0, 0, 1
                if self.ids.icon4.canvas.before.children:
                    for instruction in self.ids.icon4.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0, 0, 0, 1  # Green color
                self.ids.label4.theme_text_color = "Custom"
                self.ids.label4.text_color = 0, 0, 0, 1
                self.ids.label4.bold = False
                self.ids.sub_label3.text = f"Pending..."
                self.ids.sub_label3.text_color = 0, 0, 0, 1
                self.ids.sub_label3.bold = False
                self.ids.icon5.icon = 'checkbox-blank-circle-outline'
                self.ids.icon5.theme_text_color = "Custom"
                self.ids.icon5.text_color = 0, 0, 0, 1
                masked_account_number = 'xxxxxx' + profile_account_number[index1][-4:]
                self.ids.label5.text = f"Loan credited to a/c {masked_account_number}"
                self.ids.label5.theme_text_color = "Custom"
                self.ids.label5.text_color = 0, 0, 0, 1
                self.ids.label5.bold = False
                self.ids.sub_label4.text = f"Pending..."
                self.ids.sub_label4.text_color = 0, 0, 0, 1
                self.ids.sub_label4.bold = False

            elif loan_status[index] == 'approved':  # label2
                self.ids.icon1.icon = 'circle-slice-8'
                self.ids.icon1.theme_text_color = "Custom"
                self.ids.icon1.text_color = 0, 1, 0, 1
                if self.ids.icon1.canvas.before.children:
                    for instruction in self.ids.icon1.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0, 1, 0, 1  # Green color
                self.ids.label1.text = f"Application for {product_name[index]} product loan sent"
                self.ids.label1.theme_text_color = "Custom"
                self.ids.label1.text_color = 0, 0, 0, 1
                self.ids.label1.bold = True
                self.ids.sub_label1.text = f"{sub_date[index].strftime('%Y-%m-%d')}"
                self.ids.sub_label1.text_color = 0, 0, 0, 1
                self.ids.sub_label1.bold = True
                self.ids.icon3.icon = 'circle-slice-8'
                self.ids.icon3.theme_text_color = "Custom"
                self.ids.icon3.text_color = 0, 1, 0, 1
                if self.ids.icon3.canvas.before.children:
                    for instruction in self.ids.icon3.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0, 1, 0, 1  # Green color
                self.ids.label3.text = f'Loan is approved for ₹{loan_amount[index]:.2f}'
                self.ids.label3.theme_text_color = "Custom"
                self.ids.label3.text_color = 0, 0, 0, 1
                self.ids.label3.bold = True
                self.ids.sub_label2.text = f"{lender_accepted_date[index].strftime('%Y-%m-%d %H:%M:%S')}"
                self.ids.sub_label2.text_color = 0, 0, 0, 1
                self.ids.sub_label2.bold = True
                self.ids.icon4.icon = 'checkbox-blank-circle-outline'
                self.ids.icon4.theme_text_color = "Custom"
                self.ids.icon4.text_color = 0, 0, 0, 1
                if self.ids.icon4.canvas.before.children:
                    for instruction in self.ids.icon4.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0, 0, 0, 1  # Green color
                self.ids.label4.theme_text_color = "Custom"
                self.ids.label4.text_color = 0, 0, 0, 1
                self.ids.label4.bold = False
                self.ids.sub_label3.text = f"Pending..."
                self.ids.sub_label3.text_color = 0, 0, 0, 1
                self.ids.sub_label3.bold = False
                self.ids.icon5.icon = 'checkbox-blank-circle-outline'
                self.ids.icon5.theme_text_color = "Custom"
                self.ids.icon5.text_color = 0, 0, 0, 1
                masked_account_number = 'xxxxxx' + profile_account_number[index1][-4:]
                self.ids.label5.text = f"Loan credited to a/c {masked_account_number}"
                self.ids.label5.theme_text_color = "Custom"
                self.ids.label5.text_color = 0, 0, 0, 1
                self.ids.label5.bold = False
                self.ids.sub_label4.text = f"Pending..."
                self.ids.sub_label4.text_color = 0, 0, 0, 1
                self.ids.sub_label4.bold = False

            elif loan_status[index] == 'disbursed':  # label3
                self.ids.icon1.icon = 'circle-slice-8'
                self.ids.icon1.theme_text_color = "Custom"
                self.ids.icon1.text_color = 0, 1, 0, 1
                if self.ids.icon1.canvas.before.children:
                    for instruction in self.ids.icon1.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0, 1, 0, 1  # Green color
                self.ids.label1.text = f"Application for {product_name[index]} product loan sent"
                self.ids.label1.theme_text_color = "Custom"
                self.ids.label1.text_color = 0, 0, 0, 1
                self.ids.label1.bold = True
                self.ids.sub_label1.text = f"{sub_date[index].strftime('%Y-%m-%d')}"
                self.ids.sub_label1.text_color = 0, 0, 0, 1
                self.ids.sub_label1.bold = True
                self.ids.icon3.icon = 'circle-slice-8'
                self.ids.icon3.theme_text_color = "Custom"
                self.ids.icon3.text_color = 0, 1, 0, 1
                if self.ids.icon3.canvas.before.children:
                    for instruction in self.ids.icon3.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0, 1, 0, 1  # Green color
                self.ids.label3.text = f'Loan is approved for ₹{loan_amount[index]:.2f}'
                self.ids.label3.theme_text_color = "Custom"
                self.ids.label3.text_color = 0, 0, 0, 1
                self.ids.label3.bold = True
                self.ids.sub_label2.text = f"{lender_accepted_date[index].strftime('%Y-%m-%d %H:%M:%S')}"
                self.ids.sub_label2.text_color = 0, 0, 0, 1
                self.ids.sub_label2.bold = True
                self.ids.icon4.icon = 'circle-slice-8'
                self.ids.icon4.theme_text_color = "Custom"
                self.ids.icon4.text_color = 0, 1, 0, 1
                if self.ids.icon4.canvas.before.children:
                    for instruction in self.ids.icon4.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0, 1, 0, 1  # Green color
                self.ids.label4.text = f"{product_name[index]} product loan has been disbursed"
                self.ids.label4.theme_text_color = "Custom"
                self.ids.label4.text_color = 0, 0, 0, 1
                self.ids.label4.bold = True
                self.ids.sub_label3.text = f"{lender_disbursed_date[index].strftime('%Y-%m-%d %H:%M:%S')}"
                self.ids.sub_label3.text_color = 0, 0, 0, 1
                self.ids.sub_label3.bold = True
                self.ids.icon5.icon = 'circle-slice-8'
                self.ids.icon5.theme_text_color = "Custom"
                self.ids.icon5.text_color = 0, 1, 0, 1
                # to hide account number
                masked_account_number = 'xxxxxx' + profile_account_number[index1][-4:]
                self.ids.label5.text = f"Loan credited to a/c {masked_account_number}"
                self.ids.label5.theme_text_color = "Custom"
                self.ids.label5.text_color = 0, 0, 0, 1
                self.ids.label5.bold = True
                self.ids.sub_label4.text = f"Transaction Done."
                self.ids.sub_label4.text_color = 0, 0, 0, 1
                self.ids.sub_label4.bold = True

            elif loan_status[index] == 'rejected':
                self.ids.icon1.icon = 'circle-slice-8'
                self.ids.icon1.theme_text_color = "Custom"
                self.ids.icon1.text_color = 0, 1, 0, 1
                if self.ids.icon1.canvas.before.children:
                    for instruction in self.ids.icon1.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0, 1, 0, 1  # Green color
                self.ids.label1.text = f"Application Rejected"
                self.ids.label1.theme_text_color = "Custom"
                self.ids.label1.text_color = 0, 0, 0, 1
                self.ids.label1.bold = True
                self.ids.sub_label1.text = f"{sub_date[index].strftime('%Y-%m-%d')}"
                self.ids.sub_label1.text_color = 0, 0, 0, 1
                self.ids.icon3.icon = 'cancel'
                self.ids.icon3.theme_text_color = "Custom"
                self.ids.icon3.text_color = 0.902, 0.141, 0.278, 1
                if self.ids.icon3.canvas.before.children:
                    for instruction in self.ids.icon3.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0.902, 0.141, 0.278, 1  # Green color
                self.ids.label3.text = f'Loan is Rejected ₹{loan_amount[index]:.2f}'
                self.ids.label3.theme_text_color = "Custom"
                self.ids.label3.text_color = 0, 0, 0, 1
                self.ids.label3.bold = True
                self.ids.sub_label2.text = f"cancel..."
                self.ids.sub_label2.text_color = 1, 0, 0, 1
                self.ids.icon4.icon = 'checkbox-blank-circle-outline'
                self.ids.icon4.theme_text_color = "Custom"
                self.ids.icon4.text_color = 0, 0, 0, 1
                if self.ids.icon4.canvas.before.children:
                    for instruction in self.ids.icon4.canvas.before.children:
                        if isinstance(instruction, Color):
                            instruction.rgba = 0, 0, 0, 1  # Green color
                self.ids.label4.theme_text_color = "Custom"
                self.ids.label4.text_color = 0, 0, 0, 1
                self.ids.label4.bold = False
                self.ids.sub_label3.text = f"Pending..."
                self.ids.sub_label3.text_color = 0, 0, 0, 1
                self.ids.sub_label3.bold = False
                self.ids.icon5.icon = 'checkbox-blank-circle-outline'
                self.ids.icon5.theme_text_color = "Custom"
                self.ids.icon5.text_color = 0, 0, 0, 1
                masked_account_number = 'xxxxxx' + profile_account_number[index1][-4:]
                self.ids.label5.text = f"Loan credited to a/c {masked_account_number}"
                self.ids.label5.theme_text_color = "Custom"
                self.ids.label5.text_color = 0, 0, 0, 1
                self.ids.label5.bold = False
                self.ids.sub_label4.text = f"Pending..."
                self.ids.sub_label4.text_color = 0, 0, 0, 1
                self.ids.sub_label4.bold = False

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def borrower_dashboard(self):
        self.manager.current = 'ALLLoansAPT'


class ALLLoansAPT(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)

        if not data:
            print("No data found for email:", email)
            return

        for row in data:
            if row['user_photo']:
                image_data = row['user_photo'].get_bytes()
                if isinstance(image_data, bytes):
                    try:
                        profile_texture_io = BytesIO(image_data)
                        photo_texture = CoreImage(profile_texture_io, ext='png').texture
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                else:
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        profile_texture_io = BytesIO(image_data_binary)
                        photo_texture = CoreImage(profile_texture_io, ext='png').texture
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")

        data = app_tables.fin_loan_details.search()
        email = self.get_table()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        email1 = []
        borrower_name = []
        loan_status = []
        product_name = []
        loan_amount = []
        interest_amount = []
        processing_fee = []
        tenure = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])
            email1.append(i['borrower_email_id'])
            loan_amount.append(i['loan_amount'])
            interest_amount.append(i['total_interest_amount'])
            processing_fee.append(i['total_processing_fee_amount'])
            tenure.append(i['tenure'])
        profile_customer_id = []
        profile_mobile_number = []
        profile_email_id = []
        profile_account_number = []
        ascend_value = []

        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email_id.append('email_user')
            profile_account_number.append('account_number')
            ascend_value.append(i['ascend_value'])
        cos_id = None
        index = -1
        if email in profile_email_id:
            index = profile_email_id.index(email)

        if email in email1:
            index = email1.index(email)
            cos_id = customer_id[index]

        if cos_id is not None:
            print(cos_id, type(cos_id))
            print(customer_id[-1], type(customer_id[-1]))
            c = -1
            index_list = []
            for i in range(s):
                c += 1
                if customer_id[c] == cos_id:
                    index_list.append(c)

            b = 1
            k = -1
            for i in reversed(index_list):
                b += 1
                k += 1
                number = profile_customer_id.index(customer_id[i])
                card = MDCard(
                    orientation='horizontal',
                    size_hint=(None, None),
                    size=("380dp", "200dp"),
                    padding="12dp",
                    spacing="5dp",
                    elevation=1,
                    radius=[0, 0, 0, 0]
                )
                middle_box = MDBoxLayout(orientation='vertical', size_hint_x=0.05,
                                       pos_hint={"center_y": 0.59}, )
                card.add_widget(middle_box)
                # Left side: User information
                left_box = MDBoxLayout(orientation='vertical',padding=dp(10) ,size_hint_x=0.5,pos_hint={"center_y": 0.59},)
                if photo_texture:
                    image = CircularImage(texture=photo_texture)
                    left_box.add_widget(image)

                left_box.add_widget(MDLabel(
                    text=f"[b]{borrower_name[i]}[/b]",
                    markup=True,
                    font_size='18sp',
                    font_style='Caption',  # You can adjust font style as needed
                    theme_text_color='Primary',
                    halign='left',
                ))

                left_box.add_widget(MDLabel(
                    text=f"[b]{profile_mobile_number[number]}[/b]",
                    markup=True,
                    size_hint=(None, None),
                    height="50dp",
                    font_size='15sp',
                    font_style='Caption',  # You can adjust font style as needed
                    theme_text_color='Primary',
                    halign='left',
                ))
                left_box.add_widget(MDLabel(
                    text=f" ",
                    markup=True,
                    font_size='15sp',
                    font_style='Subtitle2',  # You can adjust font style as needed
                    theme_text_color='Secondary',
                    halign='left',
                ))
                left_box.add_widget(MDLabel(
                    text=f" ",
                    markup=True,
                    font_size='15sp',
                    font_style='Subtitle2',  # You can adjust font style as needed
                    theme_text_color='Primary',
                    halign='left',
                ))

                card.add_widget(left_box)
                # Define status color
                status_color = (0.545, 0.765, 0.290, 1)  # default color
                if loan_status[i] == "under process":
                    status_color = (253 / 255, 218 / 255, 13 / 255, 1)
                elif loan_status[i] == "disbursed loan":
                    status_color = (0.8588, 0.4392, 0.5765, 1.0)
                elif loan_status[i] == "closed":
                    status_color = (0.4235, 0.5569, 0.1373, 1.0)
                elif loan_status[i] == "extension":
                    status_color = (1.0, 0.6275, 0.4824, 1.0)
                elif loan_status[i] == "foreclosure":
                    status_color = (0.0, 0.749, 1.0, 1.0)
                elif loan_status[i] == "rejected":
                    status_color = (0.902, 0.141, 0.141, 1)
                elif loan_status[i] == "approved":
                    status_color = (0.2353, 0.7019, 0.4431, 1.0)
                elif loan_status[i] == "lost opportunities":
                    status_color = (0.902, 0.141, 0.141, 1)

                # Right side: Loan details
                right_box = MDBoxLayout(orientation='vertical', size_hint_x=0.7)

                right_box.add_widget(MDLabel(
                    text=f"[b][color=000000]Loan Status:[/color] {loan_status[i]}[/b]",
                    markup=True,
                    font_size='15sp',
                    font_style='Caption',  # You can adjust font style as needed
                    theme_text_color='Custom',
                    halign='left',
                    text_color=status_color
                ))

                right_box.add_widget(MDLabel(
                    text=f"[b]Product Name:[/b] {product_name[i]}",
                    markup=True,
                    font_size='10sp',
                    font_style='Caption',  # You can adjust font style as needed
                    theme_text_color='Primary',
                    halign='left',
                ))

                right_box.add_widget(MDLabel(
                    text=f"[b]Loan Amount:[/b] {loan_amount[i]}",
                    markup=True,
                    font_size='10sp',
                    font_style='Caption',  # You can adjust font style as needed
                    theme_text_color='Primary',
                    halign='left',
                ))
                right_box.add_widget(MDLabel(
                    text=f"[b]Tenure:[/b] {tenure[i]}",
                    markup=True,
                    font_size='10sp',
                    font_style='Caption',  # You can adjust font style as needed
                    theme_text_color='Primary',
                    halign='left',
                ))
                right_box.add_widget(MDLabel(
                    text=f"[b]Processing Fee:[/b] {processing_fee[i]}",
                    markup=True,
                    font_size='10sp',
                    font_style='Caption',  # You can adjust font style as needed
                    theme_text_color='Primary',
                    halign='left',
                ))

                right_box.add_widget(MDLabel(
                    text=f"[b]Interest Amount:[/b] {interest_amount[i]}",
                    markup=True,
                    font_size='10sp',
                    font_style='Caption',  # You can adjust font style as needed
                    theme_text_color='Primary',
                    halign='left',
                ))

                button2 = MDFlatButton(
                    text="  View Details  ",
                    size_hint=(None, None),
                    height="50dp",
                    width="250dp",
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),  # White color in RGBA format
                    pos_hint={"center_x": 0.7},
                    md_bg_color="#1E90FF",  # Background color in a shade of blue
                    on_release=lambda x, i=i: self.icon_button_clicked(x, loan_id[i])
                )

                right_box.add_widget(button2)
                card.add_widget(right_box)

                self.ids.container.add_widget(card)

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'another_method' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def icon_button_clicked(self, instance, loan_id):
        # Highlight the selected item
        self.highlight_item(instance)

        data = app_tables.fin_loan_details.search()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        sm = self.manager

        # Create a new instance of the ApplicationTrackerScreen
        approved = ApplicationTrackerScreen(name='ApplicationTrackerScreen')

        # Add the ApplicationTrackerScreen to the existing ScreenManager
        sm.add_widget(approved)

        # Switch to the ApplicationTrackerScreen
        sm.current = 'ApplicationTrackerScreen'
        self.manager.get_screen('ApplicationTrackerScreen').initialize_with_value(loan_id, data)

    def highlight_item(self, item):
        # Deselect all other items
        self.deselect_items()

        # Change the background color of the clicked item to indicate selection
        item.bg_color = (0.5, 0.5, 0.5, 1)  # Change color as desired
        self.selected_item = item

    def deselect_items(self):
        # Deselect all items in the list
        for item in self.ids.container.children:
            if isinstance(item, ThreeLineAvatarIconListItem):
                item.bg_color = (1, 1, 1, 1)  # Reset background color for all items

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()

    def go_back(self):
        self.manager.current = 'DashboardScreen'


class WindowManager(ScreenManager):
    pass


class CircularImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = ("80dp", "100dp")  # Initial size of the image
        self.bind(pos=self.update_shape, size=self.update_shape)

    def update_shape(self, *args):
        self.canvas.before.clear()

        # Calculate the diameter of the circle
        diameter = min(self.width, self.height)
        radius = diameter / 2.0

        # Calculate the position of the ellipse to center it on the image
        ellipse_pos = (self.center_x - radius, self.center_y - radius)

        with self.canvas.before:
            StencilPush()
            Ellipse(pos=ellipse_pos, size=(diameter, diameter))
            StencilUse()

        self.canvas.after.clear()
        with self.canvas.after:
            StencilUnUse()
            Ellipse(pos=ellipse_pos, size=(diameter, diameter))
            StencilPop()