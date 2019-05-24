import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Winform(QMainWindow):
	def __init__(self, parent=None):
		super(Winform, self).__init__(parent)
		self.lastPoint_t = QPointF()  # 触屏点前一点

		self.endPoint_t = QPointF()  # 触屏点后一点

		self.lastPoint_m = QPointF()  # 鼠标点前一点

		self.endPoint_m = QPointF()  # 鼠标点后一点

		self.eraser_width = 50  # 黑板擦默认宽度

		self.pix = QPixmap()  # 画布
		self.setWindowOpacity(0.8)
		self.penWidth_t = 10;  # 触摸笔画的原始粗细，会随触点粗细变化
		self.penWidth_m = 5;  # 鼠标点的粗细固定
		self.setMouseTracking(False)
		self.pos_xy = []
		self.pen = QPen(Qt.red, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)  # 画笔
		self.pen.setColor(QColor(Qt.blue))  # 设置初始颜色
		self.init()
	def init(self):
		bar=self.menuBar()
		file=bar.addMenu("文件")
		file.addAction("hello")
		open=QAction('打开',self)
		open.setShortcut("Ctrl")
		file.addAction(open)
		save=QAction('保存',self)
		save.setShortcut('Ctrl+S')
		file.triggered[QAction].connect(self.proce)
		file.addAction(save)
		self.label=QLabel(" ",self)
		self.label.move(1770,200)
		self.setEnabled(True)
		self.setWindowTitle("简单绘画工具")
		self.setWindowIcon(QIcon('o.jpg'))
		self.resize(1920, 1080)
		self.button1 = QPushButton('点击更换画笔颜色', self)
		self.button1.setIcon(QIcon('o.jpg'))
		self.button1.move(1780, 20)
		self.button1.clicked.connect(self.change)
		self.button2 = QPushButton('更换字体大小', self)
		self.button2.setIcon(QIcon('o.jpg'))
		self.button2.move(1780, 50)
		self.button2.clicked.connect(self.font)

		self.button3 = QPushButton('更换背景颜色', self)
		self.button3.setIcon(QIcon('o.jpg'))
		self.button3.move(1780, 80)
		self.button3.clicked.connect(self.background_color)

		self.button4 = QPushButton('更换画布颜色', self)
		self.button4.setIcon(QIcon('o.jpg'))
		self.button4.move(1780, 110)
		self.button4.clicked.connect(self.painter_color)

		self.button5= QPushButton("保存",self)
		self.button5.setIcon(QIcon('o.jpg'))
		self.button5.move(1780, 140)
		self.button5.clicked.connect(self.on_btn_Save_Clicked)
		
		self.lab= QLabel("按Q退出",self)
		self.lab.move(1800, 170)
		self.lab1= QLabel("按C清除画板",self)
		self.lab1.move(1800, 200)
		palette = QPalette()
		palette.setColor(QPalette.Window, Qt.gray)  # 背景颜色
		self.setPalette(palette)

		self.pix = QPixmap(1770, 900)#画步
		self.pix.fill(Qt.white)
		self.pp = QPainter(self.pix)
		self.pp.setPen(self.pen)
	def GetContentAsQImage(self):
        #获取画板内容（返回QImage）
		image = self.pix.toImage()
		return image
	def on_btn_Save_Clicked(self):
		savePath = QFileDialog.getSaveFileName(self, 'Save Your Paint', '.\\', '*.png')
		print(savePath)
		if savePath[0] == "":
			print("Save cancel")
			return
		image = self.GetContentAsQImage()
		image.save(savePath[0])
	def proce(self,q):
		if q.text()=="打开":
			self.images()
	def images(self):
		fname,_=QFileDialog.getSaveFileName(self,'open file','c:\\',"Image files(*.jpg *.gif)")
		self.label.setPixmap(QPixmap(fname))
		print("已经打印")

	def painter_color(self):
		color = QColorDialog.getColor(Qt.green, self, "Select Color")
		self.pix.fill(color)
	def background_color(self):
		color = QColorDialog.getColor(Qt.green, self, "Select Color")
		palette = QPalette()
		palette.setColor(QPalette.Window, color)  # 背景颜色
		self.setPalette(palette)

	def change(self):
		color = QColorDialog.getColor(Qt.green, self, "Select Color")
		self.pen.setColor(QColor(color))  # 设置初始颜色
	def font(self):
		num,ok=QInputDialog.getInt(self,"text int Dialog",'输入你想要该变的字体大小')
		if ok:

			self.penWidth_m=num
	def paintEvent(self,event):
		self.pen.setWidthF(self.penWidth_m)  # 采用触摸点大小作为笔宽
		self.pp.setPen(self.pen)
		self.pp.drawLine(self.lastPoint_m, self.endPoint_m)
		self.lastPoint_m = self.endPoint_m
		painter = QPainter(self)
		painter.setPen(self.pen)
		painter.drawPixmap(0, 0, self.pix)
	def mousePressEvent(self, event): #右键不可连续
		if event.button() == Qt.LeftButton:
			self.lastPoint_m = event.pos()
			self.endPoint_m = self.lastPoint_m
	def mouseMoveEvent(self, event):
		if event.buttons() and Qt.LeftButton:
			self.endPoint_m = event.pos()
			pos_tmp = (event.pos().x(), event.pos().y())

			self.pos_xy.append(pos_tmp)

			self.update()



	def eventFilter(self, watched, event):
		if watched == form:
			if event.type() == QEvent.TouchBegin:
				pass

			if event.type() == QEvent.TouchUpdate or event.type() == QEvent.TouchEnd:
				self.addline(QTouchEvent(event))

				return True
				if event.type() == QEvent.MouseButtonDblClick or event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonRelease or event.type() == QEvent.MouseButtonPress:

					mouse_event = QMouseEvent(event)
				if mouse_event != None and mouse_event.source() == Qt.MouseEventSynthesizedBySystem:
					pass

			if event.type() == QEvent.Paint:
				self.paintEvent(event)



				return True

		return QWidget.eventFilter(self, watched, event)  # 其他情况会返回系统默认的事件处理方法。



	def keyPressEvent(self, event):#按键事件

		if event.key() == Qt.Key_C:

			self.pix.fill(Qt.white)#将PIx对象背景为红色色

			self.update()#清除所有的线条

		elif event.key() == Qt.Key_Q :

			self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Winform()

    app.installEventFilter(form)

    form.show()

    #form.showFullScreen()

    sys.exit(app.exec_())
