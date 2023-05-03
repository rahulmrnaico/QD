import jenkins
import json
import os



host = "http://localhost:8080"
username = "rahulmrnaico" #jenkins username here
password = "113a35aa8955524fe4d6b40b40258eb964" # Jenkins user password / api token here
server = jenkins.Jenkins(host, username=username, password=password) #automation_user_password

user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))



# #Create deployment jobs

# #create a blank job
# server.create_job("job1", jenkins.EMPTY_CONFIG_XML)

# #create pre-configured-job
# job2_xml = open("job2.xml", mode='r', encoding='utf-8').read()
# server.create_job("job2", job2_xml)

# job3_xml = open("job3.xml", mode='r', encoding='utf-8').read()
# server.create_job("job3", job3_xml)

#view jobs
# jobs = server.get_jobs()
# print(jobs)

#copy job
# server.copy_job('job2', 'job4')

#update job
# updated_job_3 = open("job_3_updated.xml", mode='r', encoding='utf-8').read()
# server.reconfig_job('job3', updated_job_3)

#disable job
# server.disable_job('sample_job')

# Run a build and get build number and more info
# server.build_job('Technology')
# last_build_number = server.get_job_info('Technology')['lastCompletedBuild']['number']
# print("Build Number", last_build_number)
# build_info = server.get_build_info('Technology', last_build_number)
# print("build info", build_info)


#stop a build
# server.stop_build('Technology', 41)

#get build console output
last_build_number = server.get_job_info('Technology')['lastCompletedBuild']['number']
# views=server.get_build_console_output("Technology", 43)
print(last_build_number)
#delete job
# server.delete_job('sample_job')


# Create View
# view_config = open("jobs_view.xml", mode='r', encoding='utf-8').read()
# server.create_view("Job List", view_config)

#get list of view
# views = server.get_views()
# print(views)

# Update View
# updated_view_config = open("jobs_view_updated.xml", mode='r', encoding='utf-8').read()
# server.reconfig_view("Job List", updated_view_config)

#Delete View
# server.delete_view("Job List")



# Get Build ouput
# views = server.get_build_test_report('Technology',38)
# views = server.get_build_console_output('Technology',38)
# print(views)
# file2 = open("file2.txt", "w+")
# file2.write(views)
# file2.close()