import pyautogui
import pywinauto
import pygetwindow
import time


def setFocus():
    handle = None

    app = pywinauto.application.Application(backend="win32")
    title_reg = u'LDPlayer' '.*'
    t = title_reg

    print('find title : ' + str(title_reg))

    try:
        test = pywinauto.findwindows.find_windows(title_re=t)
        print(test)

        # title 을 기반으로 window handle 을 가져옴
        handle = pywinauto.findwindows.find_windows(title_re=t)[0]
        # 해당 윈도우 Control을 위해 라이브러리와 연결
        app.connect(handle=handle).top_window()

        print('title: ' + str(t) + '\nhandle: ' + str(handle) + ' Set')
    except (NameError, IndexError):
        print('No title exist on window ')

    # 어플리케이션의 window를 가져옴
    window = app.window(handle=handle)

    try:
        # 해당 윈도우를 탑으로 설정
        window.set_focus()
        window.move_window(x=300, y=300, width=None, height=None)
    except Exception as e:
        print('[error]setFocus : ' + str(e))

    return window


def setFocusApp():
    return setFocus()


def clickNumber():
    # while True:
    #     x, y = pyautogui.position()
    #     position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    #     print(position_str, end='')
    #     print('\b' * len(position_str), end='', flush=True)

    while True:
        btn_img = pyautogui.locateCenterOnScreen('eight.png', confidence=0.7)
        print('btn_img', btn_img)
        if btn_img is not None:
            pyautogui.click(btn_img)
            break


if __name__ == "__main__":
    setFocusApp()
    clickNumber()
#
# if not win.isActive:
#     pywinauto.application.Application(backend='uia').connect(title='계산기').top_window().set_focus()
#
# btn_img = pyautogui.locateCenterOnScreen('eight.png')
#
# print(btn_img)
#
# pyautogui.click(btn_img)
