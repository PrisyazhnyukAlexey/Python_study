import cv2
print(cv2)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QGraphicsTextItem

# Загрузка изображения
image = cv2.imread('office_map.jpg')

# Создание графической сцены
scene = QGraphicsScene()

# Создание и добавление графического элемента изображения на сцену
height, width, channel = image.shape
bytesPerLine = 3 * width
qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
pixmap = QPixmap.fromImage(qImg)
pixmap_item = QGraphicsPixmapItem(pixmap)
scene.addItem(pixmap_item)

# Добавление меток на изображение
labels = [
    {'name': 'Иванов Иван Иванович', 'position': (100, 50)},
    {'name': 'Петров Петр Петрович', 'position': (200, 150)},
    {'name': 'Сидоров Сидор Сидорович', 'position': (300, 250)},
]

for label in labels:
    # Создание и добавление текстовой метки на сцену
    text_item = QGraphicsTextItem(label['name'])
    text_item.setPos(label['position'][0], label['position'][1])
    scene.addItem(text_item)

# Создание и настройка графического виджета
view = QGraphicsView(scene)
view.setRenderHint(QPainter.Antialiasing)
view.setDragMode(QGraphicsView.ScrollHandDrag)
view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
view.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
view.setDragMode(QGraphicsView.ScrollHandDrag)

# Отображение графического виджета
app = QApplication([])
view.show()
app.exec_()