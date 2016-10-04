# import the necessary packages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib
import json
import pyautogui

from sound import get_volume_range

from sound import get_master_volume_level

from sound import set_master_volume_level


@csrf_exempt
def volume(request):
    # initialize the data dictionary to be returned by the request
    data = {"success": False}

    # check to see if this is a post request
    if request.method == "POST":
        # assume that a mainFrame was passed in
        if request.POST.get("volume", None) is not None:
            data["success"] = True
            # TEST BLOCk ##################################################
            volume = request.POST.get("volume", None)
            vmin, vmax, vinc = get_volume_range()
            vol = get_master_volume_level()
            print('Volume Range : %0.4f, %0.4f, %0.4f' % (vmin, vmax, vinc))
            print('Master Volume: %0.4f' % vol)
            print('\nIncrementing the master volume...')

            if volume == 'up':
                print 'Volume up'
                set_master_volume_level(vol + vinc + 1)
                vol = get_master_volume_level()
                print('New Master Volume: %0.4f' % vol)
            elif volume == 'down':
                set_master_volume_level(vol + vinc - 1)
                vol = get_master_volume_level()
                print('New Master Volume: %0.4f' % vol)
                print 'Volume down'
            elif volume == 'mute':
                set_master_volume_level(-60)
                vol = get_master_volume_level()
                print('New Master Volume: %0.4f' % vol)
                print 'Volume down'
            elif volume == 'max':
                set_master_volume_level(0)
                vol = get_master_volume_level()
                print('New Master Volume: %0.4f' % vol)
                print 'Volume down'
        if request.POST.get("play", None) is not None:
            data["success"] = True
            play = request.POST.get("play", None)
            if play == 'yes':
                pyautogui.press('space')
        if request.POST.get("move", None) is not None:
            data["success"] = True
            play = request.POST.get("move", None)
            if play == 'next':
                pyautogui.press('right')
            else:
                pyautogui.press('left')
            # TEST BLOCk ##################################################
    # return a JSON response
    return JsonResponse(data)