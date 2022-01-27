import taskEncoder, taskUser
import shares

zFlag = shares.Share(False)
pVar = shares.Share()
dVar = shares.Share()

if __name__ == "__main__":
    # Instantiate task objects
    userTask = taskUser.taskUserFcn('Task User', 10000, zFlag, pVar, dVar)
    encoderTask = taskEncoder.taskEncoderFcn('Task encoder', 10000, zFlag, pVar, dVar)
    taskList = [userTask, encoderTask]
    
    while True:
        try:
            for task in taskList:
                next(task)
                
        except KeyboardInterrupt:
            break
        
    print("Keybaord Interrupt, stopping")
    