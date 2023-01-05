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

import clipboard


class App(UserControl):
    

    def build(self):
        self.CardColumn = Column()
        self.snack = SnackBar(Text('Number copied!'))

        return Container(
            content=(
                Column(
                    alignment='center',
                    controls=[
                        # self.EntryForm(),
                        # self.WalletContainer(),
                    ],
                )
            ),
            width=900,
            height=800,
            margin=margin.all(-10),
            # gradient=self.GradientGenerator(
            #     cl.BACKGROUND["from"], cl.BACKGROUND['to']),
            alignment=alignment.center,
        )
