import re


username_pattern = re.compile("^[a-z|A-Z|0-9]{3,12}$")
password_pattern = re.compile("^[a-z|A-Z|0-9]{6,20}$")
email_pattern = re.compile("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
age_pattern = re.compile("^[0-9]{1,2}$")

form = {"username": username_pattern, "password": password_pattern, "email": email_pattern, "age": age_pattern}

while True:
    answer = input("1 - Register\n2 - Login\n3 - Exit\n")
    if answer == "1":
        for key in form:
            file = open("text.txt", "a")
            while True:
                field = input("Enter your "+ key +" :")
                if form[key].match(field):
                    file.write(key+":"+field+",")
                    break
        file.write("\n")
        file.close()

    elif answer == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        file = open("text.txt", "r")
        for line in file:
            stripped_line = line.strip()
            stripped_line = stripped_line.split(",")
            usernameLine = stripped_line[0].split(":")[1]
            passwordLine = stripped_line[1].split(":")[1]
            print("Username: " + usernameLine + " Password: " + passwordLine)
            if usernameLine == username and passwordLine == password:
                ##########################################################################3


                print("Choose a number")
                print("1- for Create Project")
                print("2- for View All Projects")
                print("3- for Edit Project")
                print("4- for Delete Project")
                print("5- for Search for a Project using Date")
                print("6- for Exit")
                sub_menu_select = input("Enter Your Number : ")

                while True:
                    if sub_menu_select == "1":
                        print("Create Project")
                        print("----------------")
                        
                        db = open("projectsdb.json",'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)

                        while True:
                            title = input("Enter Project Title : ")
                            if title:
                                for project in projects:
                                    if project['title'] == title:
                                        print("Project Title must be unique")
                                        break
                                else:
                                    new_project["title"] = title
                                    break

                        details = input("Enter Project Details : ")
                        new_project["details"] = details

                        total_target = input("Enter Project Total Target : ")
                        new_project["total_target"] = total_target

                        while True:
                            start_time = input("Enter Project Start Time : ")
                            try:
                                datetime.datetime.strptime(start_time, '%Y-%m-%d')
                                new_project["start_time"] = start_time
                                break
                            except ValueError:
                                print("Incorrect data format, should be YYYY-MM-DD")

                        while True:
                            end_time = input("Enter Project End Time : ")
                            try:
                                datetime.datetime.strptime(end_time, '%Y-%m-%d')
                                new_project["end_time"] = end_time
                                break
                            except ValueError:
                                print("Incorrect data format, should be YYYY-MM-DD")

                        new_project['auther'] = author

                        print("--------------------------------")

                        projects.append(new_project)

                        db = open("projectsdb.json",'w')
                        db.write(json.dumps(projects))
                        db.close()

                        break
                    elif sub_menu_select == "2":
                        print("View All Projects")
                        print("-------------------")
                        db = open("projectsdb.json",'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)

                        for project in projects:

                            print("----------------------------------")
                            print(f"Title: {project['title']}")
                            print(f"Details: {project['details']}")
                            print(f"Total Target: {project['total_target']}")
                            print(f"Start Time: {project['start_time']}")
                            print(f"End Time: {project['end_time']}")
                            print(f"Auther: {project['auther']}")
                            print("----------------------------------")

                        break
                    elif sub_menu_select == "3":
                        print("Edit Project")
                        print("---------------")
                        
                        project_title = input("Enter Project Title To Edit : ")

                        db = open("projectsdb.json",'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)

                        for project in projects:
                            
                            if project['title'] == project_title and project['auther'] == author:
                                
                                isExists = True
                                
                                print("-----------------------------------------------------")
                                title = input("Enter New Title or press enter to skip it : ")
                                if title:
                                    project["title"] = title

                                details = input("Enter New Details or press enter to skip it : ")
                                if details:
                                    project["details"] = details

                                total_target = input("Enter New Total Target or press enter to skip it : ")
                                if total_target:
                                    project["total_target"] = total_target

                                start_time = input("Enter New Start Time or press enter to skip it : ")
                                if start_time:
                                    while True:
                                        try:
                                            datetime.datetime.strptime(start_time, '%Y-%m-%d')
                                            project["start_time"] = start_time
                                            break
                                        except ValueError:
                                            print("Incorrect data format, should be YYYY-MM-DD")

                                        start_time = input("Enter New Start Time or press enter to skip it : ")

                                        if not start_time:
                                            break

                                end_time = input("Enter New End Time or press enter to skip it : ")
                                if end_time:
                                    while True:
                                        try:
                                            datetime.datetime.strptime(end_time, '%Y-%m-%d')
                                            project["end_time"] = end_time
                                            break
                                        except ValueError:
                                            print("Incorrect data format, should be YYYY-MM-DD")

                                        end_time = input("Enter New End Time or press enter to skip it : ")

                                        if not end_time:
                                            break


                                print("-----------------------------------------------------")
                                
                                db = open("projectsdb.json",'w')
                                db.write(json.dumps(projects))
                                db.close()
                                print("Project Edited successfully")
                                break
                        
                        if isExists == False:
                            print("This Product Doesn't Exists")

                        break
                    elif sub_menu_select == "4":
                        print("Delete Project")
                        print("----------------")

                        project_title = input("Enter Project Title To Delete : ")

                        db = open("projectsdb.json",'r')
                        data = db.read()
                        db.close()

                        projects = json.loads(data)
                        
                        for index,project in enumerate(projects):
                            
                            if project['title'] == project_title and project['auther'] == author:
                                
                                isExists = True

                                projects.pop(index)

                                db = open("projectsdb.json",'w')
                                db.write(json.dumps(projects))
                                db.close()
                                print("Project Deleted successfully")
                                break

                        if isExists == False:
                            print("This Product Doesn't Exists")

                        break
                    elif sub_menu_select == "5":
                        print("Search for a Project using Start Date")
                        print("--------------------------------------")

                        while True:
                            project_start_date = input("Enter Project Start Date to Search : ")
                            try:
                                datetime.datetime.strptime(project_start_date, '%Y-%m-%d')

                                db = open("projectsdb.json",'r')
                                data = db.read()
                                db.close()

                                projects = json.loads(data)
                                
                                for project in projects:
                                    
                                    if project['start_time'] == project_start_date and project['auther'] == author:
                                        
                                        isExists = True

                                        print("----------------------------------")
                                        print(f"Title: {project['title']}")
                                        print(f"Details: {project['details']}")
                                        print(f"Total Target: {project['total_target']}")
                                        print(f"Start Time: {project['start_time']}")
                                        print(f"End Time: {project['end_time']}")
                                        print(f"Auther: {project['auther']}")
                                        print("----------------------------------")
                                        break

                            except ValueError:
                                print("Incorrect data format, should be YYYY-MM-DD")

                            if isExists == False:
                                print("This Product Doesn't Exists")
                                
                            break

                    elif sub_menu_select == "6":
                        break


                #################################################################                3
                break
            else:
                print("Failed")

    elif answer == "3":
        break

    else:
        print("Enter a valid Choice")
