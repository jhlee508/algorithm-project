import random
import sys
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(".\\TeamProject.ui")[0] #두번째화면 Ui
first_class = uic.loadUiType(".\\Main.ui")[0] #첫번째화면 Ui
jeju_class=uic.loadUiType(".\\MAP\\jeju.ui")[0]
ulsan_class=uic.loadUiType(".\\MAP\\ulsan.ui")[0]
masan_class=uic.loadUiType(".\\MAP\\masan.ui")[0]
pohang_class=uic.loadUiType(".\\MAP\\pohang.ui")[0]
mungyeong_class=uic.loadUiType(".\\MAP\\mungyeong.ui")[0]
gwangyang_class=uic.loadUiType(".\\MAP\\gwangyang.ui")[0]
jeonnam_class=uic.loadUiType(".\\MAP\\jeonnam.ui")[0]
jeonbuk_class=uic.loadUiType(".\\MAP\\jeonbuk.ui")[0]
daejeon_class=uic.loadUiType(".\\MAP\\daejeon.ui")[0]
yesan_class=uic.loadUiType(".\\MAP\\yesan.ui")[0]
chungju_class=uic.loadUiType(".\\MAP\\chungju.ui")[0]
cheongju_class=uic.loadUiType(".\\MAP\\cheongju.ui")[0]
taebeak_class=uic.loadUiType(".\\MAP\\taebaek.ui")[0]
chuncheon_class=uic.loadUiType(".\\MAP\\chuncheon.ui")[0]
jeonju_class=uic.loadUiType(".\\MAP\\jeonju.ui")[0]
uijeongbu_class=uic.loadUiType(".\\MAP\\uijeongbu.ui")[0]
incheon_class=uic.loadUiType(".\\MAP\\incheon.ui")[0]
busanbookbu_class=uic.loadUiType(".\\MAP\\busanbookbu.ui")[0]
busannambu_class=uic.loadUiType(".\\MAP\\busannambu.ui")[0]
yongin_class=uic.loadUiType(".\\MAP\\yongin.ui")[0]
ansan_class=uic.loadUiType(".\\MAP\\ansan.ui")[0]
dobong_class=uic.loadUiType(".\\MAP\\dobong.ui")[0]
gangseo_class=uic.loadUiType(".\\MAP\\gangseo.ui")[0]
seobu_class=uic.loadUiType(".\\MAP\\seobu.ui")[0]
gangnam_class=uic.loadUiType(".\\MAP\\gangnam.ui")[0]
course_class= uic.loadUiType(".\\MAP\\course_main.ui")[0]
#전역변수
answer=[] #정답 입력 배열
idx=1 
w_answer=[] #틀린문제 넣는 배열 나중에 다시풀기 누르면 Problem으로 들어감
w_answer_2=[]
Sorted=[]
w_answer_idx=[] #인덱스 출력을 위해 넣는 인덱스 배열
w_n=[] #출력시 [] 빼기위해 넣는 배열
original=[[1, 1, 82],[2, 2, 71],[3, 3, 76],[4, 1, 46],[5, 2, 39],[6, 4, 56],[7, 3, 62],[8, 3, 64],[9, 3, 48],[10, 2, 59],[11, 1, 63],
[12, 2, 49],[13, 3, 61],[14, 3, 71],[15, 4, 23],[16, 4, 67],[17, 1, 83],[18, 2, 29],[19, 2, 37],[20, 1, 84],[21, 2, 76],[22, 3, 44],[23, 4, 53],
[24, 1, 26],[25, 3, 83],[26, 3, 92],[27, 4, 37],[28, 1, 63],[29, 3, 52],[30, 1, 37],[31, 4, 54],[32, 4, 68],[33, 2, 85],[34, 3, 93],[35, 1, 71],
[36, 3, 92],[37, 2, 98],[38, 3, 96],[39, 4, 89],[40, 2, 93],[41, 3, 72],[42, 4, 46],[43, 1, 69],[44, 3, 42],[45, 1, 56],[46, 2, 58],[47, 1, 66],
[48, 1, 97],[49, 4, 98],[50, 1, 99],[51, 3, 34],[52, 1, 95],[53, 2, 75],[54, 3, 53],[55, 4, 77],[56, 4, 88],[57, 2, 83],[58, 2, 80],[59, 1, 66],
[60, 4, 71],[61, 1, 98],[62, 2, 33],[63, 2, 83],[64, 3, 77],[65, 2, 88],[66, 2, 44],[67, 1, 62],[68, 2, 95],[69, 2, 83],[70, 3, 84],[71, 2, 96],
[72, 1, 73],[73, 1, 62],[74, 2, 62],[75, 4, 54],[76, 4, 80],[77, 2, 72],[78, 2, 85],[79, 1, 34],[80, 3, 68],[81, 4, 86],[82, 1, 91],[83, 3, 76],
[84, 3, 49],[85, 1, 38],[86, 3, 81],[87, 4, 87],[88, 4, 89],[89, 1, 89],[90, 1, 93],[91, 3, 50],[92, 1, 35],[93, 1, 33],[94, 3, 88],[95, 4, 96],
[96, 2, 93],[97, 3, 91],[98, 2, 95],[99, 4, 87],[100, 3, 90],[101, 4, 63],[102, 1, 83],[103, 4, 75],[104, 2, 80],[105, 2, 38],[106, 1, 34],[107, 3, 74],
[108, 4, 77],[109, 1, 82],[110, 1, 58],[111, 2, 98]] #original문제 배열 이거 절대 건들면 안됨!

problem=[[0,0,100]] #유형별, 모의고사 풀이시 넣는 문제

class jeju(QMainWindow,jeju_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\제주1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)
    


  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\제주{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False) 

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\제주{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)  
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)  

