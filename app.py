import asyncio
import flet
from flet import (
    Column,
    SnackBar,
    Text,
    Container,
    margin,
    alignment,
    AlertDialog,
    TextField,
    TextButton,
    LinearGradient,
    border_radius,
    padding,
    Image,
    UserControl,
    Row,
    IconButton,
    icons,
    border,
    Card,
    transform,
    animation,
    Icon
)
from settings import ColorList as cl
import clipboard


class App(UserControl):
    global HeightCount
    HeightCount = 25

    global ColorCount
    ColorCount = 0

    global CardCount
    CardCount = 0

    global DataDict
    DataDict = {}

    def WalletContainer(self):
        self.CardList = Column(
            alignment='start',
            spacing=25,
        )

        self.ImportButton = IconButton(
            icon=icons.DOWNLOAD,
            icon_size=16,
            # on_click=lambda e: asyncio.run(self.CheckDatabase()),
        )

        self.InsertButton = IconButton(
            icon=icons.ADD,
            icon_size=16,
            on_click=lambda e: self.OpenEntryForm(),
            disabled=True,
        )

        self.WalletContainer = Container(
            # Use CARD to get elevation feature
            content=Card(
                elevation=15,
                content=Container(
                    content=Column(
                        scroll="auto",
                        alignment="start",
                        spacing=25,
                        controls=[
                            self.snack,
                            Row(
                                alignment="spaceBetween",
                                controls=[
                                    # Title of the app
                                    Text(
                                        "Wallite", color="white", size=20, weight="bold"
                                    ),
                                    # Container with the icon buttons
                                    Container(
                                        content=Row(
                                            spacing=0,
                                            tight=True,
                                            alignment="end",
                                            controls=[
                                                self.InsertButton,
                                                self.ImportButton,
                                            ],
                                        )
                                    ),
                                ],
                            ),
                            Container(
                                content=Column(
                                    controls=[self.CardList],
                                ),
                            ),
                        ],
                    ),
                    width=360,
                    height=580,
                    padding=padding.all(20),
                    alignment=alignment.top_center,
                    border_radius=border_radius.all(15),
                    gradient=self.GradientGenerator(
                        cl.WALLITE["from"], cl.WALLITE["to"]
                    ),
                ),
            ),
        )

        return self.WalletContainer

    def EntryForm(self):
        self.BankName = TextField(
            label='Card Name',
            border='underline',
            text_size=12
        )

        self.CardNumber = TextField(
            label='Card Number',
            border='underline',
            text_size=12
        )

        self.CardCVV = TextField(
            label='Card CVV',
            border='underline',
            text_size=12
        )

        self.EntryForm = AlertDialog(
            title=Text(
                'Enter Your Bank Name\nCard Number',
                text_align='center',
                size=12,
            ),
            content=Column(
                [
                    self.BankName,
                    self.CardNumber,
                    self.CardCVV,
                ],
                spacing=15,
                height=280
            ),
            actions=[
                TextButton('Insert',
                           on_click=lambda e: self.CheckEntryForm()),
                TextButton(
                    'Cancel', on_click=lambda e: self.CancelEntryForm()),
            ],
            actions_alignment='center',
            on_dismiss=lambda e: self.CancelEntryForm(),
        )

        return self.EntryForm

    def OpenEntryForm(self):
        self.dialog = self.EntryForm
        self.EntryForm.open = True
        self.update()
    
    def CancelEntryForm(self):
        self.BankName.value, self.CardNumber.value, self.CardCVV.value = (
            None,
            None,
            None,
        )

        self.BankName.error_text, self.CardNumber.error_text, self.CardCVV.error_text = (
            None,
            None,
            None,
        )

        self.EntryForm.open = False
        self.update()


    def GradientGenerator(self, start, end):
        self.ColorGradient = LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=[
                start,
                end,
            ],
        )
        return self.ColorGradient

    def build(self):
        self.CardColumn = Column()
        self.snack = SnackBar(Text('Number copied!'))

        return Container(
            content=(
                Column(
                    alignment='center',
                    controls=[
                        # self.EntryForm(),
                        self.WalletContainer(),
                    ],
                )
            ),
            width=900,
            height=800,
            margin=margin.all(-10),
            gradient=self.GradientGenerator(
                cl.BACKGROUND["from"], cl.BACKGROUND['to']),
            alignment=alignment.center,
        )
