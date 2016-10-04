# import the necessary packages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib
import json
import pyautogui



@csrf_exempt
def click(request):
    # initialize the data dictionary to be returned by the request
    data = {"success": False}

    # check to see if this is a post request
    if request.method == "POST":
        # assume that a mainFrame was passed in
        if request.POST.get("hotkey", None) is not None:
            data["success"] = True
            # TEST BLOCk ##################################################
            hotkey = request.POST.get("hotkey", None)
            pyautogui.press(hotkey)

            # TEST BLOCk ##################################################
    # return a JSON response
    return JsonResponse(data)
