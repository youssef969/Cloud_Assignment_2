from flet import * 



class Login(Column):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        # self.page.window.full_screen = False
        self.page.padding = 0
        self.page.title = "Login"
        self.page.window.resizable = True
        self.page.fonts={"pac":r"assets/Pacifico-Regular.ttf"}
        self.null = Text("")
        # self.page.on_resized = self.on_resize  
       
        

        self.Login_text =Text(value="Login",font_family="pac",size=30,selectable=False)

        self.Email_textfeild = TextField(label="",border=InputBorder.UNDERLINE,hint_text="Type Your E-mail",hint_style=TextStyle(color=Colors.BLACK38))
        self.Email = ListTile(title=Text("Email",weight=FontWeight.W_700),subtitle=self.Email_textfeild)

        self.Password_textfeild = TextField(label="",border=InputBorder.UNDERLINE,hint_text="Type Your Password",hint_style=TextStyle(color=Colors.BLACK38),can_reveal_password=True,password=True,counter=TextButton(text="Forgot Password?",))
        self.password = ListTile(title=Text("Password",weight=FontWeight.W_700),subtitle=self.Password_textfeild)

        self.sign_up = Text(value="or Signup Using")
        self.sign_up_button = TextButton(text="   Signup   ")
        sign_up_login = Column(controls=[self.sign_up,self.sign_up_button],alignment=MainAxisAlignment.CENTER)
        gradient = LinearGradient(colors=["#e332ed","#5ed1d7"],begin=alignment.top_right,end=alignment.bottom_left)

        self.login_button = Container(content=Row([Text("LOGIN",weight=FontWeight.BOLD,color=Colors.WHITE,text_align=TextAlign.CENTER)],alignment=MainAxisAlignment.CENTER),gradient=gradient,width=300,height=40,border_radius=45,on_click=lambda :print,ink=True)
        Controls_Column = Column(controls=[self.null,self.Login_text,self.null,self.Email,self.password,self.null,self.login_button,self.null,self.null,sign_up_login],alignment=MainAxisAlignment.START,horizontal_alignment=CrossAxisAlignment.CENTER)
        self.login_container = Container(content=Controls_Column,width=400,height=600,border_radius=30,bgcolor="White")
        self.main_container = Container(content=Row(controls=[self.login_container],alignment=MainAxisAlignment.CENTER),gradient=gradient,width=self.page.width,height=self.page.height,expand=True)
        self.controls = [self.main_container]
        
        
    # def on_resize(self):
    #     self.main_container.width = self.page.width
    #     self.main_container.height = self.page.height
    #     self.main_container.update()

        

def main(page:Page):
    interface = Login(page)
    page.add(interface)
    page.update()
    
app(target=main,assets_dir=r"D:\My Download\DULMS\Codes\Cloud\Assignment",view=AppView.WEB_BROWSER)  # Here You Must Change path to Your actual Path
        