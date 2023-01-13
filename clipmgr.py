import win32clipboard as cb # pywin32
import keyboard

hotkey_list = list()
mem_dict = dict()

for n in range(0,10):
    hotkey_list.append((f'ctrl+alt+shift+{n}', f'ctrl+{n}', n))

def set_cb(trigger_id):
    print('set_cb :', trigger_id)
    cb.OpenClipboard()
    try:
        cb_data = cb.GetClipboardData(cb.CF_UNICODETEXT)
        mem_dict[trigger_id] = cb_data
    except Exception as e:
           print(e)
    cb.CloseClipboard()
    
def get_cb(trigger_id):
    print('get_cb :', trigger_id)
    if trigger_id in mem_dict:
        cb.OpenClipboard()
        try:
            # cb.SetClipboardText(mem_dict[trigger_id], cb.CF_TEXT)
            keyboard.write(mem_dict[trigger_id])
        except Exception as e:
           print(e)
        cb.CloseClipboard()

for k in hotkey_list:
    keyboard.add_hotkey(k[0],set_cb, args=(k[2],))
    keyboard.add_hotkey(k[1],get_cb, args=(k[2],))

keyboard.wait()
