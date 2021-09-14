
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from loadfile import *

class Ui_SMARTWATCH_WINDOW(object):
    def __init__(self):
        self.loadedconfig=False
        self.loadedsimulacion=False
    #!▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def setupUi(self, SMARTWATCH_WINDOW):

        # todo▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▄▀▄   SMARTWATCH  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ 
        self.principalwindow(SMARTWATCH_WINDOW)

        #! se cargan los gifs
        self.loadgifs()

        #! se cargan la tabla
        self.tableensamblaje()

        #! se cargan el combobox y el boton
        self.mycombobox()
        #! se carga el widget de proceso de abajo
        self.widgetprocess()  

        #! se cargan los cuadros del centro
        self.widgetscomponents()

        #! se cargan labels de subtitulos
        self.addlabelsextra()

        #! se cargan la barra de estado
        self.statusbar(SMARTWATCH_WINDOW)

    def loadgifs(self):

        self.LABEL_BACKGROUND = QtWidgets.QLabel(self.centralwidget)
        self.LABEL_BACKGROUND.setGeometry(QtCore.QRect(0, 0, 981, 531))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.LABEL_BACKGROUND.setFont(font)
        self.LABEL_BACKGROUND.setMidLineWidth(-1)
        self.LABEL_BACKGROUND.setText("")
        self.LABEL_BACKGROUND.setTextFormat(QtCore.Qt.AutoText)
        # self.LABEL_BACKGROUND.setPixmap(QtGui.QPixmap("Codigo Fuente/images/giphy.gif"))

        self.movie=QMovie("Codigo Fuente/images/giphy.gif")
        self.LABEL_BACKGROUND.setMovie(self.movie)
        self.movie.start()
        self.LABEL_BACKGROUND.setScaledContents(True)
        self.LABEL_BACKGROUND.setObjectName("LABEL_BACKGROUND")
        self.startAnimation()
        self.lbl_myicon = QtWidgets.QLabel(self.centralwidget)
        self.lbl_myicon.setGeometry(QtCore.QRect(890, 470, 71, 71))
        self.lbl_myicon.setText("")
        # self.lbl_myicon.setPixmap(QtGui.QPixmap("../../../../../Pictures/oie_25212249BZ616093.gif"))
        self.movie2=QMovie("../../../../../Pictures/oie_25212249BZ616093.gif")
        self.lbl_myicon.setMovie(self.movie2)
        self.movie2.start()
        self.lbl_myicon.setScaledContents(True)
        self.lbl_myicon.setObjectName("lbl_myicon")
        self.lbl_reloj = QtWidgets.QLabel(self.centralwidget)
        self.lbl_reloj.setGeometry(QtCore.QRect(770, -10, 241, 171))
        self.lbl_reloj.setText("")
        # self.lbl_reloj.setPixmap(QtGui.QPixmap("Codigo Fuente/images/dribble-clock.gif"))
        self.movie3=QMovie("Codigo Fuente/images/dribble-clock.gif")
        self.lbl_reloj.setMovie(self.movie3)
        self.movie3.start()
        self.lbl_reloj.setScaledContents(True)
        self.lbl_reloj.setObjectName("lbl_reloj")
        self.lbl_SMARTWATCH = QtWidgets.QLabel(self.centralwidget)
        self.lbl_SMARTWATCH.setGeometry(QtCore.QRect(35, 30, 415, 90))
        self.lbl_SMARTWATCH.setText("")
        self.lbl_SMARTWATCH.setPixmap(QtGui.QPixmap("Codigo Fuente/images/cooltext392345411513032.gif"))
        self.lbl_SMARTWATCH.setScaledContents(True)
        self.lbl_SMARTWATCH.setObjectName("lbl_SMARTWATCH")
        self.movie5=QMovie("Codigo Fuente/images/cooltext392345411513032.gif")
        self.lbl_SMARTWATCH.setMovie(self.movie5)
        self.movie5.start()
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(910, 150, 101, 71))
        self.label_5.setText("")
        # self.label_5.setPixmap(QtGui.QPixmap("Codigo Fuente/images/Gear1.gif"))
        self.movie4=QMovie("Codigo Fuente/images/Gear1.gif")
        self.label_5.setMovie(self.movie4)
        self.movie4.start()
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.lbl_BRAZOROBOTICO = QtWidgets.QLabel(self.centralwidget)
        self.lbl_BRAZOROBOTICO.setGeometry(QtCore.QRect(-90, 200, 361, 321))
        self.lbl_BRAZOROBOTICO.setText("")
        # self.lbl_BRAZOROBOTICO.setPixmap(QtGui.QPixmap("Codigo Fuente/images/robot.gif"))
        self.lbl_BRAZOROBOTICO.setScaledContents(True)
        self.lbl_BRAZOROBOTICO.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_BRAZOROBOTICO.setObjectName("lbl_BRAZOROBOTICO")
        self.movie6=QMovie("Codigo Fuente/images/robot.gif")
        self.lbl_BRAZOROBOTICO.setMovie(self.movie6)
        self.movie6.start()   

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(160, 520, 651, 16))
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

    def principalwindow(self, SMARTWATCH_WINDOW):
        SMARTWATCH_WINDOW.setObjectName("SMARTWATCH_WINDOW")
        SMARTWATCH_WINDOW.setWindowModality(QtCore.Qt.NonModal)
        SMARTWATCH_WINDOW.resize(968, 583)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        SMARTWATCH_WINDOW.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Users/Sr. C/Users/Sr. C/Pictures/FACING.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SMARTWATCH_WINDOW.setWindowIcon(icon)
        SMARTWATCH_WINDOW.setLayoutDirection(QtCore.Qt.LeftToRight)
        SMARTWATCH_WINDOW.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(SMARTWATCH_WINDOW)
        self.centralwidget.setObjectName("centralwidget")

    def mycombobox(self):

        self.combo = QtWidgets.QComboBox(self.centralwidget)
        self.combo.setGeometry(QtCore.QRect(500, 20, 191, 31))
        self.combo.setObjectName("combo")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Codigo Fuente/images/Gear1.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo.addItem(icon1, "")
        self.combo.addItem(icon1,"")
        self.combo.addItem(icon1,"")
        self.combo.addItem(icon1,"")
        self.combo.addItem(icon1,"")

        self.btn_ensamblar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ensamblar.setGeometry(QtCore.QRect(500, 60, 191, 31))
        self.btn_ensamblar.setObjectName("btn_ensamblar")

    def tableensamblaje(self):
        self.lcd_time = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_time.setGeometry(QtCore.QRect(700, 80, 111, 41))
        self.lcd_time.setAutoFillBackground(False)
        self.lcd_time.setObjectName("lcd_time")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Codigo Fuente/images/Gear1.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(610, 160, 341, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        
        self.table_ensamblaje = QtWidgets.QTableWidget(self.centralwidget)
        self.table_ensamblaje.setGeometry(QtCore.QRect(610, 160, 350, 311))
        self.table_ensamblaje.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_ensamblaje.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_ensamblaje.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_ensamblaje.setAutoScrollMargin(14)
        self.table_ensamblaje.setIconSize(QtCore.QSize(4, 4))
        self.table_ensamblaje.setGridStyle(QtCore.Qt.SolidLine)
        self.table_ensamblaje.setObjectName("table_ensamblaje")
        self.table_ensamblaje.setColumnCount(3)
        


        # item = QtWidgets.QTableWidgetItem()
        # font = QtGui.QFont()
        # font.setFamily("JetBrains Mono")
        # font.setPointSize(9)
        # font.setBold(True)
        # font.setWeight(75)
        # item.setFont(font)
        # self.table_ensamblaje.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # font = QtGui.QFont()
        # font.setFamily("JetBrains Mono")
        # font.setPointSize(9)
        # font.setBold(True)
        # font.setWeight(75)
        # item.setFont(font)
        # self.table_ensamblaje.setVerticalHeaderItem(1, item)

        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Codigo Fuente/images/clock-alarm-clock.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        item.setBackground(QtGui.QColor(128, 130, 249))
        self.table_ensamblaje.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setIcon(icon1)
        item.setBackground(QtGui.QColor(141, 200, 245))
        self.table_ensamblaje.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setIcon(icon1)
        item.setBackground(QtGui.QColor(171, 222, 255))
        self.table_ensamblaje.setHorizontalHeaderItem(2, item)



        self.table_ensamblaje.setRowCount(11)
        for f in range(0,10):
            for c in range(0,3):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setFamily("JetBrains Mono")
                font.setPointSize(9)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                font.setKerning(True)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(168, 199, 249))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setBackground(brush)
                self.table_ensamblaje.setItem(f, c, item)
                item = self.table_ensamblaje.item(f, c)
                item.setText("1 segundo")

    def widgetprocess(self):
        self.widget_proceso = QtWidgets.QListWidget(self.centralwidget)
        self.widget_proceso.setEnabled(True)
        self.widget_proceso.setGeometry(QtCore.QRect(200, 400, 391, 91))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono Medium")
        font.setPointSize(11)
        font.setItalic(True)
        self.widget_proceso.setFont(font)
        self.widget_proceso.setAcceptDrops(False)
        self.widget_proceso.setToolTip("")
        self.widget_proceso.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_proceso.setAutoFillBackground(False)
        self.widget_proceso.setStyleSheet("")
        self.widget_proceso.setFrameShape(QtWidgets.QFrame.VLine)
        self.widget_proceso.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widget_proceso.setLineWidth(0)
        self.widget_proceso.setMidLineWidth(0)
        self.widget_proceso.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.widget_proceso.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.widget_proceso.setAutoScroll(True)
        self.widget_proceso.setAutoScrollMargin(16)
        self.widget_proceso.setProperty("showDropIndicator", True)
        self.widget_proceso.setDragEnabled(False)
        self.widget_proceso.setAlternatingRowColors(True)
        self.widget_proceso.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.widget_proceso.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.widget_proceso.setIconSize(QtCore.QSize(113, 43))
        self.widget_proceso.setTextElideMode(QtCore.Qt.ElideRight)
        self.widget_proceso.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.widget_proceso.setMovement(QtWidgets.QListView.Static)
        self.widget_proceso.setFlow(QtWidgets.QListView.LeftToRight)
        self.widget_proceso.setProperty("isWrapping", False)
        self.widget_proceso.setResizeMode(QtWidgets.QListView.Fixed)
        self.widget_proceso.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.widget_proceso.setViewMode(QtWidgets.QListView.IconMode)
        self.widget_proceso.setModelColumn(0)
        self.widget_proceso.setUniformItemSizes(False)
        self.widget_proceso.setBatchSize(100)
        self.widget_proceso.setWordWrap(False)
        self.widget_proceso.setSelectionRectVisible(False)
        self.widget_proceso.setObjectName("widget_proceso")

        
        for p in range(0,5):
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            font.setStrikeOut(False)
            font.setStyleStrategy(QtGui.QFont.PreferDefault)
            item.setFont(font)
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("Codigo Fuente/images/Flecha_tesela.svg - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon3)
            brush = QtGui.QBrush(QtGui.QColor(178, 255, 96))
            brush.setStyle(QtCore.Qt.Dense1Pattern)
            item.setBackground(brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            
            self.widget_proceso.addItem(item)
            item = self.widget_proceso.item(p)
            item.setText( str(p))  

    def widgetscomponents(self):
        self.widget_components1 = QtWidgets.QListWidget(self.centralwidget)
        self.widget_components1.setGeometry(QtCore.QRect(200, 180, 181, 171))
        self.widget_components1.setObjectName("widget_components1")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(39, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.widget_components1.addItem(item)
        
        self.widget_components2 = QtWidgets.QListWidget(self.centralwidget)
        self.widget_components2.setGeometry(QtCore.QRect(390, 180, 181, 171))
        self.widget_components2.setObjectName("widget_components2")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(39, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.widget_components2.addItem(item)

    def addlabelsextra(self):
        self.lbl_componentnecesarios = QtWidgets.QLabel(self.centralwidget)
        self.lbl_componentnecesarios.setGeometry(QtCore.QRect(230, 140, 321, 31))
        
        
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_componentnecesarios.setFont(font)
        self.lbl_componentnecesarios.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_componentnecesarios.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_componentnecesarios.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_componentnecesarios.setScaledContents(True)
        self.lbl_componentnecesarios.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_componentnecesarios.setWordWrap(False)
        self.lbl_componentnecesarios.setOpenExternalLinks(False)
        self.lbl_componentnecesarios.setObjectName("lbl_componentnecesarios")
        self.lbl_procesorealizado = QtWidgets.QLabel(self.centralwidget)
        self.lbl_procesorealizado.setGeometry(QtCore.QRect(250, 360, 321, 31))
        
        
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_procesorealizado.setFont(font)
        self.lbl_procesorealizado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_procesorealizado.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_procesorealizado.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_procesorealizado.setScaledContents(True)
        self.lbl_procesorealizado.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_procesorealizado.setWordWrap(False)
        self.lbl_procesorealizado.setOpenExternalLinks(False)
        self.lbl_procesorealizado.setObjectName("lbl_procesorealizado")
    
    def statusbar(self,SMARTWATCH_WINDOW):

        #!▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▄▀▄   STATUS BAR   ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ 
        SMARTWATCH_WINDOW.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SMARTWATCH_WINDOW)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 31))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")

        #?▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▄▀▄   CARGAR ARCHIVOS   ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
        self.menuCARGAR_ARCHIVOS = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.menuCARGAR_ARCHIVOS.setFont(font)
        self.menuCARGAR_ARCHIVOS.setObjectName("menuCARGAR_ARCHIVOS")

        self.actionARCHIVO_DE_CONFIGURACI_N = QtWidgets.QAction(SMARTWATCH_WINDOW)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionARCHIVO_DE_CONFIGURACI_N.setFont(font)
        self.actionARCHIVO_DE_CONFIGURACI_N.setObjectName("actionARCHIVO_DE_CONFIGURACI_N")
        self.actionARCHIVO_DE_CONFIGURACI_N.triggered.connect(self.load_fileconfig)

        self.actionARCHIVO_DE_SIMULACI_N = QtWidgets.QAction(SMARTWATCH_WINDOW)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionARCHIVO_DE_SIMULACI_N.setFont(font)
        self.actionARCHIVO_DE_SIMULACI_N.setObjectName("actionARCHIVO_DE_SIMULACI_N")
        self.actionARCHIVO_DE_SIMULACI_N.triggered.connect(self.load_filesimulacion)


        #?▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▄▀▄   VER REPORTES   ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
        self.menuREPORTES = QtWidgets.QMenu(self.menubar)
        self.menuREPORTES.setObjectName("menuREPORTES")

        self.actionREPORTE_DE_SIMULACI_N = QtWidgets.QAction(SMARTWATCH_WINDOW)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.actionREPORTE_DE_SIMULACI_N.setFont(font)
        self.actionREPORTE_DE_SIMULACI_N.setObjectName("actionREPORTE_DE_SIMULACI_N")
        self.actionREPORTE_DE_COLA_DE_SECUENCIA = QtWidgets.QAction(SMARTWATCH_WINDOW)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.actionREPORTE_DE_COLA_DE_SECUENCIA.setFont(font)
        self.actionREPORTE_DE_COLA_DE_SECUENCIA.setObjectName("actionREPORTE_DE_COLA_DE_SECUENCIA")


        #?▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        # *▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▄▀▄   AYUDA   ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
        self.menuAYUDA = QtWidgets.QMenu(self.menubar)
        self.menuAYUDA.setObjectName("menuAYUDA")

        self.actionINFORMACI_N_PERSONAL = QtWidgets.QAction(SMARTWATCH_WINDOW)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.actionINFORMACI_N_PERSONAL.setFont(font)
        self.actionINFORMACI_N_PERSONAL.setObjectName("actionINFORMACI_N_PERSONAL")
        self.actionACERCA_DE = QtWidgets.QAction(SMARTWATCH_WINDOW)
        self.actionACERCA_DE.setCheckable(False)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.actionACERCA_DE.setFont(font)
        self.actionACERCA_DE.setObjectName("actionACERCA_DE")



        SMARTWATCH_WINDOW.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SMARTWATCH_WINDOW)
        self.statusbar.setObjectName("statusbar")
        SMARTWATCH_WINDOW.setStatusBar(self.statusbar)

        #?▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬       
        self.menuCARGAR_ARCHIVOS.addAction(self.actionARCHIVO_DE_CONFIGURACI_N)
        self.menuCARGAR_ARCHIVOS.addSeparator()
        self.menuCARGAR_ARCHIVOS.addAction(self.actionARCHIVO_DE_SIMULACI_N)
        self.menuCARGAR_ARCHIVOS.addSeparator()

        self.menuREPORTES.addAction(self.actionREPORTE_DE_SIMULACI_N)
        self.menuREPORTES.addSeparator()
        self.menuREPORTES.addAction(self.actionREPORTE_DE_COLA_DE_SECUENCIA)
        self.menuREPORTES.addSeparator()

        self.menuAYUDA.addAction(self.actionINFORMACI_N_PERSONAL)
        self.menuAYUDA.addSeparator()
        self.menuAYUDA.addAction(self.actionACERCA_DE)
        self.menuAYUDA.addSeparator()

        self.menubar.addAction(self.menuCARGAR_ARCHIVOS.menuAction())
        self.menubar.addAction(self.menuREPORTES.menuAction())
        self.menubar.addAction(self.menuAYUDA.menuAction())
        self.retranslateUi(SMARTWATCH_WINDOW)
        self.widget_proceso.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(SMARTWATCH_WINDOW)

    def startAnimation(self):
        self.movie.start()

    def retranslateUi(self, SMARTWATCH_WINDOW):
        _translate = QtCore.QCoreApplication.translate
        SMARTWATCH_WINDOW.setWindowTitle(_translate("SMARTWATCH_WINDOW", "MainWindow"))
        # self.combo.setItemText(0, _translate("SMARTWATCH_WINDOW", "New Item"))
        # self.combo.setItemText(1, _translate("SMARTWATCH_WINDOW", "New Item"))
        # self.combo.setItemText(2, _translate("SMARTWATCH_WINDOW", "New Item"))
        # self.combo.setItemText(3, _translate("SMARTWATCH_WINDOW", "New Item"))
        # self.combo.setItemText(4, _translate("SMARTWATCH_WINDOW", "New Item"))

        self.btn_ensamblar.setText(_translate("SMARTWATCH_WINDOW", "ENSAMBLAR"))
        self.table_ensamblaje.setSortingEnabled(False)

        item = self.table_ensamblaje.horizontalHeaderItem(0)
        item.setText(_translate("SMARTWATCH_WINDOW", "TIEMPO"))
        item = self.table_ensamblaje.horizontalHeaderItem(1)
        item.setText(_translate("SMARTWATCH_WINDOW", "LINEA 1"))
        item = self.table_ensamblaje.horizontalHeaderItem(2)
        item.setText(_translate("SMARTWATCH_WINDOW", "LINEA 2"))
        __sortingEnabled = self.table_ensamblaje.isSortingEnabled()
        self.table_ensamblaje.setSortingEnabled(False)

        # for i in range(0,5):
        #     for j in range(0,2):
        

        

        self.table_ensamblaje.setSortingEnabled(__sortingEnabled)




        self.widget_proceso.setSortingEnabled(False)
        __sortingEnabled = self.widget_proceso.isSortingEnabled()
        self.widget_proceso.setSortingEnabled(False)
        

        



        self.widget_proceso.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.widget_components1.isSortingEnabled()
        self.widget_components1.setSortingEnabled(False)
        item = self.widget_components1.item(0)
        item.setText(_translate("SMARTWATCH_WINDOW", "New Item"))
        self.widget_components1.setSortingEnabled(__sortingEnabled)
        self.lbl_componentnecesarios.setText(_translate("SMARTWATCH_WINDOW", "Componentes Necesarios"))
        self.lbl_procesorealizado.setText(_translate("SMARTWATCH_WINDOW", "Procesos Realizados"))
        __sortingEnabled = self.widget_components2.isSortingEnabled()
        self.widget_components2.setSortingEnabled(False)
        item = self.widget_components2.item(0)
        item.setText(_translate("SMARTWATCH_WINDOW", "New Item"))
        self.widget_components2.setSortingEnabled(__sortingEnabled)
        self.menuCARGAR_ARCHIVOS.setTitle(_translate("SMARTWATCH_WINDOW", "CARGAR ARCHIVOS"))
        self.menuREPORTES.setTitle(_translate("SMARTWATCH_WINDOW", "REPORTES"))
        self.menuAYUDA.setTitle(_translate("SMARTWATCH_WINDOW", "AYUDA"))
        self.actionARCHIVO_DE_CONFIGURACI_N.setText(_translate("SMARTWATCH_WINDOW", "ARCHIVO DE CONFIGURACIÓN"))
        self.actionARCHIVO_DE_SIMULACI_N.setText(_translate("SMARTWATCH_WINDOW", "ARCHIVO DE SIMULACIÓN"))
        self.actionREPORTE_DE_SIMULACI_N.setText(_translate("SMARTWATCH_WINDOW", "REPORTE DE SIMULACIÓN"))
        self.actionREPORTE_DE_COLA_DE_SECUENCIA.setText(_translate("SMARTWATCH_WINDOW", "REPORTE DE COLA DE SECUENCIA"))
        self.actionINFORMACI_N_PERSONAL.setText(_translate("SMARTWATCH_WINDOW", "INFORMACIÓN PERSONAL"))
        self.actionACERCA_DE.setText(_translate("SMARTWATCH_WINDOW", "ACERCA DE"))

    def load_fileconfig(self):
         
        if self.loadedconfig:
            print("El archivo de configuracion ya se ha cargado")
        else:
            loadfile(0)
            self.loadedconfig=True

    def load_filesimulacion(self):
        global lista_lista_productos
        if self.loadedsimulacion:
            print("Cargando el archivo de simulación, otra vez...")
            loadfile(1)
        else:
            loadfile(1)
            self.loadedsimulacion=True

        # for l in lista_lista_productos.:
        #     t=str(list[l][0]) 
        #     t = re.sub("\"","",t)           
        #     self.comboBox.addItem(t)
        #     a=showoriginal()
        #     print(len(list))
        # a.genoriginal(list)

