from flet import *
import flet



Osnova = Container(
    Container(
        Stack([
            Container(
                height=1024,
                width=1024,
                border_radius=20,
                bgcolor="transparent",
                blur=Blur(10,10,BlurTileMode.MIRROR),
            ),
            Container(
                Stack([
                    Container(
                        height=724,
                        width=354,
                        border_radius=20,
                        bgcolor="black",
                    ),
                ]),padding=padding.only(335,150),
            ),
            Container(
                Stack([
                    Container(
                        height=720,
                        width=350,
                        border_radius=20,
                        bgcolor="transparent",
                        blur=Blur(200,200, BlurTileMode.DECAL),
                    ),
                    Container(
                        ElevatedButton(
                            content = Text(
                                "SIGN IN",
                                color="white",
                                weight="w500",
                                size=20,
                                bgcolor="#3d2563",      
                            ),bgcolor="#3d2563", width=300,
                        ), padding=padding.only(20,500)
                    ),
                    Container(
                            Text(
                                "Sign in",
                                width=350,
                                size=25,
                                color="#faf9fe",
                                weight="w700",
                                text_align="center",
                            ),padding=padding.only(0, 150),
                        ),
                        Container(
                            Row([
                                Icon(
                                    icons.ARROW_FORWARD_IOS,
                                    color="#faf9fe",
                                    size=20,
                                ),
                            ]),padding=padding.only(120, 608),
                        ),
                        Container(
                            Text(
                                "Sign up",
                                width=350,
                                size=20,
                                
                                color="#faf9fe",
                                weight="w500",
                            ),padding=padding.only(20, 600),
                        ),
                        Container(
                            Row([
                                Text(
                                    "Don't have an account?",
                                    color= "#7dc9f2",
                                ),
                            ]), padding=padding.only(20, 560),
                        ),
                        Container(
                            Text(
                                "E-Mail",
                                width=350,
                                size= 16,
                                color="#faf9fe",
                                weight="w300",
                            ),padding= padding.only(20,250),
                        ),
                        Container(
                            Column([
                                Container(
                                    TextField(
                                        width=300,
                                        height=45,
                                        border_radius=10,
                                        border_color="#3d2563",
                                        prefix_icon=icons.EMAIL_ROUNDED, 
                                        color= "#bc46fe",
                                        hint_text="yourname@gmail.com"
                                    ),
                                ),
                            ]), padding=padding.only(20, 285),
                        ),
                        Container(
                            Text(
                                "Password",  
                                width=350,
                                size= 16,
                                color="#faf9fe",
                                weight="w300",
                            ),padding= padding.only(20,350),
                        ),
                        Container(
                            Column([
                                Container(
                                    TextField(
                                        password=True, 
                                        can_reveal_password=True,
                                        width=300,
                                        height=45,
                                        border_radius=10,
                                        border_color="#3d2563",
                                        prefix_icon=icons.LOCK, 
                                        color= "#bc46fe",
                                        hint_text="yourpassword",
                                    ),
                                ),
                            ]), padding=padding.only(20, 385),
                        ),
                    Container(
                        Container(
                            Column([
                                Container(
                                    Image(
                                        src="NEWimages-Photoroom.png",
                                        width=90,
                                        color="black",
                                    ),
                                ),
                            ]), padding=padding.only(130,30),
                        ),
                        
                    ),
                ]), padding=padding.only(337,152),
            ),
        ]),
    ),

    height=1024,
    width=1024,
    gradient=SweepGradient(["#295465", "#1e1b2e", "#342156", "#3b2635", "#2b4a67", "#452634", "#1b1a2a", "#212d45"]),
    
)

def main(page:Page):
    page.window_max_width = 1024
    page.window_max_height = 1024
    page.padding = 0
    
    page.add(Osnova)
    

flet.app(target=main)