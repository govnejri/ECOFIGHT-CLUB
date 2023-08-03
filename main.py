import random
import openai
import sys
from config import API_KEY
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsProxyWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class GraphicsViewWithCanvas(QtWidgets.QGraphicsView):
    def __init__(self, canvas):
        super(GraphicsViewWithCanvas, self).__init__()
        proxy = QGraphicsProxyWidget()
        proxy.setWidget(canvas)
        self.setScene(QtWidgets.QGraphicsScene())
        self.scene().addItem(proxy)
        self.setSceneRect(0, 0, 800, 400)

class Ui_MainWindow(object):

    def __init__(self):
        self.a = 0
        self.b = 0
        self.influnc =0


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 760)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-2, 0, 1366, 704))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_1)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, -1, 1366, 704))
        self.tabWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_2.setAutoFillBackground(False)
        self.tabWidget_2.setStyleSheet("")
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 1300, 281))
        self.label.setMinimumSize(QtCore.QSize(0, 81))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(170, 320, 331, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 420, 331, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 1300, 291))
        self.label_2.setStyleSheet("")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit.setGeometry(QtCore.QRect(10, 310, 1300, 91))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 420, 491, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 1300, 271))
        self.label_8.setObjectName("label_8")

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 1366, 704))
        self.tabWidget_3.setStyleSheet("border-color: rgb(255, 255, 255);\n""border-color: rgb(0, 170, 0);\n""")
        self.tabWidget_3.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_6)
        self.graphicsView.setGeometry(QtCore.QRect(30, 10, 741, 330))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.label_9 = QtWidgets.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(330, 350, 600, 71))
        self.label_9.setObjectName("label_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 350, 241, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_4 = QtWidgets.QLabel(self.tab_7)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 1280, 121))
        self.label_4.setStyleSheet("")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_7)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 1280, 41))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 360, 451, 81))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab_8)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 20, 661, 281))
        self.graphicsView_2.setStyleSheet("")
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.pushButton_6 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 330, 270, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget_3.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        with open(r"C:\Users\bekan\PycharmProjects\JASAHUBHAKATONDA\styles.css", 'r') as f:
            style = f.read()

        # Примените стили к каждому виджету
        MainWindow.setStyleSheet(style)
        self.tabWidget.setStyleSheet(style)
        self.tabWidget_2.setStyleSheet(style)
        self.tabWidget_3.setStyleSheet(style)
        self.tab_1.setStyleSheet(style)
        self.tab_2.setStyleSheet(style)
        self.tab_3.setStyleSheet(style)
        self.tab_4.setStyleSheet(style)
        self.tab_5.setStyleSheet(style)
        self.tab_6.setStyleSheet(style)
        self.tab_7.setStyleSheet(style)
        self.tab_8.setStyleSheet(style)
        self.label.setStyleSheet(style)
        self.label_2.setStyleSheet(style)
        self.label_4.setStyleSheet(style)
        self.label_5.setStyleSheet(style)

        self.label_8.setStyleSheet(style)
        self.label_9.setStyleSheet(style)

        self.textEdit.setStyleSheet(style)

        self.achivs_quantity = 0
        self.addfunction()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "ПОЛУЧИТЬ ЗАДАНИЕ"))
        self.pushButton_3.setText(_translate("MainWindow", "Я ВЫПОЛНИЛ ЗАДАНИЕ"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "ЕЖЕДНЕВНЫЕ ЗАДАНИЯ"))
        self.label_2.setText(_translate("MainWindow", "ПОГОВОРИ С УЧИТЕЛЕМ"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Напишите свой вопрос</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "ЗАДАТЬ ВОПРОС"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "РАЗГОВОР С ТАЙЛЕРОМ"))
        self.label_8.setText(_translate("MainWindow", "ТВОИ ДОСТИЖЕНИЯ"))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "ТВОИ ДОСТИЖЕНИЯ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "ЗАДАНИЯ"))
        self.label_9.setText(_translate("MainWindow", "СОСТОЯНИЕ ВОЗДУХА ГОРОДА АЛМАТЫ"))
        self.pushButton_4.setText(_translate("MainWindow", "ВЫВЕСТИ ГРАФИК"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "ОБЩЕЕ СОСТОЯНИЕ "))
        self.label_4.setText(_translate("MainWindow", ""))
        self.pushButton_5.setText(_translate("MainWindow", "РАСЧИТАТЬ МОЕ ВЛИЯНИЕ"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("MainWindow", "ТВОЕ ВЛИЯНИЕ  "))

        self.pushButton_6.setText(_translate("MainWindow", "СОСТАВИТЬ ПРОГНОЗ"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("MainWindow", "ПРОГНОЗ НА БУДУЩЕЕ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "СОСТОЯНИЕ ВОЗДУХА АЛМАТЫ"))


    def addfunction(self):
        self.pushButton.clicked.connect(lambda: self.give_task())
        self.pushButton_3.clicked.connect(lambda: self.complite())
        self.pushButton_2.clicked.connect(lambda: self.gpt_interaction())
        self.pushButton_4.clicked.connect(lambda: self.graph())
        self.pushButton_6.clicked.connect(lambda: self.forecast())
        self.pushButton_5.clicked.connect(lambda: self.influence())


    def give_task(self):
         try:
            self.KEY = API_KEY
            openai.api_key = self.KEY
            prompt = "А теперь составь мне одно конкретное  задания для того чтобы я помог решить проблему смога в Алматы. Задание должно быть максимально кратко и быть про экологию."
            role = "представь себя как главный герой фильма Бойцовский луб Тайлер Дерден. используй манеру речи и другие изюминки данного интересного персонажа и отвечай в таком формате на все мои сообщения в этом чате. Отвечай коротко и без сильного уважения ко мне, отвечай как будто ты не зависим от пользователя и несильно волнуешься о нем   а также не стоит делать все что я тебе говорю. Если я слишком много говорю скажи это мне как сказал бы гордый Тайлер ты можешь использовать подходящие цитаты из Бойцовского клуба. Только не матерись и несильно обижай меняНе зови меня братам и так далее делай вид что я твой ученик."

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content":role},
                    {"role": "user", "content": prompt },
                ],
            )

            if response and response['choices']:
                answer = response['choices'][0]['message']['content'].strip()
                answer = str(answer)
                self.achivs_quantity =random.randint(7, 9)
                self.label.setText(answer + " Баллы за задание:" + str(self.achivs_quantity))
            else:
                self.label.setText("Учитель задумался((( попробуй спросить еще раз")

         except Exception as e:
            print(f"Произошла ошибка: {e}")


    def complite(self):
        self.a += self.achivs_quantity
        self.b +=1
        self.label_8.setText(f"Общее количество баллов: {self.a} Количество выполненных заданий {self.b}")


    def gpt_interaction(self):
        try:
            self.KEY = API_KEY
            openai.api_key = self.KEY

            # Получаем вопрос от пользователя из textEdit
            prompt = self.textEdit.toPlainText()

            # Роль для GPT-3.5 Turbo, замените значение role на свое
            role = "представь себя как главный герой фильма Бойцовский луб Тайлер Дерден. используй манеру речи и другие изюминки данного интересного персонажа и отвечай в таком формате на все мои сообщения в этом чате. Отвечай коротко и без сильного уважения ко мне, отвечай как будто ты не зависим от пользователя и несильно волнуешься о нем   а также не стоит делать все что я тебе говорю. Если я слишком много говорю скажи это мне как сказал бы гордый Тайлер ты можешь использовать подходящие цитаты из Бойцовского клуба. Только не матерись.Если тебя спросили что ты Тайлер Дерден ты можешь ответить  'Ты не прав, мы оба Тайлеры Дерданы'"

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": role},
                    {"role": "user", "content": prompt},
                ],
            )

            if response and response['choices']:
                answer = response['choices'][0]['message']['content'].strip()
                answer = str(answer)
                self.label_2.setText(answer)
            else:
                self.label_2.setText("Учитель задумался((( попробуй спросить еще раз")

        except Exception as e:
            print(f"Произошла ошибка: {e}")


    def graph(self):
        try:
            file_path = r"C:\Users\bekan\PycharmProjects\JASAHUBHAKATONDA\almaty_data.xlsx"
            try:
                df = pd.read_excel(file_path, parse_dates=["date"], index_col="date")
            except FileNotFoundError:
                print(f"Файл {file_path} не найден.")
                return
            df = df.sort_index()
            df = df.drop_duplicates()
            df = df.dropna()  # удалить строки с пропусками
            # или
            df = df.fillna(0)  # заполнить пропуски нулями (можно использовать другое значение вместо 0)

            # Clear the previous scene
            self.graphicsView.setScene(QGraphicsScene())

            # Create the figure and axes for the plot
            fig, ax = plt.subplots(figsize=(self.graphicsView.width() / 100, self.graphicsView.height() / 100))

            # Plot the data with different colors for each parameter
            colors = ["red", "blue", "green", "yellow", "orange"]  # Add more colors if needed
            for i, column in enumerate(df.columns):
                ax.plot(df.index, df[column], label=column.upper(), color=colors[i])

            # Set background color of the plot to white
            ax.set_facecolor("white")

            # Set labels and title with black color
            ax.set_xlabel("Дата", color="black")
            ax.set_ylabel("Уровень загрязнения", color="black")
            ax.set_title("Анализ данных о загрязнении воздуха", color="black")

            # Set legend text color to black
            ax.legend(loc="upper left", facecolor="white", edgecolor="black", fontsize=10, labelcolor="black")

            # Set tick labels color to black
            ax.tick_params(axis="both", colors="black")

            # Create a FigureCanvas
            canvas = FigureCanvas(fig)

            # Set the canvas in the custom QGraphicsView
            graphics_view = GraphicsViewWithCanvas(canvas)
            self.graphicsView.setScene(graphics_view.scene())
            AQI = df.max()
            self.label_9.setText(f"Индекс загрязнения воздуха по данным PM2,5 AQI : {AQI[0]}")
        except Exception as e:
            print("Ошибка при обработке данных:", e)


    def forecast(self):
        try:
            file_path = r"C:\Users\bekan\PycharmProjects\JASAHUBHAKATONDA\almaty_data_forecast.xlsx"
            try:
                df = pd.read_excel(file_path, parse_dates=["date"], index_col="date")
            except FileNotFoundError:
                print(f"Файл {file_path} не найден.")
                return

            # Clear the previous scene
            self.graphicsView_2.setScene(QGraphicsScene())

            # Create the figure and axes for the plot
            fig, ax = plt.subplots(figsize=(self.graphicsView_2.width() / 100, self.graphicsView_2.height() / 100))

            # Plot the forecast data with a line plot
            ax.plot(df.index, df["co(forecast)"], label="CO Forecast", color="purple")

            # Set background color of the plot to white
            ax.set_facecolor("white")

            # Set labels and title with black color
            ax.set_xlabel("Дата", color="black")
            ax.set_ylabel("Прогноз CO", color="black")
            ax.set_title("Прогноз уровня CO воздуха", color="black")

            # Set legend text color to black
            ax.legend(loc="upper left", facecolor="white", edgecolor="black", fontsize=10, labelcolor="black")

            # Set tick labels color to black
            ax.tick_params(axis="both", colors="black")

            # Create a FigureCanvas
            canvas = FigureCanvas(fig)

            # Set the canvas in the custom QGraphicsView
            graphics_view = GraphicsViewWithCanvas(canvas)
            self.graphicsView_2.setScene(graphics_view.scene())

        except Exception as e:
            print("Ошибка при обработке данных:", e)


    def influence(self):
        self.influnc = 2*(self.a*self.b)/1000
        if self.influnc > 1:
            self.label_4.setText(f"Неплохо для обычного человека, ты практически дошел до действительно влиятельного уровня. Твой уровень влияния на решение проблемы смога составляет: {self.influnc}")
        else:
            self.label_4.setText(f"Так себе( тебе предстоит трудиться еще больше чтобы помочь решить проблему смога своего города. Твой уровень влияния составляет: {self.influnc}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())