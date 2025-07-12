import time
import pyautogui

screen_width, screen_height = pyautogui.size()

#15-30% from each edge
margin_x = int(screen_width * 0.15)
margin_y = int(screen_height * 0.3)

#rectangle corners
top_left = (margin_x, margin_y)
top_right = (screen_width - margin_x, margin_y)
bottom_right = (screen_width - margin_x, screen_height - margin_y)
bottom_left = (margin_x, screen_height - margin_y)

print(f"Screen size: {screen_width}x{screen_height}")
print(f"Rectangle corners: {top_left}, {top_right}, {bottom_right}, {bottom_left}")

#let the user switch to their window
time.sleep(5)

pyautogui.moveTo(top_left[0], top_left[1], duration=0.3)

#move mouse in a rectangle pattern continuously
while True:

    pyautogui.moveTo(top_right[0], top_right[1], duration=0.3)
    pyautogui.moveTo(bottom_right[0], bottom_right[1], duration=0.3)
    pyautogui.moveTo(bottom_left[0], bottom_left[1], duration=0.3)
    pyautogui.moveTo(top_left[0], top_left[1], duration=0.3)
