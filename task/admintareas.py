class Task:
    def __init__(self,title,description=""):
        self.title=title
        self.description=description
        self.completed=False

    def mark_completed(self):
        self.completed=True    

    def __str__(self):
        status = "✅" if self.completed else "❌"  
        return f"{status} {self.title} - {self.description}"
        

tarea1 = Task(title="Aprende POO",description="Revisar el capitulo IV CC")
tarea2 = Task(title="Aprende TKINTER",description="Revisar el capitulo V CC")
tarea3 = Task(title="Aprende BD",description="Revisar el capitulo VI CC")


class TaskMananger:
    def __init__(self):
        self.tasks=[] #Esta es una Lista Vacia de Tareas
    def add_task(self,title,description=""):
        task=Task(title,description)
        self.tasks.append(task)
    def list_tasks(self):
        if not self.tasks:    
            print("No Hay Tareas aun.")
            return
        for i,task in enumerate(self.tasks,start=1):
            print(f"{i}. {task}")
    def complete_task(self,index):
        if 0<=index <len(self.tasks):
            self.tasks[index].mark_completed()      
            print("Tarea Completada")  
        else:
            print("Indice Invalido")    


if __name__=="__main__":
    mananger=TaskMananger()

    #Agregamos algunas Tareas
    mananger.add_task("Estudiar POO","Repasar Conceptos de Clases y Objetos")
    mananger.add_task("Hacer Ejercicio","Caminar 30 Minutos")
    mananger.add_task("Dormir 8 Horas","Recuperar Energias")

    print("\n Listar Tareas:")
    mananger.complete_task(0)
    mananger.complete_task(2)
    mananger.list_tasks()




#print(tarea3)
#print(f"{tarea1.title} {tarea1.description}")        
#print(f"{tarea2.title} {tarea2.description}")        
#print(f"{tarea3.title} {tarea3.description}")        
