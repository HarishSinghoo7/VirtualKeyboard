import cv2

keys = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '?']]

class Button:
    size = 100, 100
    defaultBtnColor = 255, 0, 255
    btnColor = defaultBtnColor
    textColor = 255, 255, 255
    btnPadding = 10
    btnInitPos = [0, 0]

    def __init__(self, pos, text, size = []):
        if size:
            self.size = size
        self.pos = pos
        self.text = text

    def draw(self, img):
        x, y = self.pos
        w, h = self.size
        cv2.rectangle(img, self.pos, (x+w, y+h), self.btnColor, cv2.FILLED)
        cv2.putText(img, self.text, (x+30, y+60), cv2.FONT_HERSHEY_PLAIN, 3, self.textColor, 4)

    def action(self, detector, lm_list, img):
        # check index and middle finger position and take action

        if self.pos[0] < lm_list[8][0] < self.pos[0] + self.size[0] and self.pos[1] < lm_list[8][1] < self.pos[1] + self.size[1]:
            l, _, _ = detector.findDistance(8, 12, img)
            if l <= 40:
                self._click()
                return self.text
            else:
                return self._hover()
        else:
            self.btnColor = self.defaultBtnColor
            return None

    def _hover(self):
        # Change color on hover
        self.btnColor = 255, 150, 255

    def _click(self):
        # btn click functionality
        self.btnColor = 0, 255, 0