class ulsan(QMainWindow,ulsan_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\울산1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()


  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

class masan(QMainWindow,masan_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\마산1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)


  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\마산{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)


  def front_trans_image(self):#이미지 변환
      global idx
      if idx<2:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\마산{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==2:
        self.pushButton_2.setEnabled(False)

class pohang(QMainWindow,pohang_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\포항1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)


  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\포항{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\포항{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)  
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)  

class mungyeong(QMainWindow,mungyeong_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\문경1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\문경{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<2:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\문경{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==2:
        self.pushButton_2.setEnabled(False)

class gwangyang(QMainWindow,gwangyang_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\광양1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\광양{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<3:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\광양{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint() 
      self.pushButton.setEnabled(True)
      if idx==3:
        self.pushButton_2.setEnabled(False)

class jeonnam(QMainWindow,jeonnam_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\전남1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\전남{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\전남{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)

class jeonbuk(QMainWindow,jeonbuk_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\전북1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\전북{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\전북{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)

class daejeon(QMainWindow,daejeon_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\대전1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\대전{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\대전{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)

class yesan(QMainWindow,yesan_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\예산1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\예산{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\예산{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)

class chungju(QMainWindow,chungju_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\충주1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\충주{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\충주{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)

class cheongju(QMainWindow,cheongju_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\청주1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\청주{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<2:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\청주{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==2:
        self.pushButton_2.setEnabled(False)

class taebaek(QMainWindow,taebeak_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\태백1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\태백{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\태백{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)

class chuncheon(QMainWindow,chuncheon_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\춘천1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\춘천{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\춘천{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)

class jeonju(QMainWindow,jeonju_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\전주1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\전주{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<2:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\전주{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==2:
        self.pushButton_2.setEnabled(False)

  
class uijeongbu(QMainWindow,uijeongbu_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\의정부1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\의정부{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\의정부{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)


class incheon(QMainWindow,incheon_class):
  def __init__(self):
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\인천1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)
      

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\인천{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<2:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\인천{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==2:
        self.pushButton_2.setEnabled(False)



class Gangnam(QMainWindow,gangnam_class):
  def __init__(self) :
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\강남1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\강남{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\강남{str(idx)}.png")
      self.image.scaledToWidth(300)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)


class Busanbookbu(QMainWindow,busanbookbu_class):
  def __init__(self):
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\부산북부1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\부산북부{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<2:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\부산북부{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==2:
        self.pushButton_2.setEnabled(False)


class Busannambu(QMainWindow,busannambu_class):
  def __init__(self):
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\부산남부1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\부산남부{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\부산남부{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)

class Yongin(QMainWindow,yongin_class):
  def __init__(self):
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\용인1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\용인{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\용인{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)


class Ansan(QMainWindow,ansan_class):
  def __init__(self):
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\안산1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)


  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\안산{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\안산{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)


class Dobong(QMainWindow,dobong_class):
  def __init__(self):
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\도봉1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\도봉{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\도봉{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)

class Gangseo(QMainWindow,gangseo_class):
  def __init__(self):
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\강서1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)


  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\강서{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\강서{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)


class Seobu(QMainWindow,seobu_class ):
  def __init__(self):
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))
    self.pushButton_2.clicked.connect(self.front_trans_image)
    self.pushButton.clicked.connect(self.back_trans_image)
    self.pushButton_3.clicked.connect(self.select_course)
    self.image=QPixmap()
    self.image.load(f".\\MAP\\서부1.png")
    self.image.scaledToWidth(300)
    self.label.setPixmap(self.image)
    self.label.repaint()
    self.pushButton.setEnabled(False)
      

  def select_course(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()
      global idx
      idx =1
    else:
      self.myWindow.close()
      self.myWindow=None

  def back_trans_image(self):
      global idx
      if idx>1:
        idx-=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\서부{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton_2.setEnabled(True)
      if idx==1:
        self.pushButton.setEnabled(False)

  def front_trans_image(self):#이미지 변환
      global idx
      if idx<4:
        idx+=1
      self.image=QPixmap()
      self.image.load(f".\\MAP\\서부{str(idx)}.png")
      self.image.scaledToWidth(1200)
      self.label.setPixmap(self.image)
      self.label.repaint()
      self.pushButton.setEnabled(True)
      if idx==4:
        self.pushButton_2.setEnabled(False)

class courseClass(QMainWindow, course_class):
  def __init__(self) :
      super().__init__()
      self.myWindow=None
      self.setupUi(self) 
      self.setWindowIcon(QIcon(".\\MAP\\car.png"))
      self.pushButton.clicked.connect(self.Beforepage)
      self.pushButton_2.clicked.connect(self.gangnampage)
      self.pushButton_3.clicked.connect(self.seobupage)
      self.pushButton_6.clicked.connect(self.uijeongbupage)
      self.pushButton_7.clicked.connect(self.gangseopage)
      self.pushButton_8.clicked.connect(self.ansanpage)
      self.pushButton_9.clicked.connect(self.yonginpage)
      self.pushButton_10.clicked.connect(self.busannambupage)
      self.pushButton_11.clicked.connect(self.busanbookbupage)
      self.pushButton_12.clicked.connect(self.incheonpage)
      self.pushButton_13.clicked.connect(self.jeonjupage)
      self.pushButton_14.clicked.connect(self.chuncheonpage)
      self.pushButton_15.clicked.connect(self.dobongpage)
      self.pushButton_16.clicked.connect(self.taebaekpage)
      self.pushButton_17.clicked.connect(self.cheongjupage)
      self.pushButton_18.clicked.connect(self.chungjupage)
      self.pushButton_19.clicked.connect(self.yesanpage)
      self.pushButton_20.clicked.connect(self.daejeonpage)
      self.pushButton_21.clicked.connect(self.jeonbukpage)
      self.pushButton_22.clicked.connect(self.jeonnampage)
      self.pushButton_23.clicked.connect(self.gwangyangpage)
      self.pushButton_24.clicked.connect(self.mungyeongpage)
      self.pushButton_25.clicked.connect(self.pohangpage)
      self.pushButton_26.clicked.connect(self.masanpage)
      self.pushButton_27.clicked.connect(self.ulsanpage)
      self.pushButton_28.clicked.connect(self.jejupage)
      self.pushButton_5.setEnabled(False)

  def jejupage(self):
    if self.myWindow is None:
      self.myWindow=jeju()
      self.myWindow.show()
      self.close()  

  def ulsanpage(self):
    if self.myWindow is None:
      self.myWindow=ulsan()
      self.myWindow.show()
      self.close()  
  def masanpage(self):
    if self.myWindow is None:
      self.myWindow=masan()
      self.myWindow.show()
      self.close()    

  def pohangpage(self):
    if self.myWindow is None:
      self.myWindow=pohang()
      self.myWindow.show()
      self.close()    

  def mungyeongpage(self):
    if self.myWindow is None:
      self.myWindow=mungyeong()
      self.myWindow.show()
      self.close()    

  def gwangyangpage(self):
    if self.myWindow is None:
      self.myWindow=gwangyang()
      self.myWindow.show()
      self.close()    

  def jeonnampage(self):
    if self.myWindow is None:
      self.myWindow=jeonnam()
      self.myWindow.show()
      self.close()

  def jeonbukpage(self):
    if self.myWindow is None:
      self.myWindow=jeonbuk()
      self.myWindow.show()
      self.close()

  def daejeonpage(self):
    if self.myWindow is None:
      self.myWindow=daejeon()
      self.myWindow.show()
      self.close()
  
  def yesanpage(self):
    if self.myWindow is None:
      self.myWindow=yesan()
      self.myWindow.show()
      self.close()

  def chungjupage(self):
    if self.myWindow is None:
      self.myWindow=chungju()
      self.myWindow.show()
      self.close()

  def cheongjupage(self):
    if self.myWindow is None:
      self.myWindow=cheongju()
      self.myWindow.show()
      self.close()

  def taebaekpage(self):
    if self.myWindow is None:
      self.myWindow=taebaek()
      self.myWindow.show()
      self.close()

  def chuncheonpage(self):
    if self.myWindow is None:
      self.myWindow=chuncheon()
      self.myWindow.show()
      self.close()

  def jeonjupage(self):
    if self.myWindow is None:
      self.myWindow=jeonju()
      self.myWindow.show()
      self.close()

  def uijeongbupage(self):
     if self.myWindow is None:
      self.myWindow=uijeongbu()
      self.myWindow.show()
      self.close()

  def incheonpage(self):
     if self.myWindow is None:
      self.myWindow=incheon()
      self.myWindow.show()
      self.close()

  def busanbookbupage(self): 
    if self.myWindow is None:
      self.myWindow=Busanbookbu()
      self.myWindow.show()
      self.close()

  def busannambupage(self):
    if self.myWindow is None:
      self.myWindow=Busannambu()
      self.myWindow.show()
      self.close()

  def yonginpage(self):
    if self.myWindow is None:
      self.myWindow=Yongin()
      self.myWindow.show()
      self.close()
    
    else:
      self.myWindow.close()
      self.myWindow=None

  def ansanpage(self):
    if self.myWindow is None:
      self.myWindow=Ansan()
      self.myWindow.show()
      self.close()
    
    else:
      self.myWindow.close()
      self.myWindow=None


  def dobongpage(self):
    if self.myWindow is None:
      self.myWindow=Dobong()
      self.myWindow.show()
      self.close()
    
    else:
      self.myWindow.close()
      self.myWindow=None

  def gangnampage(self):#이전버튼 누르면 초기화면으로 돌아감
    if self.myWindow is None:
      self.myWindow=Gangnam()
      self.myWindow.show()
      self.close()

    else:
      self.myWindow.close()
      self.myWindow=None
  
  def gangseopage(self):
    if self.myWindow is None:
      self.myWindow=Gangseo()
      self.myWindow.show()
      self.close()
    
    else:
      self.myWindow.close()
      self.myWindow=None

  def seobupage(self):
    if self.myWindow is None:
      self.myWindow=Seobu()
      self.myWindow.show()
      self.close()
    
    else:
      self.myWindow.close()
      self.myWindow=None

  
  def Beforepage(self):#이전버튼 누르면 초기화면으로 돌아감
    if self.myWindow is None:
      self.myWindow=MainWindow()
      self.myWindow.show()
      self.close()

    else:
      self.myWindow.close()
      self.myWindow=None



class Node:
  def __init__(self,val):
    self.val=val
    self.child=[]

class Heap:
  def __init__(self):
    self.data=[]

  
  def insert(self,item):
    self.data.append(item)

    idx=len(self.data)-1

    while idx!=1:
      numOfParentNode=idx//2

      if self.data[numOfParentNode][2]>self.data[idx][2]:
        self.data[numOfParentNode],self.data[idx]= self.data[idx], self.data[numOfParentNode]
        idx=numOfParentNode
      else:
        break

  def remove(self):
    if len(self.data)>1:
      self.data[1],self.data[-1]=self.data[-1],self.data[1]
      data=self.data.pop(-1)
      self.minHeapify(1)
    else:
      data=None
    return data

  def minHeapify(self, i):
    left=i*2
    right=i*2+1
    greatest=i

    if left<len(self.data) and self.data[left][2]<self.data[greatest][2]:
      greatest=left
    if right<len(self.data) and self.data[right][2]<self.data[greatest][2]:
      greatest=right
    if greatest!=i:
      self.data[i],self.data[greatest]=self.data[greatest],self.data[i]

      self.minHeapify(greatest) 


class WindowClass(QMainWindow, form_class) :
  def __init__(self) :#INIT
      super().__init__()
      self.myWindow=None
      self.setupUi(self) 
      self.btn_3.clicked.connect(self.texteditFunction)
      self.btn_3.clicked.connect(self.lineclear)
      self.setWindowIcon(QIcon(".\\MAP\\car.png"))
       #정답 버튼 누를 경우
      global idx
      self.btn_1.setEnabled(True)
      if idx!=len(answer):
        self.btn_1.setEnabled(False)
      self.btn_2.clicked.connect(self.btrans_image)
      self.btn_1.clicked.connect(self.ftrans_image)
      self.btn_4.setEnabled(False)
      self.btn_5.setEnabled(False)
      self.btn_6.hide()
      self.btn_6.clicked.connect(self.Beforepage)
      self.btn_4.clicked.connect(self.Scoring)
      self.label02.hide()
      self.ans_text.hide()
      self.btn_7.hide()
      self.image=QPixmap()
      self.image.load(f".\\picture\\{str(problem[idx][0])}.png")
      self.image.scaledToWidth(300)
      self.pict01.setPixmap(self.image)
      self.pict01.repaint()
      validator=QIntValidator(1,4,self)
      self.lineEdit.setValidator(validator)
      self.label03.setText(f"{idx}번  정답률:{problem[idx][2]}%")

  

   

    # 정답버튼 클릭 시 line 답 answer 배열에 넣기 
  def texteditFunction(self): #정답 입력창 함수
      if len(self.lineEdit.text())==0:
        QMessageBox.about(self,"메시지","숫자를 입력해 주세요!")
      elif int(self.lineEdit.text())>4 or int(self.lineEdit.text())==0:
        QMessageBox.about(self,"메시지","숫자를 다시 입력해 주세요!")
      else:  # 1~4 입력시 다음화면 and answer배열에 넣음
        data = int(self.lineEdit.text())
        if idx>=len(answer) and len(problem)!=2: #순서대로 푼경우
          self.ftrans_image()
          answer.append(data)
          print(answer)
        elif len(problem)==2:
          self.ftrans_image()
          answer.append(0)
          answer.append(data)
          print(answer)
        else: # 지나간 문제 다시 풀경우
          self.ftrans_image()
          answer[idx-1]=data
          print(answer)
  
  def Beforepage(self):# 이전버튼 누르면 초기화면으로 돌아감
    global idx
    idx=1
    if self.myWindow is None:
      self.myWindow=MainWindow()
      self.myWindow.show()
      self.close()
      problem.clear()
      problem.append([0,0,100])
      answer.clear()
      w_answer.clear()
      w_answer_idx.clear()
      w_n.clear()
    
    else:
      self.myWindow.close()
      self.myWindow=None

  def first_image(self):# 다시 풀기 할 경우 
      global idx
      self.label03.show()
      self.label03.setText(f"{idx}번  정답률:{problem[idx][2]}%")  
      self.btn_1.setEnabled(True)
      if idx>=len(answer):
        self.btn_1.setEnabled(False)
      self.btn_2.setEnabled(True)
      self.btn_3.setEnabled(True)
      self.btn_5.setEnabled(False)
      if len(problem)==2:
        self.image=QPixmap()
        self.image.load(f".\\picture\\{str(problem[idx][0])}.png")
        self.image.scaledToWidth(300)
        self.pict01.setPixmap(self.image)
        self.pict01.repaint()
        self.btn_4.setEnabled(True)

      else:
        if problem[idx][0]!=problem[-1][0]:
          self.image=QPixmap()
          self.image.load(f".\\picture\\{str(problem[idx][0])}.png")
          self.image.scaledToWidth(300)
          self.pict01.setPixmap(self.image)
          self.pict01.repaint()
          if self.btn_1.clicked and idx>len(answer)+1:
            answer.append(0)
          if problem[idx][0]==problem[-1][0]:
            self.btn_4.setEnabled(True)
          elif problem[idx][0]!=problem[-1][0]:
            self.btn_4.setEnabled(False)
        else:
          QMessageBox.about(self,"메시지","마지막 문제입니다!")
        

  def ftrans_image(self):# 입력or다음 누를때 다음화면 넘어가기
      global idx
      self.btn_2.setEnabled(True)
      self.btn_3.setEnabled(True)
      self.btn_5.setEnabled(False)
      self.btn_1.setEnabled(True)
       #여기까지는 idx값이 1이네 #2에서

      if problem[idx][0]!=problem[-1][0]:
        idx+=1
        self.label03.setText(f"{idx}번  정답률:{problem[idx][2]}%")
        if idx>=len(answer):
          self.btn_1.setEnabled(False)
        self.image=QPixmap()
        self.image.load(f".\\picture\\{str(problem[idx][0])}.png") #다음눌렀을때 2값 #3값
        self.image.scaledToWidth(300)
        self.pict01.setPixmap(self.image)
        self.pict01.repaint()
        if self.btn_1.clicked and idx>len(answer)+1:
          answer.append(0)
        if problem[idx][0]==problem[-1][0]:
          self.btn_4.setEnabled(True)
        elif problem[idx][0]!=problem[-1][0]:
          self.btn_4.setEnabled(False)
      else:
        QMessageBox.about(self,"메시지","마지막 문제입니다!")


    
   
  
  def btrans_image(self):# 이전 페이지
      global idx
      idx-=1
      self.label03.setText(f"{idx}번  정답률:{problem[idx][2]}%")
      self.btn_1.setEnabled(True)
      if idx>len(answer):
        self.btn_1.setEnabled(False) #이전 누르면 1이된다
      if idx>0:
        self.image=QPixmap()
        self.image.load(f".\\picture\\{str(problem[idx][0])}.png")
        self.image.scaledToWidth(300)
        self.pict01.setPixmap(self.image)
        self.pict01.repaint()
      else:
        self.Beforepage()
      if idx==len(problem):
        self.btn_4.setEnabled(True)
      elif idx!=len(problem):
        self.btn_4.setEnabled(False)

  def lineclear(self): # 입력창초기화
    self.lineEdit.clear()    
  

  def Scoring(self):  #채점하기
    H=Heap()
    self.label03.hide()
    global problem
    global idx
    self.label02.show()
    self.ans_text.show()
    self.pict01.hide()
    self.btn_5.setEnabled(True)
    self.btn_7.show()
    self.btn_7.setEnabled(True)
    self.btn_7.clicked.connect(self.Print_ans)
      

    for i in range(len(answer)): #틀린 문항 넣기
      if problem[i][1]!=answer[i]:
        w_answer.append(problem[i])
        w_answer_idx.append(i)
        w_answer_2.append(str(problem[i][1]))
    

      
    #print(f"w_answer={w_answer}")
    
  

    if len(w_answer)==0 : # 다 맞은 경우
      self.label02.setText("다 맞았습니다!")
      self.label02.repaint()
      self.ans_text.hide()
      self.btn_7.setEnabled(False)
      self.btn_1.setEnabled(False)
      self.btn_2.setEnabled(False)
      self.btn_3.setEnabled(False)
      self.btn_4.setEnabled(False)
      self.btn_5.setEnabled(False)
      self.btn_6.show()
      problem.clear()
      problem=[[0,0,100]]
      Sorted.clear()
      w_answer.clear()
      w_answer_idx.clear()
      answer.clear()
      w_n.clear()
      idx=1

    
    else: #w_answer => Heap에 넣기
      H.insert([100,100,100])
      for i in range(len(w_answer)):
        H.insert(w_answer[i])
      
      
      
      for i in range(len(w_answer)):
        d=H.remove()
        Sorted.append(d)
      



      self.label02.setText("한 번 더 풀어봐야 할 문제")
      self.label02.repaint()
    
      for i in range(len(w_answer_idx)):
        w_n.append(str(w_answer_idx[i])+'번')
        self.ans_text.setText(",  ".join(w_n))
    
      self.btn_4.setEnabled(False)
      self.btn_1.setEnabled(False)
      self.btn_2.setEnabled(False)
      self.btn_3.setEnabled(False)
      problem.clear()
      problem=[[0,0,100]]
      problem.extend(Sorted)
      print(problem)
      Sorted.clear()
      w_answer.clear()
      w_answer_idx.clear()
      answer.clear()
      w_n.clear()
      idx=1
      self.btn_5.clicked.connect(self.first_image)
      self.btn_5.clicked.connect(self.pict01.show)
      self.btn_5.clicked.connect(self.ans_text.hide)
      self.btn_5.clicked.connect(self.label02.hide)
      self.btn_5.clicked.connect(self.btn_7.hide)
      self.btn_5.clicked.connect(self.Init_answer)
  
  def Print_ans(self): #채점간 정답 출력
    QMessageBox.about(self,"정답","정답 : "+",  ".join(w_answer_2))
  
  def Init_answer(self):
    w_answer_2.clear()

    

  

class MainWindow(QMainWindow,first_class):
  
  def __init__(self) : #INIT
    super().__init__()
    self.myWindow=None
    self.setupUi(self)
    self.Pbtn_1.hide()
    self.Pbtn_2.hide()
    self.Pbtn_3.hide()
    self.btn_3.hide()
    self.Dbtn_1.hide()
    self.Dbtn_2.hide()
    self.Dbtn_3.hide()
    self.Dbtn_3.hide()
    self.Dbtn_4.hide()
    self.setWindowIcon(QIcon(".\\MAP\\car.png"))  
    self.btn_1.clicked.connect(self.Make_data)
    self.btn_1.clicked.connect(self.Nextpage)
    self.label_3.hide()
    self.btn_2.clicked.connect(self.Open_original)
    self.btn_2.clicked.connect(self.Make_problem)
    self.btn_4.clicked.connect(self.CoursePage)
    self.btn_5.clicked.connect(self.Nextpage_media)
    



  def Open_original(self):
    self.btn_1.hide()
    self.btn_2.hide()
    self.label.hide()
    self.btn_4.hide()
    self.btn_5.hide()
    self.Pbtn_1.show()
    self.Pbtn_2.show()
    self.Pbtn_3.show()
    self.btn_3.show()
    self.label_3.show()
    self.btn_3.clicked.connect(self.first_Page)
    self.Pbtn_1.clicked.connect(self.difficulty_1)
    self.Pbtn_2.clicked.connect(self.difficulty_2)
    self.Pbtn_3.clicked.connect(self.difficulty_3)

  def difficulty_1(self):
    self.Pbtn_2.setEnabled(False)
    self.Pbtn_3.setEnabled(False)
    self.Dbtn_1.show()
    self.Dbtn_2.show()
    self.Dbtn_3.show()
    self.Dbtn_4.show()
    self.Dbtn_1.clicked.connect(lambda: self.start_problem(0,3))
    self.Dbtn_2.clicked.connect(lambda: self.start_problem(0,2))
    self.Dbtn_3.clicked.connect(lambda: self.start_problem(0,1))
    self.Dbtn_4.clicked.connect(lambda: self.start_problem(0,0))
    self.Dbtn_1.clicked.connect(self.Nextpage)
    self.Dbtn_2.clicked.connect(self.Nextpage)
    self.Dbtn_3.clicked.connect(self.Nextpage)
    self.Dbtn_4.clicked.connect(self.Nextpage)

  def difficulty_2(self):
    self.Pbtn_1.setEnabled(False)
    self.Pbtn_3.setEnabled(False)
    self.Dbtn_1.show()
    self.Dbtn_2.show()
    self.Dbtn_3.show()
    self.Dbtn_4.show()
    self.Dbtn_1.clicked.connect(lambda: self.start_problem(1,3))
    self.Dbtn_2.clicked.connect(lambda: self.start_problem(1,2))
    self.Dbtn_3.clicked.connect(lambda: self.start_problem(1,1))
    self.Dbtn_4.clicked.connect(self.Update)
    self.Dbtn_1.clicked.connect(self.Nextpage)
    self.Dbtn_2.clicked.connect(self.Nextpage)
    self.Dbtn_3.clicked.connect(self.Nextpage)
    #self.Dbtn_4.clicked.connect(self.Nextpage)

  def difficulty_3(self):
    self.Pbtn_1.setEnabled(False)
    self.Pbtn_2.setEnabled(False)
    #self.Pbtn_3.setEnabled(False)
    self.Dbtn_1.show()
    self.Dbtn_2.show()
    self.Dbtn_3.show()
    self.Dbtn_4.show()
    self.Dbtn_1.clicked.connect(lambda: self.start_problem(2,3))
    self.Dbtn_2.clicked.connect(lambda: self.start_problem(2,2))
    self.Dbtn_3.clicked.connect(lambda: self.start_problem(2,1))
    self.Dbtn_4.clicked.connect(self.Update)
    self.Dbtn_1.clicked.connect(self.Nextpage)
    self.Dbtn_2.clicked.connect(self.Nextpage)
    self.Dbtn_3.clicked.connect(self.Nextpage)
    #self.Dbtn_4.clicked.connect(self.Nextpage)
    

  def first_Page(self): 
    self.Pbtn_1.hide()
    self.Pbtn_2.hide()
    self.Pbtn_3.hide()
    self.btn_3.hide()
    self.btn_1.show()
    self.btn_2.show()
    self.btn_4.show()
    self.btn_5.show()
    self.label_3.hide
    self.label.show()
    self.Dbtn_1.hide()
    self.Dbtn_2.hide()
    self.Dbtn_3.hide()
    self.Dbtn_4.hide()
    self.label_3.hide()
    self.Pbtn_1.setEnabled(True)
    self.Pbtn_2.setEnabled(True)
    self.Pbtn_3.setEnabled(True)

  def Update(self):
    QMessageBox.about(self,"메시지","문제가 없습니다?")
     

  def start_problem(self,_i,_j):
    
    for k in range(len(root.child[_i].child[_j].child)):
      problem.append(root.child[_i].child[_j].child[k].val)
    print(problem)

  def Make_problem(self):
    
    problem.clear()
    problem.append([0,0,100])
    global root

    root=Node(0)
    
    # 유형별 4단계 생성(1단계:동영상형 | 2단계:표지판형 | 3단계:문장형)
    for i in range(4):
        root.child.append(Node(i + 1))

    # 정답률 4단계 생성(1단계:0~30(30) | 2단계:30~59(30) | 3단계:60~79(20)
    for i in range(4):
        for j in range(4):
            root.child[i].child.append(Node(j + 1))

    # 유형별 문제 은행 데이터 저장
    for p in range(len(original)):
        if 1 <= original[p][0] < 32:  # 유형별 1단계
            if 0 <= original[p][2] < 30:  # 정답률 1단계
                root.child[0].child[0].child.append(Node(original[p]))
            elif 30 <= original[p][2] < 60:  # 정답률 2단계
                root.child[0].child[1].child.append(Node(original[p]))
            elif 60 <= original[p][2] < 79:  # 정답률 3단계
                root.child[0].child[2].child.append(Node(original[p]))
            else:  # 정답률 4단계
                root.child[0].child[3].child.append(Node(original[p]))

        if 32 <= original[p][0] < 72:  # 유형별 2단계
            if 0 <= original[p][2] < 30:  # 정답률 1단계
                root.child[1].child[0].child.append(Node(original[p]))
            elif 30 <= original[p][2] < 60:  # 정답률 2단계
                root.child[1].child[1].child.append(Node(original[p]))
            elif 60 <= original[p][2] < 79:  # 정답률 3단계
                root.child[1].child[2].child.append(Node(original[p]))
            else:  # 정답률 4단계
                root.child[1].child[3].child.append(Node(original[p]))

        if 72 <= original[p][0] < 112:  # 유형별 3단계
            if 0 <= original[p][2] < 30:  # 정답률 1단계
                root.child[2].child[0].child.append(Node(original[p]))
            elif 30 <= original[p][2] < 60:  # 정답률 2단계
                root.child[2].child[1].child.append(Node(original[p]))
            elif 60 <= original[p][2] < 79:  # 정답률 3단계
                root.child[2].child[2].child.append(Node(original[p]))
            else:  # 정답률 4단계
                root.child[2].child[3].child.append(Node(original[p]))

        if 112 <= original[p][0] <= 160:  # 유형별 4단계
            if 0 <= original[p][2] < 30:  # 정답률 1단계
                root.child[3].child[0].child.append(Node(original[p]))
            elif 30 <= original[p][2] < 60:  # 정답률 2단계
                root.child[3].child[1].child.append(Node(original[p]))
            elif 60 <= original[p][2] < 79:  # 정답률 3단계
                root.child[3].child[2].child.append(Node(original[p]))
            else:  # 정답률 4단계
                root.child[3].child[3].child.append(Node(original[p]))

     
    #for i in range(4):
      #for j in range(4):
        #for k in range(len(root.child[i].child[j].child)):
          #print(f"({i},{j},{k}) {root.child[i].child[j].child[k].val})")

    
  def Make_data(self): #모의고사 40제 problem append
    problem.clear()
    problem.append([0,0,100])
    rand=[random.randrange(0,111) for r in range(10)]
    for r in rand:
      problem.append(original[r])
    print(problem)

  def CoursePage(self):
    if self.myWindow is None:
      self.myWindow=courseClass()
      self.myWindow.show()
      self.close()

    else:
      self.myWindow.close()
      self.myWindow=None
      

  def Nextpage(self): #모의고사 40제 UI로 넘어가기
    if self.myWindow is None:
      self.myWindow=WindowClass()
      self.myWindow.show()
      self.close()
    
    else:
      self.myWindow.close()
      self.myWindow=None

  def Nextpage_media(self):
    if self.myWindow is None:
      self.myWindow=VideoPlayer()
      self.myWindow.resize(640, 480)
      self.myWindow.show()
      self.close()
      
    
    else:
      self.myWindow.close()
      self.myWindow=None

 
class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("시뮬레이션")
        self.myWindow=None
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.setWindowIcon(QIcon(".\\MAP\\car.png"))
 
        videoWidget = QVideoWidget()
        self.btn_1=QPushButton("뒤로가기")
        self.btn_1.setToolTip("선택")
        self.btn_1.setStatusTip("선택")
        self.btn_1.setFixedSize(100, 24)
        self.btn_1.setStyleSheet("QPushButton::enabled"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: white;"
                                  "background-color: rgb(58, 134, 255);"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: rgb(58, 134, 255);"
                                  "background-color: white;"
                                  "text-align: center;"
                                  "}"
                                  )

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
 
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
 
        self.error = QLabel()
        self.error.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

 
        self.openButton1 = QPushButton("1. 장치조작")  
        self.openButton1.setToolTip("선택")
        self.openButton1.setStatusTip("선택")
        self.openButton1.setFixedSize(100, 24)
        self.openButton1.setStyleSheet(
                                  "QPushButton::enabled"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: white;"
                                  "background-color: rgb(58, 134, 255);"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: rgb(58, 134, 255);"
                                  "background-color: white;"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::disabled"
                                  "{"
                                  "font: 10 DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(0, 85, 197);"
                                  "color: white;"
                                  "background-color: rgb(0, 85, 197);"
                                  "text-align: center;"
                                  "}")
                             
     
        self.openButton1.clicked.connect(self.openFile1)

        self.openButton2 = QPushButton("2. 차로준수")   
        self.openButton2.setToolTip("선택")
        self.openButton2.setStatusTip("선택")
        self.openButton2.setFixedSize(100, 24)
        self.openButton2.setStyleSheet("QPushButton::enabled"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: white;"
                                  "background-color: rgb(58, 134, 255);"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: rgb(58, 134, 255);"
                                  "background-color: white;"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::disabled"
                                  "{"
                                  "font: 10 DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(0, 85, 197);"
                                  "color: white;"
                                  "background-color: rgb(0, 85, 197);"
                                  "text-align: center;"
                                  "}")
        self.openButton2.clicked.connect(self.openFile2)


        self.openButton3 = QPushButton("3. 경사로")   
        self.openButton3.setToolTip("선택")
        self.openButton3.setStatusTip("선택")
        self.openButton3.setFixedSize(100, 24)
        self.openButton3.setStyleSheet("QPushButton::enabled"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: white;"
                                  "background-color: rgb(58, 134, 255);"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: rgb(58, 134, 255);"
                                  "background-color: white;"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::disabled"
                                  "{"
                                  "font: 10 DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(0, 85, 197);"
                                  "color: white;"
                                  "background-color: rgb(0, 85, 197);"
                                  "text-align: center;"
                                  "}")
        self.openButton3.clicked.connect(self.openFile3)

        self.openButton4 = QPushButton("4. 회전코스")   
        self.openButton4.setToolTip("선택")
        self.openButton4.setStatusTip("선택")
        self.openButton4.setFixedSize(100, 24)
        self.openButton4.setStyleSheet("QPushButton::enabled"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: white;"
                                  "background-color: rgb(58, 134, 255);"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: rgb(58, 134, 255);"
                                  "background-color: white;"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::disabled"
                                  "{"
                                  "font: 10 DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(0, 85, 197);"
                                  "color: white;"
                                  "background-color: rgb(0, 85, 197);"
                                  "text-align: center;"
                                  "}")
        self.openButton4.clicked.connect(self.openFile4)

        self.openButton5 = QPushButton("5. 교차로")   
        self.openButton5.setToolTip("선택")
        self.openButton5.setStatusTip("선택")
        self.openButton5.setFixedSize(100, 24)
        self.openButton5.setStyleSheet("QPushButton::enabled"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: white;"
                                  "background-color: rgb(58, 134, 255);"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: rgb(58, 134, 255);"
                                  "background-color: white;"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::disabled"
                                  "{"
                                  "font: 10 DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(0, 85, 197);"
                                  "color: white;"
                                  "background-color: rgb(0, 85, 197);"
                                  "text-align: center;"
                                  "}")
        self.openButton5.clicked.connect(self.openFile5)

        self.openButton6 = QPushButton("6. 직각주차")   
        self.openButton6.setToolTip("선택")
        self.openButton6.setStatusTip("선택")
        self.openButton6.setFixedSize(100, 24)
        self.openButton6.setStyleSheet("QPushButton::enabled"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: white;"
                                  "background-color: rgb(58, 134, 255);"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: rgb(58, 134, 255);"
                                  "background-color: white;"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::disabled"
                                  "{"
                                  "font: 10 DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(0, 85, 197);"
                                  "color: white;"
                                  "background-color: rgb(0, 85, 197);"
                                  "text-align: center;"
                                  "}")
        self.openButton6.clicked.connect(self.openFile6)

        self.openButton7 = QPushButton("7. 돌발상황")   
        self.openButton7.setToolTip("선택")
        self.openButton7.setStatusTip("선택")
        self.openButton7.setFixedSize(100, 24)
        self.openButton7.setStyleSheet("QPushButton::enabled"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: white;"
                                  "background-color: rgb(58, 134, 255);"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: rgb(58, 134, 255);"
                                  "background-color: white;"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::disabled"
                                  "{"
                                  "font: 10 DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(0, 85, 197);"
                                  "color: white;"
                                  "background-color: rgb(0, 85, 197);"
                                  "text-align: center;"
                                  "}")
        self.openButton7.clicked.connect(self.openFile7)


        self.openButton8 = QPushButton("8. 가속코스")   
        self.openButton8.setToolTip("선택")
        self.openButton8.setStatusTip("선택")
        self.openButton8.setFixedSize(100, 24)
        self.openButton8.setStyleSheet("QPushButton::enabled"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: white;"
                                  "background-color: rgb(58, 134, 255);"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "font: 10pt DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(58, 134, 255);"
                                  "color: rgb(58, 134, 255);"
                                  "background-color: white;"
                                  "text-align: center;"
                                  "}"
                                  "QPushButton::disabled"
                                  "{"
                                  "font: 10 DX방탄고딕;"
                                  "border-radius: 5px;"
                                  "border: 2px solid rgb(0, 85, 197);"
                                  "color: white;"
                                  "background-color: rgb(0, 85, 197);"
                                  "text-align: center;"
                                  "}")
        self.openButton8.clicked.connect(self.openFile8)
        self.btn_1.clicked.connect(self.back_page)
 
        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)
 
        # Create layouts to place inside widget
        backLayout = QHBoxLayout()
        backLayout.addWidget(self.btn_1,alignment=Qt.AlignLeft)
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        menuLayout = QHBoxLayout()
        menuLayout.addWidget(self.openButton1)
        menuLayout.addWidget(self.openButton2)
        menuLayout.addWidget(self.openButton3)
        menuLayout.addWidget(self.openButton4)
        menuLayout.addWidget(self.openButton5)
        menuLayout.addWidget(self.openButton6)
        menuLayout.addWidget(self.openButton7)
        menuLayout.addWidget(self.openButton8)

        layout = QVBoxLayout()
        layout.addLayout(backLayout)
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addLayout(menuLayout)
        # layout.addWidget(self.error)

        
        # Set widget to contain window contents
        wid.setLayout(layout)
 
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
   
    def back_page(self):
      # 이전버튼 누르면 초기화면으로 돌아감
        if self.myWindow is None:
          self.mediaPlayer.pause()
          self.myWindow=MainWindow()
          self.myWindow.show()
          self.close()
        else:
          self.myWindow.close()
          self.myWindow=None
  
    def openFile1(self):
        self.openButton1.setEnabled(False)
        self.openButton2.setEnabled(True)
        self.openButton3.setEnabled(True)
        self.openButton4.setEnabled(True)
        self.openButton5.setEnabled(True)
        self.openButton6.setEnabled(True)
        self.openButton7.setEnabled(True)
        self.openButton8.setEnabled(True)
        fileName = ".\\Video\\장치조작.mp4"
        self.play()
        
 
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
    
    def openFile2(self):
        self.openButton1.setEnabled(True)
        self.openButton2.setEnabled(False)
        self.openButton3.setEnabled(True)
        self.openButton4.setEnabled(True)
        self.openButton5.setEnabled(True)
        self.openButton6.setEnabled(True)
        self.openButton7.setEnabled(True)
        self.openButton8.setEnabled(True)
        fileName = ".\\Video\\차로준수.mp4"
        self.play()
 
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def openFile3(self):
        self.openButton1.setEnabled(True)
        self.openButton2.setEnabled(True)
        self.openButton3.setEnabled(False)
        self.openButton4.setEnabled(True)
        self.openButton5.setEnabled(True)
        self.openButton6.setEnabled(True)
        self.openButton7.setEnabled(True)
        self.openButton8.setEnabled(True)
        fileName = ".\\Video\\경사로.mp4"
        self.play()
 
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def openFile4(self):
        self.openButton1.setEnabled(True)
        self.openButton2.setEnabled(True)
        self.openButton3.setEnabled(True)
        self.openButton4.setEnabled(False)
        self.openButton5.setEnabled(True)
        self.openButton6.setEnabled(True)
        self.openButton7.setEnabled(True)
        self.openButton8.setEnabled(True)
        fileName = ".\\Video\\회전코스.mp4"
        self.play()
 
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def openFile5(self):
        self.openButton1.setEnabled(True)
        self.openButton2.setEnabled(True)
        self.openButton3.setEnabled(True)
        self.openButton4.setEnabled(True)
        self.openButton5.setEnabled(False)
        self.openButton6.setEnabled(True)
        self.openButton7.setEnabled(True)
        self.openButton8.setEnabled(True)
        fileName = ".\\Video\\교차로.mp4"
        self.play()
 
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def openFile6(self):
        self.openButton1.setEnabled(True)
        self.openButton2.setEnabled(True)
        self.openButton3.setEnabled(True)
        self.openButton4.setEnabled(True)
        self.openButton5.setEnabled(True)
        self.openButton6.setEnabled(False)
        self.openButton7.setEnabled(True)
        self.openButton8.setEnabled(True)
        fileName = ".\\Video\\직각주차.mp4"
        self.play()
 
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def openFile7(self):
        self.openButton1.setEnabled(True)
        self.openButton2.setEnabled(True)
        self.openButton3.setEnabled(True)
        self.openButton4.setEnabled(True)
        self.openButton5.setEnabled(True)
        self.openButton6.setEnabled(True)
        self.openButton7.setEnabled(False)
        self.openButton8.setEnabled(True)
        fileName = ".\\Video\\돌발상황.mp4"
        self.play()
 
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def openFile8(self):
        self.openButton1.setEnabled(True)
        self.openButton2.setEnabled(True)
        self.openButton3.setEnabled(True)
        self.openButton4.setEnabled(True)
        self.openButton5.setEnabled(True)
        self.openButton6.setEnabled(True)
        self.openButton7.setEnabled(True)
        self.openButton8.setEnabled(False)
        fileName = ".\\Video\\가속구간.mp4"
        self.play()
 
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
 
    def exitCall(self):
        sys.exit(app.exec_())
 
    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
 
    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))
 
    def positionChanged(self, position):
        self.positionSlider.setValue(position)
 
    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)
 
    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
 
    def handleError(self):
        self.playButton.setEnabled(False)
        self.error.setText("Error: " + self.mediaPlayer.errorString())



if __name__ == "__main__" :
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    # WindowClass의 인스턴스 생성
    myWindow = MainWindow() 

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
