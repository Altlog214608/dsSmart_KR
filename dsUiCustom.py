from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt, QObject, QEvent

# PYSIDE_DESIGNER_PLUGINS
from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection

class scentSlider(QSlider):
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            e.accept()
            x = e.pos().x()
            value = (self.maximum() - self.minimum()) * x / self.width() + self.minimum()
            self.setValue(value)
        else:
            return super().mousePressEvent(self, e)

# Custome StyleSheets
# Progress bar
pb_blue_style = "QProgressBar {\
	                border: 2px solid rgba(77, 127, 243, 180);\
	                border-radius: 5px;\
	                text-align: center;\
	                background-color: rgba(77, 127, 243, 180);\
	                color: black;\
                }\
                QProgressBar::chunk {\
                    background-color: #AAD7DD;\
                }"
pb_red_style = "QProgressBar {\
	                border: 2px solid rgba(176, 91, 161, 180);\
	                border-radius: 5px;\
	                text-align: center;\
	                background-color: rgba(176, 91, 161, 180);\
	                color: black;\
                }\
                QProgressBar::chunk {\
                    background-color: #EB88DA;\
                }"

class Filter_ReturnTabSpaceNumber(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress: # and obj is self.text_box:
            key = event.key()
            if key == Qt.Key.Key_Return: # and self.text_box.hasFocus():
                return True
                # print('Enter pressed')
            elif key == Qt.Key.Key_Tab:
                return True
                # print('Tab pressed')
            elif key == Qt.Key.Key_Space:
                return True
            elif Qt.Key.Key_0 <= key <= Qt.Key.Key_9:
                return True
        return super().eventFilter(obj, event)

class Filter_ReturnTabSpace(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress: # and obj is self.text_box:
            key = event.key()
            if key == Qt.Key.Key_Return: # and self.text_box.hasFocus():
                return True
                # print('Enter pressed')
            elif key == Qt.Key.Key_Tab:
                return True
                # print('Tab pressed')
            elif key == Qt.Key.Key_Space:
                return True
        return super().eventFilter(obj, event)
    
class Filter_TabSpace(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress: # and obj is self.text_box:
            key = event.key()
            if key == Qt.Key.Key_Tab:
                return True
                # print('Tab pressed')
            elif key == Qt.Key.Key_Space:
                return True
        return super().eventFilter(obj, event)
    
# class Filter_InputNumber(QObject):
#     def eventFilter(self, obj, event):
#         if event.type() == QEvent.Type.KeyPress: # and obj is self.text_box:
#             key = event.key()
#             if key <= Qt.Key.Key_0 or key >= Qt.Key.Key_9:
#                 text = obj.toPlainText()
#                 if text and not text.isdigit():
#                     return False
#                 if text:
#                     num = int(text)
#                     if num < 0 or num > 100:
#                         return True
#                 return True
#         return super().eventFilter(obj, event)


class Filter_InputNumber(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyRelease:
            text = obj.toPlainText()
            # 비어 있으면 그냥 통과
            if not text:
                return False
            # 숫자인지 확인
            if not text.isdigit():
                # 숫자가 아니면 제거 (숫자만 입력되게)
                cleaned = ''.join(filter(str.isdigit, text))
                obj.setPlainText(cleaned)
                self.move_cursor_to_end(obj)
                return False
            # 숫자로 변환해서 범위 검사
            number = int(text)
            if number < 0 or number > 100:
                print("❌ 범위 밖 숫자! 입력 차단")
                obj.setPlainText("")  # 또는 이전 상태 기억해서 복구도 가능
                self.move_cursor_to_end(obj)
        return False