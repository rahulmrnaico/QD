from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
import subprocess
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
import jenkins

host = "http://localhost:8080"
username = "rahulmrnaico" #jenkins username here
password = "113a35aa8955524fe4d6b40b40258eb964" # Jenkins user password / api token here
server = jenkins.Jenkins(host, username=username, password=password) #automation_user_password



# Run a build and get build number and more info using api
def build_start(request):
    if request.method == 'GET':
        try:
            server.build_job('Technology')
            last_build_number = server.get_job_info('Technology')['lastCompletedBuild']['number']
            print("Build Number", last_build_number)
            build_info = server.get_build_info('Technology', last_build_number)
            print("build info", build_info)
           
            return JsonResponse({'status': 'Build started successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return HttpResponseBadRequest()


# Run a build using subprocess
def build_start_sub(request):
    if request.method == 'GET':
        try:
            subprocess.Popen('curl -X POST -L --user rahulmrnaico:113a35aa8955524fe4d6b40b40258eb964 "http://192.168.0.108:8080/job/Technology/build/start"', shell=True)  
            return JsonResponse({'status': 'Build started successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return HttpResponseBadRequest()


# Get Console log of a specific build and download it in a text file using api
def build_log(request):
    if request.method == 'GET':
        try:
            views = server.get_build_console_output('Technology',38)
            print(views)
            file2 = open("log.txt", "w+")
            file2.write(views)
            file2.close()
            return JsonResponse({'status': 'Build log downloaded successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return HttpResponseBadRequest()


# Get status of build using subprocess
@api_view(['GET'])
def build_status_sub(request):
    if request.method == 'GET':
          p=subprocess.Popen('curl -g -u rahulmrnaico:113a35aa8955524fe4d6b40b40258eb964 "http://192.168.0.108:8080/job/Technology/lastBuild/api/json"', shell=True, stdout=subprocess.PIPE)
          out, err = p.communicate() 
          msg=out.decode('utf-8') 
          print(msg)       
    return HttpResponse(msg)

    
# Stop a build using api
def build_stop(request):
    if request.method == 'GET':
        try:
            last_build_number = server.get_job_info('Technology')['lastCompletedBuild']['number']
            server.stop_build('Technology', last_build_number)
           
            return JsonResponse({'status': 'Build stopped successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return HttpResponseBadRequest()


# Stop a build using subprocess
def build_stop_sub(request):
     if request.method == 'GET':
        try:
            subprocess.Popen('curl -X POST -L --user rahulmrnaico:113a35aa8955524fe4d6b40b40258eb964 "http://192.168.0.108:8080/job/Technology/lastB+uild/stop"', shell=True)
            return JsonResponse({'status': 'Stopped the build succesfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
     else:
        return HttpResponseBadRequest()



from Adapter1 import MySQLAdapter 
adapter = MySQLAdapter(host="localhost", username="yourusername", password="yourpassword", database="yourdatabase")
results = adapter.execute("SELECT * FROM yourtable")
for result in results:
    print(result)
adapter.close()






     





@csrf_exempt
@api_view(['POST'])
def post(request):
    if request.method =='POST':
        try:
            data = json.loads(request.body)
            with open('API/tree .json', 'r+') as f:
                try:
                    existing_data = json.load(f)
                except:
                    existing_data = {}
                existing_data.update(data)
                f.seek(0)
                json.dump(existing_data, f)
                f.truncate()
               
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return HttpResponseBadRequest()


@api_view(['GET'])
def initialize(request):
    if request.method == 'GET':
        try:


            
            return JsonResponse({'status':'success'})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return HttpResponseBadRequest()